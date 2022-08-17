import os
import json
import pandas as pd


class LoadFiles:

    def getBasePath(self):
        currentDirectory = os.path.abspath(__file__)
        basePath = currentDirectory.split('src')[0]
        return basePath

    def listFiles(self, path):
        ls = os.listdir(path)
        return ls

    def listInputFiles(self, airportName):
        basePath = self.getBasePath()
        inputFilesPath = basePath+'data/'+airportName+'/inputData/'
        inputFilesList = self.listFiles(inputFilesPath)
        return inputFilesList

    def findAllInputFiles(self, listOfFiles):
        files = {
            'runways': '',
            'obstacles': '',
            'terminalStands': ''
        }
        for file in listOfFiles:
            if file.endswith('runways.pdf'):
                files['runways'] = file
            if file.endswith('terminalStands.pdf'):
                files['terminalStands'] = file
            if file.endswith('obstacles.csv'):
                files['obstacles'] = file
        return files

    def readJson(self, airportName, fileName):
        basePath = self.getBasePath()
        filePath = basePath+'data/'+airportName+'/json/'+fileName+'.json'
        with open(filePath) as f:
            jsonData = json.load(f)
        return jsonData

    def writeJson(self, airport, fileName, content):
        basePath = self.getBasePath()
        with open(basePath+'data/'+airport+'/json/'+fileName+'.json', 'w') as output:
            output.write(content)

    def createDirectoryIfNotExists(self, path):
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path, exist_ok='false')
            print('New directory created at \n', path)
        else:
            print('Directory Already exists')

    def csvToJson(self, airportName, csvName):
        basePath = self.getBasePath()
        csvPath = basePath+'data/'+airportName+'/inputData/'+csvName+'.csv'
        jsonPath = basePath+'data/'+airportName+'/json/'+csvName+'.json'
        obstaclesDataFrame = pd.read_csv(csvPath,sep=';')
        obstaclesDataFrame.to_json(jsonPath)

    def removeFileExtension(self, file, extension):
        return (file.split(extension)[0])
