import os
import json


class extractUsableDataFromJson:

    def removeSpanishCharacters(self, data):
        if 'Yes' in data:
            return 'Yes'
        else:
            return data

    def removeExtraData(self, data):
        if '(' in data:
            newData = self.replaceNewline(data, "")
            newData = newData.split('(')[0]
            return newData
        else:
            return data

    def replaceNewline(self, data, replaceWith):
        if '\n' in data:
            newData = data.replace('\n', replaceWith)
            return newData
        else:
            return data

    def dimensions(self, data):
        if 'x' in data:
            newData = data.split('x')
            return ({
                'length': str(newData[0]),
                'width': str(newData[1])
            })

    def removeUniCode(self, data):
        encoded = data.encode("ascii", "ignore")
        return encoded.decode()

    def direction(self, directionData):
        data = self.replaceNewline(directionData, " ")
        data = self.removeUniCode(data)
        splitData = data.split("GEO")
        return{
            "Geographic": str(splitData[0]),
            "Magnetic": str(splitData[1].split("MAG")[0])
        }

    def thresholdCoordinates(self, threshold):
        data = self.replaceNewline(threshold, "")
        if "N" in data:
            data = data.split('N')
            coordinates = {
                "latitude": str(data[0]+'N'),
                "longitude": str(data[1])
            }
            return coordinates
        if "S" in data:
            data = data.split('S')
            coordinates = {
                "latitude": str(data[0]+'S'),
                "longitude": str(data[1])
            }
            return coordinates

    def replaceQuotes(self, text, replaceWith=''):
        if '\'' in text:
            text = self.removeUniCode(text)
            text = text.replace('\'', replaceWith)

        if '\"' in text:
            text = text.replace('\"', replaceWith)

        return text

    def loadJson(self, fileNameWithExtension):
        currentDirectory = os.path.abspath(__file__)
        basePath = currentDirectory.split('src')[0]
        filePath = basePath+'data/json/'+fileNameWithExtension
        with open(filePath) as f:
            jsonData = json.load(f)
        return jsonData
