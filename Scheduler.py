import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

global DataSet
XLim = 0
DataSet = 0
fig,ax = plt.subplots(1)

Message = "Enter Course, Time of Week, Time of day\n\
    For example: \n\
    ECE5, MWR, 1500-1750\
    "
RawData = input(Message)


def ProcessTimeOfWeek(WeekDays):
    DayOnX = []
    DateToInt = []
    for WeekDay in WeekDays:
        if(WeekDay.upper() == "M"):   DateToInt = [0,1]
        elif(WeekDay.upper() == "T"): DateToInt = [1,2]
        elif(WeekDay.upper() == "W"): DateToInt = [2,3]
        elif(WeekDay.upper() == "R"): DateToInt = [3,4]
        elif(WeekDay.upper() == "F"): DateToInt = [4,5]
        DateToInt = [each + DataSet * 7 for each in DateToInt]
        DayOnX.append(DateToInt)
    return DayOnX

def ProcessTimeOfDay(Times):
    TimeOnY = [] #Starting Axis, Length
    Time = Times.split("-")
    Time = list(map(int, Time))
    TempTimes = Time[1]
    if(Time[0] > Time[1]):
        Time[1] = Time[0]
        Time[0] = TempTimes
    TimeOnY = [Time[0], Time[1]-Time[0]]
    return TimeOnY

def DrawData(CourseName, WeekDays, Times):
    global XLim
    i = 1
    rectangles = dict()
    for DayX in WeekDays:
        Name = CourseName + " (" + str(i) + ")"
        rectangles[Name] = patches.Rectangle((DayX[0],Times[0]), 1, Times[1], linewidth = 2, edgecolor='black',facecolor = 'none' )
        i += 1
    for r in rectangles:
        ax.add_artist(rectangles[r])
        rx, ry = rectangles[r].get_xy()
        cx = rx + rectangles[r].get_width() / 2.0
        cy = ry + rectangles[r].get_height() / 2.0
        ax.annotate(r, (cx, cy), color='Black', weight='bold', fontsize=6, ha='center', va='center')

    DayLim = WeekDays[-1][-1] + 2

    if(XLim < DayLim):
        XLim = WeekDays[-1][-1] + 2

    plt.xticks(range(0,XLim))
    plt.yticks(range(600,2500,100))

    ax.set_xlim((0, XLim))
    ax.set_ylim((2100, 700))

    #plt.show()

while(True):
    if(RawData.lower() == "complete"):
        ax.grid()
        plt.show()
        break

    SplitData = RawData.split(",")

    try:
        for i in range(math.floor((len(SplitData))/3)):
            NameIndex = 3 * i
            if(SplitData[NameIndex].strip() == "s"):
                CourseName += " s"
            else:
                CourseName = SplitData[NameIndex].strip()

            WeekDays = SplitData[NameIndex + 1].strip()
            Times = SplitData[NameIndex + 2].strip()

            WeekDay = ProcessTimeOfWeek(WeekDays)
            DayTime = ProcessTimeOfDay(Times)

            DrawData(CourseName, WeekDay, DayTime)
    except:
        pass

    DataSet += 1

    RawData = input(Message)
