from molmass import Formula
import math
Message = "Acid Formula, Acid Mass, V NaOH, X-protic: "
RawData = input(Message)
while(RawData != "quit"):
    SplitData = RawData.split(" ")
    F1 = Formula(SplitData[0])
    M1 = float(SplitData[1])
    V1 = float(SplitData[2])
    X1 = float(SplitData[3])

    Conc = M1 / F1.mass * X1 / V1

    print("Conc = ",Conc)

    RawData = input(Message)