#%% All imports
import constants
import math
import dmsToddConverter as dmsToDd

#%% 
RWY_03_THR_LAT = dmsToDd.convertDmsToDd(constants.RWY_03_THRESHOLD_POINT[0])
RWY_03_THR_LONG = dmsToDd.convertDmsToDd(constants.RWY_03_THRESHOLD_POINT[1])
RWY_21_THR_LAT = dmsToDd.convertDmsToDd(constants.RWY_21_THRESHOLD_POINT[0])
RWY_21_THR_LONG = dmsToDd.convertDmsToDd(constants.RWY_21_THRESHOLD_POINT[1])
RWY_02_THR_LAT = dmsToDd.convertDmsToDd(constants.RWY_02_THRESHOLD_POINT[1])
RWY_02_THR_LONG = dmsToDd.convertDmsToDd(constants.RWY_02_THRESHOLD_POINT[0])

# print(RWY_03_THR_LAT, RWY_03_THR_LONG)
# print(RWY_02_THR_LAT, RWY_02_THR_LONG)
#%%
def findLongitudeLatitude2(lat1, long1, distance, bearingPoint1):
    angularDistance = distance/constants.R
    # print(angularDistance)
    lat = math.radians(lat1)
    long = math.radians(long1)
    bearingPoint = math.radians(bearingPoint1)
    latitude2 = math.asin(math.sin(lat) * math.cos(angularDistance) + math.cos(lat) * math.sin(angularDistance)* math.cos(bearingPoint))
    longitude2 = long + math.atan2(math.sin(bearingPoint) * math.sin(angularDistance) * math.cos((lat)), math.cos(angularDistance) - math.sin((lat)) * math.sin((latitude2)))
    # print(latitude2, longitude2)
    return [math.degrees(latitude2),math.degrees(longitude2)]
# %%

[lat2,long2] = findLongitudeLatitude2(RWY_03_THR_LAT, RWY_03_THR_LONG, constants.RWY_03_DIM[0], constants.RWY_03_BEARING_POINT)

print(long2,lat2)