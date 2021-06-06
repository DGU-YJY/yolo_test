import playsound
import random
import os
import pandas as pd
import pyaudio
import wave
### 참고로 pygame 버전 1.9.x 해야함
def run_wav(path):
	chunk = 1024
	with wave.open(path, 'rb') as f:
		p = pyaudio.PyAudio()
		stream = p.open(format = p.get_format_from_width(f.getsampwidth()),channels = f.getnchannels(), rate = f.getframerate(), output= True)
		data = f.readframes(chunk)
		while data:
			stream.write(data)
			data = f.readframes(chunk)
		stream.stop_stream()
		stream.close()
		p.terminate()