
import fileSystem
import transformDataCommon
from geojson import Point, FeatureCollection, Feature
tdc = transformDataCommon.TransformDataCommon()
fs = fileSystem.LoadFiles()


class TransformObstaclesData:

    def combineObstaclesPointAndProperties(self, features, properties):
        collection = []
        for n in features.keys():
            m = int(n)
            del properties[m]['Coordinates']
            features[n]['properties'] = properties[m]
            collection.append(features[n])
        return FeatureCollection(collection)

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

    def combineCoordinates(self, latitudes, longitudes):
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
        convertedCoordinates.append(tdc.convertCoordinatesToDMS(coordinates))
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
