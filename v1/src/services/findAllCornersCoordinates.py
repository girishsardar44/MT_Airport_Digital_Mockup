import writeToGeojson as wtg
import constants
import coordinatesFromThreshold as cft
import perpendicularBearingAnglesCalculator as perpendicularAngles
def findCornersFromThreshold(originalBearingPoint,dim ,latitude,longitude):
    [positiveAngle, negativeAngle]= perpendicularAngles.calculatePerpendicularBearingAngle(originalBearingPoint)
    totalWidth = dim[1]/2
    adjacentPositiveCorner = cft.findLongitudeLatitude2(latitude,longitude,totalWidth, positiveAngle)
    adjacentNegativeCorner = cft.findLongitudeLatitude2(latitude,longitude,totalWidth, negativeAngle)
    farPositiveCorner = cft.findLongitudeLatitude2(adjacentPositiveCorner[0], adjacentPositiveCorner[1],constants.RWY_03_DIM[0] ,originalBearingPoint)
    farNegativeCorner = cft.findLongitudeLatitude2(adjacentNegativeCorner[0], adjacentNegativeCorner[1],constants.RWY_03_DIM[0] ,originalBearingPoint)
    print([adjacentPositiveCorner,farPositiveCorner, farNegativeCorner, adjacentNegativeCorner])
    return ([adjacentPositiveCorner,farPositiveCorner, farNegativeCorner, adjacentNegativeCorner])

#assign returns in a,d,b,c format
k = findCornersFromThreshold(constants.RWY_03_BEARING_POINT, constants.RWY_03_DIM, cft.RWY_03_THR_LAT, cft.RWY_03_THR_LONG)
l = findCornersFromThreshold(constants.RWY_21_BEARING_POINT, constants.RWY_21_DIM, cft.RWY_21_THR_LAT, cft.RWY_21_THR_LONG)
b = findCornersFromThreshold(constants.RWY_02_BEARING_POINT, constants.RWY_02_DIM, cft.RWY_02_THR_LAT, cft.RWY_02_THR_LONG)
print (k)
wtg.runwaygeojson(k)
