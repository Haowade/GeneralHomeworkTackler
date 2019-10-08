Alls = input("How many above or below what:")
while Alls != "quit":
    All = Alls.split(" ")
    A = int(All[0])
    B = All[1]
    C = All[2].upper()
    Notes = {
        "A":0,
        "B":1,
        "C":2,
        "D":3,
        "E":4,
        "F":5,
        "G":6,
    }
    if(B.lower() == "above"): P = 1
    else: P = -1
    found = (Notes.get(C) + P*(A-1) + 7)%7
    print(found)
    Notes1 = {
        0:"A",
        1:"B",
        2:"C",
        3:"D",
        4:"E",
        5:"F",
        6:"G",
    }
    print(Notes1.get(found))
    Alls = input("How many above or below what:")
    
