from extractInfoFromJson import extractUsableDataFromJson
from transformJsonDataToGeoJson import TransformJsonToGeoJson

convert = TransformJsonToGeoJson()

def convertRunwaysToGeoJson(data):
    jsonData = convert.changeRunwayDataKeys(data)
    validJsonData = convert.removeRunwayInvalidData(jsonData)
    cleanJson = convert.cleanRunwayData(validJsonData)
    thresholds = convert.getRunwayThresholds(cleanJson)
    thresholds = convert.convertRunwayThresholds(thresholds)
    features = convert.createRunwayGeoJsonPointFeatures(thresholds)
    geojson = convert.combineRunwayPointAndProperties(features, cleanJson)
    return geojson

def convertTerminalStandsJsonToGeojson(data):
    jsonData = convert.changeTerminalStandsDataKeys(data)
    validJsonData = convert.removeTerminalStandsInvalidData(jsonData)
    cleanJson = convert.cleanTerminalStandsData(validJsonData)
    coordinates = convert.getCoordinates(cleanJson)
    coordinates = convert.convertRunwayThresholds(coordinates)
    features = convert.createRunwayGeoJsonPointFeatures(coordinates)
    geojson = convert.combineTerminalStandsPointsAndProperties(features,cleanJson)
    return geojson

