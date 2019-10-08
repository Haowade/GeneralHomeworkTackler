import numpy as np

# allows matplotlib charts to be displayed inside the notebook
import matplotlib.pyplot as plt

# let us read .wav audio files
from scipy.io import wavfile
#help(wavfile)

# let us play audio in Jupyter
from IPython.display import Audio

ys = np.loadtxt("piano.txt") # load the array into the variable ys

fs =  44100 # sample rate (Hz)

# Create an audio object using these numbers that makes the speakers vibrate according to these numbers and generate these piano note
Audio(ys,rate=fs) 

N = ys.size  # number of samples
fs = 44100   # sample rate (Hz)
L = 2.2675     # Length of the audio clip (sec)

# we need N time inputs. divide interval [0,L] in N equally spaced points
ts = np.linspace(0, L, N)

# We can now plot!
fig, ax = plt.subplots(2,2)
ax[1,0].plot(ts,ys)
ax[1,0].set_xlim(0,3)
ax[0,0].set_xlabel("t")

# print(1/L) 
f1 = 1/L                   # fundamental frequency
k = np.arange(N)              # 0 to N-1
freqs = k*f1              # harmonics

"""Print frequencies"""
print(f1)
for x in range(10):
    print(freqs[x])

# Call the Fast Fourier Transform FFT
yk = np.fft.fft(ys)

"""Print yk"""
print(yk)
"""Call the function np.isreal"""
np.isreal(yk)

print("It is recorded in a complex plane as a complex number,\n\
which is intuitive for describing any thing with a period")

ax[0,0].plot(freqs,abs(yk))
ax[0,0].set_xlabel("f (Hz)")
ax[0,0].set_xlim(0,600)

ax[0,1].plot(freqs,abs(yk))
ax[0,1].set_xlabel("f (Hz)")
ax[0,1].set_xlim(0,5000)
print("C5")

"""Plot the phase of yk"""
ax[1,1].plot(freqs,np.angle(yk))
ax[1,1].set_xlabel("Phase (Rad)")
ax[1,1].set_xlim(0,5000)

plt.show()