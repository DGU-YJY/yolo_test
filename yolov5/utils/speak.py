from gtts import gTTS
from time import sleep
import pyglet
import os



def speak(talk):
    print(talk)
    tts = gTTS(text=talk, lang = 'ko')
    talkfile = "talk.mp3"
    tts.save(talkfile)
    music = pyglet.media.load(talkfile, streaming=False)
    music.play()

    sleep(music.duration) #prevent from killing
    os.remove(talkfile) #remove temperory file

