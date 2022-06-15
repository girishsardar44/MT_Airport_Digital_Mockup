import re

x = 9.942778

def convertDdToDms(b):
    deg = int(b)
    min = int(b - deg * 60)
    sec = round ((b - deg - min/60) * 3600, 6)

    # if (min > 60 or min < -60):
    #     addToDegrees = int(min/60)
    #     # print(addToDegrees)
    #     min = int(round(addToDegrees - min/60, 2)*100)
    print([deg, min, sec])


convertDdToDms(x)