import re
from geojson import Point, FeatureCollection, Feature
import constants
from extractInfoFromJson import extractUsableDataFromJson
from dmsToddConverter import validateCoordinates, convertDmsToDd
extract = extractUsableDataFromJson()


class TransformJsonToGeoJson:

    def getRunwayThresholds(self, data):
        thresholdPoints = {}
        for n in range(len(data)):
            thresholdPoints[n] = data[n]['Threshold']
        return thresholdPoints
    
    def getCoordinates(self, data):
        coordinates= {}
        for n in data.keys():
            coordinates[n] =  data[n][constants.terminalStandsTableHeaderKeys['2']]
        return coordinates

    def convertRunwayThresholds(self, thresholds):
        identifiers = ['latitude', 'longitude']
        # breakpoint()
        for n in thresholds.keys():
            thresholds[n] = validateCoordinates(thresholds[n])
            thresholds[n][identifiers[0]] = convertDmsToDd(thresholds[n][identifiers[0]])
            thresholds[n][identifiers[1]] = convertDmsToDd(thresholds[n][identifiers[1]])
        return thresholds


    def createKeysArray(self, start=0, end=10, stepSize=1):
        keys = []
        for m in range(start, end, stepSize):
            keys.append(str(m))
        return keys


    def changeRunwayDataKeys(self, data):
        del data[0]
        newData = {}
        for n in range(len(data)):
            newData[n] = dict(zip(constants.runwayTableHeaderKeys.values(), data[n].values()))
        return (newData)


    def createRunwayGeoJsonPointFeatures(self, thresholds):
            features = {}
            # print(thresholds.keys())
            # breakpoint()
            for n in thresholds.keys():
                features[n] = Feature(geometry=Point(
                    (thresholds[n]['longitude'], thresholds[n]['latitude']), precision=15))
            return features


    def combineRunwayPointAndProperties(self, features, properties):
            collection = []
            for n in range(len(features)):
                del properties[n]['Threshold']
                features[n]['properties'] = properties[n]
                collection.append(features[n])
            return FeatureCollection(collection)
    
    def combineObstaclesPointAndProperties(self, features, properties):
            collection = []
            for n in features.keys():
                # breakpoint()
                m = int(n)
                del properties[m]['Coordinates']
                features[n]['properties'] = properties[m]
                collection.append(features[n])
            return FeatureCollection(collection)

    def combineTerminalStandsPointsAndProperties(self,features,properties):
        collection =[]
        for n in features.keys():
            del properties[n][constants.terminalStandsTableHeaderKeys['2']]
            features[n]['properties'] = properties[n]
            collection.append(features[n])
        return FeatureCollection(collection)

    def changeTerminalStandsDataKeys(self,data):
        del data[0]
        newData = {}
        for n in range(len(data)):
            newData[n] = dict(zip(constants.terminalStandsTableHeaderKeys.values(), data[n].values()))
        return newData
        
    def removeTerminalStandsInvalidData(self,data):
        listToDelete=[]
        for n in range(len(data)):
            if not 'E' in (data[n]['Coordinates']):
                listToDelete.append(int(n))
            if 'STAND' in (data[n]['Stand']):
                listToDelete.append(int(n))
        for n in range(len(listToDelete)):
            data.pop(listToDelete[n])
        return data

    def removeRunwayInvalidData(self,data):
        for n in range(len(data)):
            if data[n][constants.runwayTableHeaderKeys['2']] == "" or 'Direction' in  data[n][constants.runwayTableHeaderKeys['2']]:
                del data[n]
            else: 
                return data
        return data
        
    def cleanRunwayData(self, data):
            for n in range(len(data)):
                
                if data[n][constants.runwayTableHeaderKeys['0']]:
                    temp = data[n][constants.runwayTableHeaderKeys['0']]
                    data[n][constants.runwayTableHeaderKeys['0']] = extract.removeExtraData(temp)

                if data[n][constants.runwayTableHeaderKeys['1']]:
                    temp = data[n][constants.runwayTableHeaderKeys['1']]
                    data[n][constants.runwayTableHeaderKeys['1']] = extract.direction(temp)

                if data[n][constants.runwayTableHeaderKeys['2']]:
                    temp = data[n][constants.runwayTableHeaderKeys['2']]
                    temp = extract.removeExtraData(temp)
                    data[n][constants.runwayTableHeaderKeys['2']] = extract.dimensions(temp)

                if data[n][constants.runwayTableHeaderKeys['3']]:
                    temp = data[n][constants.runwayTableHeaderKeys['3']]
                    temp = extract.thresholdCoordinates(temp)
                    data[n][constants.runwayTableHeaderKeys['3']] = temp

                if data[n][constants.runwayTableHeaderKeys['4']]:
                    temp = data[n][constants.runwayTableHeaderKeys['4']]
                    temp = extract.replaceNewline(temp, " ")

                if data[n][constants.runwayTableHeaderKeys['5']]:
                    temp = data[n][constants.runwayTableHeaderKeys['5']]
                    temp = extract.removeSpanishCharacters(temp)
                    data[n][constants.runwayTableHeaderKeys['5']] = temp

                if data[n][constants.runwayTableHeaderKeys['6']]:
                    temp = data[n][constants.runwayTableHeaderKeys['6']]
                    temp = extract.removeExtraData(temp)
                    data[n][constants.runwayTableHeaderKeys['6']] = extract.dimensions(temp)

                if data[n][constants.runwayTableHeaderKeys['7']]:
                    temp = data[n][constants.runwayTableHeaderKeys['7']]
                    temp = extract.removeExtraData(temp)
                    data[n][constants.runwayTableHeaderKeys['7']] = extract.dimensions(temp)

                if data[n][constants.runwayTableHeaderKeys['8']]:
                    temp = data[n][constants.runwayTableHeaderKeys['8']]
                    temp = extract.removeSpanishCharacters(temp)
                    data[n][constants.runwayTableHeaderKeys['8']] = temp

                if data[n][constants.runwayTableHeaderKeys['9']]:
                    temp = data[n][constants.runwayTableHeaderKeys['9']]
                    temp = extract.removeExtraData(temp)
                    data[n][constants.runwayTableHeaderKeys['9']] = temp

                if data[n][constants.runwayTableHeaderKeys['10']]:
                    temp = data[n][constants.runwayTableHeaderKeys['10']]
                    temp = extract.replaceNewline(temp, " ")
                    temp = extract.removeExtraData(temp)
                    data[n][constants.runwayTableHeaderKeys['10']] = temp
            
            return data


    def cleanTerminalStandsData(self,data):
        for n in data.keys():
            if data[n][constants.terminalStandsTableHeaderKeys['6']]:
                temp = data[n][constants.terminalStandsTableHeaderKeys['6']]
                temp = extract.replaceNewline(temp," ")
                data[n][constants.terminalStandsTableHeaderKeys['6']] = temp

            if data[n][constants.terminalStandsTableHeaderKeys['3']]:
                temp = data[n][constants.terminalStandsTableHeaderKeys['3']]
                temp = extract.removeExtraData(temp)
                data[n][constants.terminalStandsTableHeaderKeys['3']] =temp

            if data[n][constants.terminalStandsTableHeaderKeys['2']]:
                temp = data[n][constants.terminalStandsTableHeaderKeys['2']]
                temp = extract.removeUniCode(temp)
                temp = extract.replaceQuotes(temp,"")
                temp = extract.thresholdCoordinates(temp)
                data[n][constants.terminalStandsTableHeaderKeys['2']] = temp
        return data