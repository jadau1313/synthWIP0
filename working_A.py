import numpy as np
import pygame as pg

pg.init()
pg.mixer.init()

sampling_rate = 44100
frequency = 440 #hz
duration = 6 #seconds
frames = int(duration * sampling_rate)
octave = 0.25
amp = .5

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
waveform = amp * np.cos(octave*np.pi*frequency*t)

#waveform = np.clip(10*waveform, -1, 1) #square wave...test this

'''
#triangle wave...test this
waveform = np.cumsum(np.clip(waveform*10, -1, 1))
waveform = waveform/max(np.abs(waveform))
'''

waveform = np.int16(waveform*32767)

print(waveform)
sound = pg.mixer.Sound(waveform)
sound.play()
pg.time.wait(1500)