from extractInfoFromJson import extractUsableDataFromJson
from transformDataCommon import TransformDataCommon
from transformObstaclesData import TransformObstaclesData
from transformRunwayData import TransformRunwayData
from transformTerminalData import TransformTerminalData

tod = TransformObstaclesData()
trd = TransformRunwayData()
ttd = TransformTerminalData()
tdc = TransformDataCommon()

def convertRunwaysToGeoJson(data):
    jsonData = trd.changeRunwayDataKeys(data)
    validJsonData = trd.removeRunwayInvalidData(jsonData)
    cleanJson = trd.cleanRunwayData(validJsonData)
    thresholds = trd.getRunwayThresholds(cleanJson)
    thresholds = tdc.convertCoordinatesToDMS(thresholds)
    features = tdc.createGeoJsonPointFeatures(thresholds)
    geojson = trd.combineRunwayPointAndProperties(features, cleanJson)
    return geojson

def convertTerminalStandsJsonToGeojson(data):
    jsonData = ttd.changeTerminalStandsDataKeys(data)
    validJsonData = ttd.removeTerminalStandsInvalidData(jsonData)
    cleanJson = ttd.cleanTerminalStandsData(validJsonData)
    coordinates = ttd.getCoordinates(cleanJson)
    coordinates = tdc.convertCoordinatesToDMS(coordinates)
    features = tdc.createGeoJsonPointFeatures(coordinates)
    geojson = ttd.combineTerminalStandsPointsAndProperties(features,cleanJson)
    return geojson

def convertObstaclesJsonToGeoJson(data):
    keys, values = tod.getKeysAndValues(data)
    englishKeys = tod.getEnglishKeys(keys)
    obstaclesWithNewKeys = tod.mergeNewKeys(englishKeys,values)
    combinedCoordinates = tod.combineCoordinates(list(obstaclesWithNewKeys['Latitude'].values()), list(obstaclesWithNewKeys['Longitude'].values()))
    obstaclesWithCombinedCoordinates = tod.addNewCoordinatesToObstacles(obstaclesWithNewKeys, combinedCoordinates)
    dmsCoordinates = tdc.convertCoordinatesToDMS(obstaclesWithCombinedCoordinates['Coordinates'])
    obstaclesPointFeatures = tdc.createGeoJsonPointFeatures(dmsCoordinates)
    mergedObstacles = tod.mergeObstacleData(obstaclesWithCombinedCoordinates)
    obstaclesGeoJson = tod.combineObstaclesPointAndProperties(obstaclesPointFeatures,mergedObstacles)
    return obstaclesGeoJson