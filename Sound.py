import sounddevice
from scipy.io.wavfile import write
from playsound import playsound

class Sound:

    def __init__(self):
        fs = 44100
        seconds = 5
        x = input("To start recording press Y")
        while x.upper() is not 'Y':
            x = input("To start recording press Y")


