import dmsToddConverter as dmstoDd
import constants
import geoJsonPointsClass
import coordinatesFromThreshold as cft
from coordinatesFromThreshold import findLongitudeLatitude2
from geojson import Point, LineString
coruna_thr_lat = dmstoDd.convertDmsToDd(constants.RWY_03_THRESHOLD_POINT[0])
coruna_thr_long = dmstoDd.convertDmsToDd(constants.RWY_03_THRESHOLD_POINT[1])
[lat2, long2] = findLongitudeLatitude2(
    coruna_thr_lat, coruna_thr_long, constants.RWY_03_DIM[0], constants.RWY_03_BEARING_POINT)

print(LineString(
    [(coruna_thr_long, coruna_thr_lat), (long2, lat2)], precision=15))
# print(Point((coruna_thr_lat, coruna_thr_long),precision = 15))
# print(lat2,long2)
