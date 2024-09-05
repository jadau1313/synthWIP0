import numpy as np
import pygame as pg

pg.init()
pg.mixer.init()

sampling_rate = 44100
frequency = 440 #hz
duration = 6 #seconds
frames = int(duration * sampling_rate)
octave = 1
amp = .5

def synth(frequency, duration=1.5, sampling_rate=44100):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    waveform = amp * np.cos(octave * np.pi * frequency * t)
    waveform = np.int16(waveform*32767)
    sound = pg.mixer.Sound(waveform)
    pg.time.wait(1000)
    return sound


keylist = '123456789qwertyuioasdfghjklzxcvbnm,.'
notelistfile = open("noteslist.txt")
noteslistcontent = notelistfile.read()
notelistfile.close()
notelist = noteslistcontent.splitlines()

keymod = '0-='
notes = {}
freq = 16.3516
for i in range(len(notelist)):
    mod = int(i/36)
    key = keylist[i-mod*36]+str(mod)
    sample = synth(freq)
    notes[key] = [sample, notelist[i], freq]
    notes[key][0].set_volume(0.25)
    notes[key][0].play()
    notes[key][0].fadeout(1000)
    pg.time.wait(100)

    freq = freq * 2 ** (1/12)

pg.mixer.quit()
pg.quit()



#waveform = np.clip(10*waveform, -1, 1) #square wave...test this

'''
#triangle wave...test this
waveform = np.cumsum(np.clip(waveform*10, -1, 1))
waveform = waveform/max(np.abs(waveform))
'''



#sound = pg.mixer.Sound(waveform)
#sound.play()
#pg.time.wait(1000)