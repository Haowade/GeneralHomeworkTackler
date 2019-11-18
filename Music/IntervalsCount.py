Message = "1:HalfSteps between keys (C#, D), 2 Count steps (C#, m2, +):"
UserInput = input(Message)
MajorAndMinorNames = {
    0:"Unison",
    1:"m2",
    2:"M2",
    3:"m3",
    4:"M3",
    5:"P4",
    6:"A4/d5",
    7:"P5",
    8:"m6",
    9:"M6",
    10:"m7",
    11:"M7",
    12:"Octave",
}
StepsNumber = {
    "Unison":0,
    "m2":1,
    "M2":2,
    "m3":3,
    "M3":4,
    "P4":5,
    "A4/d5":6,
    "P5":7,
    "m6":8,
    "M6":9,
    "m7":10,
    "M7":11,
    "Octave":12,
}
KeysDiatonic = ["C","D","E","F","G","A","B"]


def DetermineKeyStep(Key = "C", Accidental = "", Key1 = "C", Accidental1 = ""):
    KeyOrder = ["C","CD","D","DE","E","F","FG","G","GA","A","AB","B"]
    KeyNumber = KeyOrder.index(Key)
    KeyNumber1 = KeyOrder.index(Key1)
    if(Accidental == "#"):
        KeyNumber += 1
    elif(Accidental == "b"):
        KeyNumber -= 1
    else:
        Accidental = ""

    if(Accidental1 == "#"):
        KeyNumber1 += 1
    elif(Accidental1 == "b"):
        KeyNumber1 -= 1
    else:
        Accidental1 = ""

    steps = (12+KeyNumber1 - KeyNumber) % 12
    Name = MajorAndMinorNames[steps]
    Distance = (8 + KeysDiatonic.index(Key1) - KeysDiatonic.index(Key)) % 7

    if(Name == "A4/d5"):
        if(Distance == 4):
            Name += " A4"
        if(Distance == 5):
            Name += " d5"
    else:
        if(Distance > int(Name[1])):
            Name = "d" + str(Distance)
        elif(Distance < int(Name[1])):
            Name = "A" + str(Distance)

    return str(steps)+ " " +  Name

def DetermineKeys(Key = "C", Accidental = "", Interval = "m1", Up = "+"):
    KeyOrder = ["C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B"]
    IOriginal = Interval
    if(Interval[:2] == "A4" or Interval[:2] == "d5"):
        Interval = "A4/d5"
    elif(Interval[0] == "d"):
        Interval = "M" + str(int(Interval[1:])-1)
    elif(Interval[0] == "A"):
        if(Interval[1] == "8"):
            Interval = "m2"
        else:
            Interval = "m" + str(int(Interval[1:])+1)

    KeyNumber = KeyOrder.index(Key)
    ReturnKey = ""
    if(Accidental == "#"):
        KeyNumber += 1
    elif(Accidental == "b"):
        KeyNumber -= 1
    else:
        Accidental = ""

    if(Up == "+"):
        KeyReturn = KeyNumber + StepsNumber[Interval.strip()]
        ReturnKey = KeyOrder[(12+KeyReturn)%12]
        if(len(ReturnKey)>3):
            if(Interval[0] == "M"):
                ReturnKey = "A" + str(int(Interval[1])-1) + " " + ReturnKey
            elif(Interval[0] == "m"):
                ReturnKey = ReturnKey + " d" + str(int(Interval[1]) + 1)
            else:
                if(IOriginal[0] == "d"):
                    ReturnKey = IOriginal + " " + ReturnKey
                else:
                    ReturnKey = ReturnKey + " " + IOriginal
    else:
        KeyReturn = KeyNumber - StepsNumber[Interval.strip()]
        ReturnKey = KeyOrder[(12+KeyReturn)%12]
        if(len(ReturnKey)>3):
            if(Interval[0] == "M"):
                ReturnKey = "d" + str(int(Interval[1])+1) + " " + ReturnKey
            elif(Interval[0] == "m"):
                ReturnKey = ReturnKey + " A" + str(int(Interval[1]) - 1)
            else:
                if(IOriginal[0] == "d"):
                    ReturnKey = IOriginal + " " + ReturnKey
                else:
                    ReturnKey = ReturnKey + " " + IOriginal


    return ReturnKey

while UserInput != "quit":
    try:
        Inputs = [text.strip() for text in UserInput.split(",")]
    except:
        print("Something Went wrong when splitting")
        UserInput = input(Message)
        continue
    if(Inputs[0] == "1"):
        try:
            Inputs = [text.strip() for text in UserInput.split(",")]
            Inputs[1] += " "
            Inputs[2] += " "
            print(DetermineKeyStep(Inputs[1][0],Inputs[1][1],Inputs[2][0],Inputs[2][1]), end = "|| if inverse: ||")
            print(DetermineKeyStep(Inputs[2][0],Inputs[2][1],Inputs[1][0],Inputs[1][1]))
        except:
            print("Something Went wrong")
    else:
        try:
            Inputs = [text.strip() for text in UserInput.split(",")]
            Inputs[1] += " "
            Inputs[2] += " "
            print(DetermineKeys(Inputs[1][0],Inputs[1][1],Inputs[2],Inputs[3]))
        except:
            print("Something Went wrong")
    UserInput = input(Message)