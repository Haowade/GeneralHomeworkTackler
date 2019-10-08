from molmass import Formula
RawData = input("1st gas Formula, mass, 2nd Formula, mass, T, V: ")
while(RawData != "quit"):
    SplitData = RawData.split(" ")
    if(len(SplitData) == 1):
        F1 = Formula(SplitData[0])
        print(F1.mass)
    elif(len(SplitData) == 2):
        F1 = Formula(SplitData[0])
        M1 = float(SplitData[1])
        mol = M1/F1.mass
        print("Mol: ", mol)
    elif(len(SplitData) == 4):
        F1 = Formula(SplitData[0])
        M1 = float(SplitData[1])
        F2 = Formula(SplitData[2])
        M2 = float(SplitData[3])
        mol1 = M1/F1.mass
        mol2 = M2/F2.mass
        molT = mol1 + mol2
        print(F1.formula, F2.formula, "total: ",molT)
        print(F1.formula, "ratio: ",mol1/molT," mol 1: ",mol1)
        print(F2.formula, "ratio: ",mol2/molT," mol 2: ",mol2)
    elif(len(SplitData) == 6):
        F1 = Formula(SplitData[0])
        M1 = float(SplitData[1])
        F2 = Formula(SplitData[2])
        M2 = float(SplitData[3])
        T1 = float(SplitData[4]) + 273.15
        V1 = float(SplitData[5])
        mol1 = M1/F1.mass
        mol2 = M2/F2.mass
        molT = mol1 + mol2
        P = molT * 0.0820574 * T1 / (V1)
        print(F1.formula, F2.formula, "total: ",molT,"\n")
        
        print(F1.formula, "ratio: ",mol1/molT," mol 1: ",mol1)
        print(F1.formula, "P1 ratio: ",mol1/molT * P)
        print(F2.formula, "ratio: ",mol2/molT," mol 2: ",mol2)
        print(F2.formula, "P2 ratio: ",mol2/molT * P)
        print("Total Pressure: ", P)
    RawData = input("1st gas Formula, mass, 2nd Formula, mass: ")