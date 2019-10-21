def SpectrumFind(Fs):
    fs = Fs                # sampling frequency (Hz)
    t_max = 0.2             # signal duration (sec)
    N = round(t_max*fs)     # number of samples
    t = np.linspace(0,t_max,N)
    s_t = 10 + 20*np.cos(200*np.pi*t+np.pi/4) + 10*np.cos(500*np.pi*t)
    S_f = np.fft.fft(s_t)             # list of FFT coefficients
    print(len(S_f))
    freqs = fs/N*np.linspace(0,N-1,N) # list of frequencies corresponding to the coefficients returned by fft
    # Plot magnitude of FFT coefficients 
    fig, ax = plt.subplots()
    ax.plot(freqs,abs(S_f))
    ax.set_xlabel("f (Hz)")
    ax.set_xlim(0,fs)           # you might need to adjust the value here to better see the dominant frequencies
    print('The sampling frequency is', fs, 'Hz')

SpectrumFind(5000)
SpectrumFind(700)
SpectrumFind(400)
SpectrumFind(500)