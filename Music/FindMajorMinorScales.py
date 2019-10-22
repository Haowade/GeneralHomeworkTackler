Message = "What Major/Minor (Capital/Lower case):"
UserInput = input(Message)
Keys = ["BCD","CD","D","DE","DEF","EFG","FG","G","GA","A","AB","ABC"]
CMajorKeys = ["C","D","E","F","G","A","B"]


def DetermineKeys(Key = "C", Accidental = ""):
    KeyOrder = ["C","CD","D","DE","D","E","F","G","GA","A","AB","B"]
    KeyNumber = KeyOrder.index(Key)
    if(Accidental == "#"):
        KeyNumber += 1
    elif(Accidental == "b"):
        KeyNumber -= 1
    else:
        Accidental = ""

    RawArray = \
        [Key + Accidental, Keys[(2 + KeyNumber)%len(Keys)], Keys[(4 + KeyNumber)%len(Keys)], \
        Keys[(5 + KeyNumber)%len(Keys)], Keys[(7 + KeyNumber)%len(Keys)], Keys[(9 + KeyNumber)%len(Keys)], \
        Keys[(11 + KeyNumber)%len(Keys)], Keys[(12 + KeyNumber)%len(Keys)]]


    for i in range(len(RawArray)):
        if(i==0): continue
        if(len(RawArray[i]) == 2):
            if(RawArray[i][0] == RawArray[i - 1][0]):
                RawArray[i] = RawArray[i][1] + "b"
            else:
                RawArray[i] = RawArray[i][0] + "#"
        if(len(RawArray[i]) == 3 and len(RawArray[i - 1]) == 2):
            if(RawArray[i - 1][1] == "#"):
                RawArray[i] = RawArray[i][0] + "#"
            if(RawArray[i - 1][1] == "b"):
                RawArray[i] = RawArray[i][2] + "b"
        if(len(RawArray[i]) == 3 and len(RawArray[i - 1]) == 1):
            RawArray[i] = RawArray[i][1]

    MajorKeys = {
        "Tonic" : RawArray[0],
        "Supertonic" : RawArray[1],
        "Mediant" : RawArray[2],
        "Subdominant" : RawArray[3],
        "Dominant" : RawArray[4],
        "Submediant" : RawArray[5],
        "LeadingTone" : RawArray[6],
        "TonicOCT" : RawArray[7]
    }
    return MajorKeys



while UserInput != "quit":
    if(UserInput[0] in CMajorKeys):
        try:
            print(DetermineKeys(UserInput[0], UserInput[1]))
        except:
            print(DetermineKeys(UserInput[0]))
        pass
    elif(UserInput[0].upper() in CMajorKeys):
        pass
    else:
        UserInput = input(Message)
        continue
    UserInput = input(Message)