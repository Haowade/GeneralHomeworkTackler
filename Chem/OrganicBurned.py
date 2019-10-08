from molmass import Formula
RawData = input("Original Mass, Mr, CO2 Mass, H2O Mass: ")
while(RawData != "quit"):
    SplitData = RawData.split(" ")
    MOrigin = float(SplitData[0])
    Mr = float(SplitData[1])
    MCO2 = float(SplitData[2])
    MWater = float(SplitData[3])

    Cmol = MCO2 / Formula("CO2").mass
    Hmol = 2 * MWater / Formula("H2O").mass
    OMass = MOrigin - Cmol * Formula("C").mass - Hmol * Formula("H").mass
    Omol = OMass/Formula("O").mass
    HtoCRatio = Hmol / Cmol
    OtoCRatio = Omol / Cmol
    EmpiricalMr = HtoCRatio * Formula("H").mass + Formula("C").mass + OtoCRatio * Formula("O").mass
    Coefficient = round(Mr/EmpiricalMr,0)
    print("C","H", int(round(HtoCRatio,0)), "O",int(round(OtoCRatio,0) ))
    print("C",int(Coefficient),"H", int(round(Coefficient*HtoCRatio,0)), "O",int(Coefficient*round(OtoCRatio,0)))


    RawData = input("1st gas Formula, mass, 2nd Formula, mass: ")