from molmass import Formula
RawData = input("A1+B2 => C3+D4, yield of which, mass of 1 2, A B C D, Coefficients: ")
while(RawData != "quit"):
    SplitData = RawData.split(" ")
    R1 = Formula(SplitData[0])
    R2 = Formula(SplitData[1])
    P1 = Formula(SplitData[2])
    P2 = Formula(SplitData[3])
    PYield = Formula(SplitData[4])
    M = [float(SplitData[5]), float(SplitData[6])]
    C = [int(SplitData[7]),int(SplitData[8]),int(SplitData[9]),int(SplitData[10])]
    Mr = [R1.mass,R2.mass,P1.mass,P2.mass]
    Mol = [M[0]/Mr[0], M[1]/Mr[1]]
    UnitMol0 = Mol[0]/C[0]
    UnitMol1 = Mol[1]/C[1]
    Coefficient = 0
    if(UnitMol0 > UnitMol1):
        print(R2.formula," Limiting")
        LimitingM = M[1]
        Limiting = R2
        LimitingC = C[1]
    elif(UnitMol0 < UnitMol1):
        print(R1.formula," Limiting")
        LimitingM = M[0]
        Limiting = R1
        LimitingC = C[0]
    else:
        print("Not Limiting")
        Limiting = R2
        LimitingC = C[1]
    if(PYield.formula == P1.formula):
        Coefficient = C[2]
    if(PYield.formula == P2.formula):
        Coefficient = C[3]
    YieldMol = LimitingM/Limiting.mass / LimitingC * Coefficient
    YieldMass = YieldMol * PYield.mass
    print("Mol of yield: ", YieldMol)
    print("Mass of yield: ", YieldMass)
    if(PYield != P1 and PYield != P2):
        RawData = input("A1+B2 => C3+D4, yield of which, mass of 1 2, A B C D, Coefficients: ")
        continue
    

    RawData = input("A1+B2 => C3+D4, yield of which, mass of 1 2, A B C D, Coefficients: ")