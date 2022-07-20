import requests


def getWSrange(ws_ip: str):
    """ startFreq < endFreq
    endFreq(short wavelength) and startFreq(long wavelength)
    """
    result = requests.get('http://'+ws_ip+'/waveshaper/devinfo').json()
    startFreq = result['startfreq']
    endFreq   = result['stopfreq']
    return startFreq, endFreq