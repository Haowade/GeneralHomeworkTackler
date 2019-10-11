from molmass import Formula
RawData = input("Gas Formula, to second Gas, ratio, x for unknown: ")
while(RawData != "quit"):
    SplitData = RawData.split(" ")
    F0 = SplitData[0]
    F = Formula(F0)
    R = float(SplitData[1])
    print("Results: x = ", F.mass/(R**2))
    RawData = input("Gas Formula, Mass, Temp(C), Volume, Pressure, x for unknown: ")