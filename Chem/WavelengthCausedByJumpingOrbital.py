RawData = input("From orbit n1 to n2 isinput_energy(1/0): ")
while(RawData != "quit"):
    SplitData = RawData.split(" ")
    A = float(SplitData[0])
    B = float(SplitData[1])
    if(SplitData[2].lower() != "1"):
        wavelength = 299792458.0 * 6.62607 / 10**34 / (2.17987 /10 ** 18 * (1/ A**2 - 1/ B**2))
    else:
        wavelength = 299792458.0 * 6.62607 / 10**34 / (abs(A-B)/10**21)
    print(wavelength, " m")
    print(wavelength*1000, " mm")
    print(wavelength*1000000, " um")
    print(wavelength*1000000000, " nm")
    RawData = input("From n1 to n2: ")