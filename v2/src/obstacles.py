
from hamcrest import none
import fileSystem
import transformJsonDataToGeoJson

td = transformJsonDataToGeoJson.TransformJsonToGeoJson()
fs = fileSystem.LoadFiles()

name = "LE_Amdt_A_2020_03_AD_2_10_LECO_en_obstacles"

airportName = "coruna"

obstacles = fs.readJson(airportName, name)


class TransformObstaclesData:

    def getKeysAndValues(self, obstacles):
        keys = list(obstacles.keys())
        values = list(obstacles.values())
        return keys, values

    def getEnglishKeys(self, originalKeys):
        englishKeys = []
        for n in range(len(originalKeys)):
            if '_' in originalKeys[n]:
                englishKeys.append(originalKeys[n].split('_')[1])
            else:
                englishKeys.append(originalKeys[n])
        return englishKeys

    def mergeNewKeys(self, newKeys, obstaclesValues):
        newObstaclesData = {}
        for n in range(len(obstaclesValues)):
            newObstaclesData[newKeys[n]] = obstaclesValues[n]
        return newObstaclesData

    def convertCoordinates(self, latitudes, longitudes):
        coordinates = {}
        allCoordinates = {}
        listLength = (len(latitudes))
        if (len(latitudes) == len(longitudes)):
            for n in range(listLength):
                coordinates[n] = {'latitude': latitudes[n],
                                  'longitude': longitudes[n]}
                allCoordinates[str(n)] = coordinates[n]
        else:
            print('Mismatched Array Lengths :', 'lat:', len(
                latitudes), ',', 'long:', len(longitudes))
        return allCoordinates

    def addNewCoordinatesToObstacles(self, obstacles, coordinates):
        obstacles['Coordinates'] = coordinates
        del obstacles['Longitude']
        del obstacles['Latitude']
        return obstacles

    def convertCoordinatesToDms(self, coordinates):
        convertedCoordinates = []
        convertedCoordinates.append(td.convertRunwayThresholds(coordinates))
        return convertedCoordinates

    def mergeObstacleData(self, obstacles):
        allObstacles = []
        categories = list(obstacles.keys())
        length = len(list(obstacles['Type'].values()))
        for m in range(length):
            mergedObstacles = {}
            for n in categories:
                mergedObstacles[n] = obstacles[n][str(m)]
            allObstacles.append(mergedObstacles)
        return allObstacles


data = TransformObstaclesData()
obstacleKeys, obstacleValues = data.getKeysAndValues(obstacles)
keys = data.getEnglishKeys(obstacleKeys)
newObstacles = data.mergeNewKeys(keys, obstacleValues)
newCoordinates = data.convertCoordinates(list(
    newObstacles['Latitude'].values()), list(newObstacles['Longitude'].values()))
newObstacles = data.addNewCoordinatesToObstacles(newObstacles, newCoordinates)
dmsCoordinates = td.convertRunwayThresholds((newObstacles['Coordinates']))
obstaclesPointFeatures = td.createRunwayGeoJsonPointFeatures(dmsCoordinates)
mergedObstacles = data.mergeObstacleData(newObstacles)
obstaclesCollection = td.combineObstaclesPointAndProperties(obstaclesPointFeatures,mergedObstacles)
print(obstaclesCollection)
