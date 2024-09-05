import pygame
import numpy as np

# Initialize Pygame mixer for stereo sound
pygame.mixer.init(frequency=44100, size=-16, channels=2)  # 44100 Hz, 16-bit signed, stereo
pygame.init()

# Parameters for the sound
frequency = 440  # Frequency in Hz (A4)
duration = 1.0   # Duration in seconds
sample_rate = 44100  # Sample rate

n_samples = int(round(duration*sample_rate))

#setup our numpy array to handle 16 bit ints, which is what we set our mixer to expect with "bits" up above
buf = np.zeros((n_samples, 2), dtype=np.int16)
max_sample = 2**(16 - 1) - 1

# Generate the sound waveform
t = np.linspace(0, duration, int(sample_rate * duration), False)
waveform = 0.5 * np.sin(2 * np.pi * frequency * t)  # Sine wave with 50% volume
waveform = np.int16(waveform * 32767)  # Convert to 16-bit PCM format

# Create a stereo waveform by duplicating the mono waveform across two channels
waveform_stereo = np.column_stack((waveform, waveform))

# Create a Pygame sound object
#sound = pygame.sndarray.make_sound(waveform_stereo)
sound = pygame.mixer.Sound(waveform_stereo)
print(waveform)
# Play the sound
sound.play()

# Keep the program running long enough to hear the sound
pygame.time.delay(int(duration * 1000))
print(pygame.mixer.get_num_channels())
# Quit Pygame mixer
pygame.mixer.quit()