from molmass import Formula
RawData = input("Gas Formula, Mass, Temp(C), Volume, Pressure, x for unknown: ")
while(RawData != "quit"):
    SplitData = RawData.split(" ")
    F0 = SplitData[0]
    M0 = SplitData[1].lower()
    T0 = SplitData[2].lower()
    V0 = SplitData[3].lower()
    P0 = SplitData[4].lower()
    #Constant
    R = 0.0820574
    Results = 0.0
    if(F0 == "x"):
        M1 = float(M0)
        T1 = float(T0) + 273.15
        V1 = float(V0)
        P1 = float(P0)
        N = P1 * V1/(R * T1)
        Mr = M1 / N
        Results = Mr
        print("Results: mol = ", N)
    if(M0 == "x"):
        F1 = Formula(F0)
        T1 = float(T0) + 273.15
        V1 = float(V0)
        P1 = float(P0)
        N = P1 * V1/(R * T1)
        M1 = N * F1.mass
        Results = M1
        print("Results: x in mol = ", N)
    if(T0 == "x"):
        F1 = Formula(F0)
        M1 = float(M0)
        V1 = float(V0)
        P1 = float(P0)
        T1 = P1 * V1 / (M1/F1.mass * R)
        Results = T1
    if(V0 == "x"):
        F1 = Formula(F0)
        M1 = float(M0)
        T1 = float(T0) + 273.15
        P1 = float(P0)
        V1 = M1/F1.mass * R * T1 / P1
        Results = V1
    if(P0 == "x"):
        F1 = Formula(F0)
        M1 = float(M0)
        T1 = float(T0) + 273.15
        V1 = float(V0)
        P1 = M1/F1.mass * R * T1 / V1
        Results = P1
    print("Results: x = ", Results)
    RawData = input("Gas Formula, Mass, Temp(C), Volume, Pressure, x for unknown: ")