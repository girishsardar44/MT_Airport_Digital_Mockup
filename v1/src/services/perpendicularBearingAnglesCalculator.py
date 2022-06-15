
# angle = 30.94

def calculatePerpendicularBearingAngle(angle1):
    left = angle1 - 90
    right = angle1 + 90
    print(right, left)
    if (left < 0):
        left = 360 + left
    if (right > 360):
        right = right - 360
    print(right,left)
    return [right,left]

# calculatePerpendicularBearingAngle(angle)