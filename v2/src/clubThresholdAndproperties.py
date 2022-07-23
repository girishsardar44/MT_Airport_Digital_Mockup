from geojson import Point, FeatureCollection, Feature

def createGeoJsonPointFeatures(thresholds):
    features={}
    for n in range(len(thresholds)):
        features[n] = Feature(geometry = Point((thresholds[n]['longitude'],thresholds[n]['latitude']),precision=15))
    return features

def combinePointAndProperties(features,properties):
    collection = []
    for n in range(len(features)):
        del properties[n]['Threshold']
        features[n]['properties'] = properties[n]
        collection.append(FeatureCollection([features[n]])) 
    return collection
