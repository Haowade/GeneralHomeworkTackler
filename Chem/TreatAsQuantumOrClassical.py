RawData = input("Plank-Constant mass speed length: ")
while(RawData != "quit"):
    SplitData = RawData.split(" ")
    h = float (SplitData[0])
    m = float (SplitData[1])
    v = float (SplitData[2])
    l = float (SplitData[3])

    wavelength = h / (m * v)

    print(wavelength)
    if(wavelength > l):print("Quantum")
    elif(wavelength < l):print("Classical")
    RawData = input("Plank-Constant mass speed length")