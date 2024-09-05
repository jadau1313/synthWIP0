import wave
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sound
frequency = 440  # Frequency in Hz (A4)
duration = 1.5   # Duration in seconds
sample_rate = 44100  # Sample rate
amplitude = 0.5  # Amplitude (volume)

# Generate the sound waveform
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
waveform = amplitude * np.sin(2 * np.pi * frequency * t)

#waveform = np.clip(10*waveform, -1, 1) #square wave...test this...9.2.24 this works, PCM 16bit conversion needs to happen after
'''
#triangle wave...test this ...9.2.24 this works, make sure the conversion to 16bit PCM occurs after
waveform = np.cumsum(np.clip(waveform*10, -1, 1))
waveform = waveform/max(np.abs(waveform))
'''

waveform = np.int16(waveform * 32767)  # Convert to 16-bit PCM format





# Write the waveform to a WAV file
with wave.open('sound.wav', 'wb') as wf:
    wf.setnchannels(1)  # Mono
    wf.setsampwidth(2)  # 2 bytes per sample (16 bits)
    wf.setframerate(sample_rate)
    wf.writeframes(waveform.tobytes())

import pygame



# Initialize Pygame mixer
pygame.mixer.init()

# Load and play the WAV file
sound = pygame.mixer.Sound('sound.wav')
sound.play()

# Keep the program running long enough to hear the sound
pygame.time.wait(1000)  # Wait for 1 second

soundfile = wave.open('sound.wav')
signal = soundfile.readframes(-1)
signal = np.frombuffer(signal, dtype=np.int16)
fs = soundfile.getframerate()
# Create a time array
time = np.linspace(0, len(signal) / fs, num=len(signal))

# Plot the waveform
plt.figure(figsize=(10, 4))
plt.plot(time, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Waveform')
plt.show()

# Quit Pygame mixer
pygame.mixer.quit()