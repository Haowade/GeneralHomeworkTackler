import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from IPython.display import Audio

f1 = 200
f2 = 20
f = 20000

fig, (ax,ax1) = plt.subplots(2)
t = np.arange(0,1,1/f)
y = np.cos(2*np.pi*f1*t) * np.cos(2*np.pi*f2*t)
ax.plot(np.arange(len(y)),y)
ax.set_ylabel('|Amplitude|')
ax.set_xlim(0,f/4)

Audio(y,rate=f) #Only in IPython notebook

y1 = np.cos(2*np.pi*f1*t)
Audio(y,rate=f) #Only in IPython notebook

y = 5+4*y
ax1.plot(np.arange(len(y)),y)
ax1.set_ylabel('|Amplitude|')
ax1.set_xlim(0,f/4)

plt.show()