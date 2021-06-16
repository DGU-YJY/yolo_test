import speech_recognition as sr
from utils.speak import *


def listening(to = None):

    r = sr.Recognizer()
    r.energy_threshold = 3500
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout = to)

    data = ""
    # Speech recognition using Google Speech Recognition
    try:
        data =  r.recognize_google(audio, language = 'ko-KR')
        print("You said: " + data)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        pass
    return data