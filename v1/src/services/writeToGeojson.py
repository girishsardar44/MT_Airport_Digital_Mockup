
import geojsonClasses as gjc
import json
def runwaygeojson(x):
    points_list= []
    for num in x: 
        points_list.append(gjc.Feature(type="Feature", properties={},geometry=(gjc.geometries(type="Point",coordinates=num))))
    featureCollection = gjc.featureCollection(points_list)
    jsondata = json.dumps(featureCollection, sort_keys=False, indent=2, cls=gjc.dataEncoder)
    print (jsondata)