from molmass import Formula
import math
Message = "Gas, Temperature: "
RawData = input(Message)
while(RawData != "quit"):
    SplitData = RawData.split(" ")
    F1 = Formula(SplitData[0])
    Mr = F1.mass
    T1 = float(SplitData[1]) + 273.15

    Vrms = math.sqrt(3 * (1.38065 / 10**23) * T1 / ((Mr/1000)/(6.02214 * 10**23)))
    print("Vrms = ",Vrms)

    RawData = input(Message)