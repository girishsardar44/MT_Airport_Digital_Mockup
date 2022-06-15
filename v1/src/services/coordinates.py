from dis import dis
import constants
import math
import dmsToddConverter as dmsToDd

def getcoordinates(lat, long, bearing, distance):
    print(distance)
    rlat = math.radians(lat)
    rlong = math.radians(long)
    rbearing = math.radians(bearing)
    angularDist = distance/constants.R
    lat2 = math.asin(math.sin(rlat)* math.cos(angularDist) + math.cos(rlat) * math.sin(angularDist) * math.cos(rbearing))
    long2 = rlong + math.atan2(math.sin(rbearing) * math.sin(angularDist) * math.cos(rlat), math.cos(angularDist) - math.sin(rlat) * math.sin(lat2))
    return [math.degrees(lat2), math.degrees(long2)]


[RWY_03_THR_LAT] = dmsToDd.convertDmsToDd(constants.RWY_03_THRESHOLD_POINT[0])
[RWY_03_THR_LONG] = dmsToDd.convertDmsToDd(constants.RWY_03_THRESHOLD_POINT[1])


[lat, long] = getcoordinates(RWY_03_THR_LAT, RWY_03_THR_LONG, constants.RWY_03_BEARING_POINT, constants.RWY_03_DIM[0])
print('Calculated Point >>> ',long,lat)
print('Threshold >>> ', RWY_03_THR_LAT, RWY_03_THR_LONG)