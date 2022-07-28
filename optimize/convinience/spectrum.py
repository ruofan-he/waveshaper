import numpy as np
from scipy.interpolate import interp1d
import copy


class Band:
    frequency : np.array = None # THz
    def __init__(self):
        pass

    @property
    def wavelength(self) -> np.array:    # nm
        c = 299792458
        return c/self.frequency/1E3 if self.frequency is not None else None

    @wavelength.setter
    def wavelength(self, wavelength):
        c = 299792458
        self.frequency : np.array = c/wavelength/1E3



class Spectrum:
    powerdensity : np.array = None # dB
    phase        : np.array = None # rad
    band         : Band     = None # THz

    def __init__(self):
        pass

    @property
    def frequency(self) -> np.array:
        return self.band.frequency if self.band is not None else None

    @frequency.setter
    def frequency(self, frequency):
        new_band = Band()
        new_band.frequency = frequency
        self.band = new_band

    @property
    def wavelength(self) -> np.array:
        return self.band.wavelength if self.band is not None else None

    @wavelength.setter
    def wavelength(self, wavelength):
        new_band = Band()
        new_band.wavelength = wavelength
        self.band = new_band



def synthesisSpectrum(spectrum1: Spectrum, spectrum2: Spectrum, band: Band):
    new_spectrum = Spectrum()
    new_spectrum.band = copy.deepcopy(band)
    _, new_spectrum.powerdensity = interp_func(
        spectrum1.frequency, 
        spectrum1.powerdensity,
        spectrum2.frequency,
        spectrum2.powerdensity,
        band.frequency)
    _, new_spectrum.phase = interp_func(
        spectrum1.frequency, 
        spectrum1.phase,
        spectrum2.frequency,
        spectrum2.phase,
        band.frequency)
    return new_spectrum



def interp_func(x1,y1,x2,y2,x):
    interp1 = interp1d(x1,y1, fill_value='extrapolate', kind='nearest')
    interp2 = interp1d(x2,y2, fill_value='extrapolate', kind='nearest')
    return x, interp1(x) + interp2(x)




def gaussian_profile(centerWavelength = 1545.2, bandWidth = 0.3, band : Band= None, dispersion = 0):
    c = 299792458
    spectrum = Spectrum()
    spectrum.band = copy.deepcopy(band)
    spectrum.powerdensity = -10*((band.wavelength - centerWavelength)/(bandWidth/2.0))**2 * 0.3 # dB
    centerFreq = c/(centerWavelength*1E-9)/1E12
    spectrum.phase = (centerWavelength*1E-9)**2/(1*np.pi*c)*(dispersion*1E-2)*((band.frequency-centerFreq)*1E12)**2
    return spectrum

def compensation(optSpectrum: Spectrum, targetSpectrum: Spectrum, band: Band):
    tempSpectrum = copy.deepcopy(optSpectrum)
    tempSpectrum.powerdensity = -tempSpectrum.powerdensity
    new_spectrum = synthesisSpectrum(tempSpectrum, targetSpectrum, band)
    # たとえば1542~1550nm帯域で増幅(new_spectrum.powerdensity)しないように、引いとくとか。
    range_max = np.max(new_spectrum.powerdensity[(1542 < new_spectrum.wavelength) & (new_spectrum.wavelength < 1550)])
    new_spectrum.powerdensity -= range_max
    return new_spectrum

def calc_totalPower(optSpectrum: Spectrum, filterSpectrum: Spectrum):
    # optSpectrumがオリジナルのスペクトラムと仮定して、そこにfilterSpectrum指定されたフィルター適用時の予想パワー[a.u.]単位は不明。まあどうでもいい。
    # 周波数が一定間隔であることを仮定する。まずかったら変えましょう。
    band = copy.deepcopy(optSpectrum.band)
    new_spectrum = synthesisSpectrum(optSpectrum, filterSpectrum, band)
    power = 10*np.log10((10**(new_spectrum.powerdensity/10)).sum())
    return power

def attenuation(spectrum: Spectrum, atten: int):
    new_spectrum = copy.deepcopy(spectrum)
    new_spectrum.powerdensity -= atten
    return new_spectrum