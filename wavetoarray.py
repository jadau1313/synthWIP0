# This is a sample Python script.
import numpy as np
import pygame as pg

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

pg.init()
pg.mixer.init()

sampling_rate = 44100
frequency = 440 #hz
duration = 1.5 #seconds
amplitude = 0.5

t = np.linspace(0, duration, int(sampling_rate*duration), endpoint=False)
waveform = amplitude * np.cos(2*np.pi*frequency*t)

waveform_pcm = np.int16(waveform*32767)

sound = np.asarray([waveform_pcm, waveform_pcm]).T.astype(np.float16)
sound = pg.sndarray.make_sound(sound.copy())
sound1 = pg.mixer.Sound(sound)
sound1.play()

#print("Waveform array:", waveform_pcm)
#print("Shape of waveform array:", waveform_pcm.shape)

"""
frames = int(duration * sampling_rate)
wave1 = np.cos(0.5*np.pi*np.arange(sampling_rate) * frequency / sampling_rate).astype(np.float16)
wave2 = np.cos(0.5*np.pi*np.arange(sampling_rate) * frequency / sampling_rate).astype(np.float16) #test this
#sound = np.asarray([32767*wave_array, 32767*wave_array]).T.astype(np.int16)
#sound = pg.sndarray.make_sound(sound.copy())
sample0 = np.asarray()
sound = pg.mixer.Sound(wave1)
sound.play()
pg.time.wait(1500)
"""