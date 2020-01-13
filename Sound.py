#import sounddevice
#from scipy.io.wavfile import write
from playsound import playsound


def play_record(file_path):
    """
    Input - the file path by string
    Output - None
    play the file
    """
    print("Playing")
    playsound(file_path)
    sounddevice.wait()


class Sound:

    def __init__(self, contact_name):
        """
        Input - contact name by string
        Output - None
        recode the user voice
        """
        fs = 44100
        second = 3
        x = input("To start recording press Y - ")
        while x.upper() != 'Y':
            x = input("To start recording press Y - ")
        print("Recording")
        record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
        sounddevice.wait()
        print("Recording Done")
        sounddevice.play(record_voice, fs)
        sounddevice.wait()
        y = input("To save the file enter yes \nTo try again press any button\n")
        while y.upper() != 'YES':
            x = input("To start recording press Y - ")
            while x.upper() != 'Y':
                x = input("To start recording press Y - ")
            print("Recording")
            record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
            sounddevice.wait()
            print("Recording Done")
            sounddevice.play(record_voice, fs)
            sounddevice.wait()
            y = input("To save the file enter yes \nTo try again press any button\n")
        self.file_path = "Sound/" + contact_name + ".wav"
        write(self.file_path, fs, record_voice)
