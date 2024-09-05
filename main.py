# This is a sample Python script.
import numpy as np
import pygame as pg

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

pg.init()
pg.mixer.init()

sampling_rate = 44100
frequency = 440 #hz
duration = 6 #seconds
frames = int(duration * sampling_rate)
octave = 1
amp = .5


wave1 = np.cos(octave*np.pi*np.arange(sampling_rate) * frequency / sampling_rate).astype(np.float16)
wave2 = np.cos(octave*np.pi*np.arange(sampling_rate) * frequency / sampling_rate).astype(np.float16) #test this

t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
waveform = amp * np.cos(octave*np.pi*frequency*t)
waveform = np.int16(waveform*32767)
#sound = np.asarray([32767*wave_array, 32767*wave_array]).T.astype(np.int16)
#sound = pg.sndarray.make_sound(sound.copy())
#sample0 = np.asarray()

sound = pg.mixer.Sound(waveform)
sound.play()
pg.time.wait(1000)

##good example here all parameters produce a response, not using frames for anything tho
