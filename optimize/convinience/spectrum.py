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
