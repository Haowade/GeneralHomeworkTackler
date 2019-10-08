from molmass import Formula
import math
Message = "Acid Mass, Conc NaOH, V NaOH, X-protic: "
RawData = input(Message)
while(RawData != "quit"):
    SplitData = RawData.split(" ")
    M0 = float(SplitData[0])
    C1 = float(SplitData[1])
    V1 = float(SplitData[2])
    X1 = float(SplitData[3])

    Mr = M0 / ((V1 * C1)/X1)
    print("Mr = ",Mr)

    RawData = input(Message)