#%% Runway Dimensions and Co-Ordinate Constants
RWY_03_DIM = [2.188,0.045] # units in Kilometers
RWY_03_THRESHOLD_POINT = ["431730.11N","082308.74W"] #lat, long 
RWY_03_BEARING_POINT = 30.94 #Geographic North in degrees.

#%%
#radius of Earth in KMS 
R = 6378.1 
#%% CORUNA RUNWAY 21
RWY_21_DIM = [2.188, 0.045]
RWY_21_THRESHOLD_POINT = ["431830.91N","082218.84W"]
RWY_21_BEARING_POINT = 210.95


#%% BARCELONA RUNWAY 02 
RWY_02_DIM = [2.528, 0.045]
RWY_02_BEARING_POINT = 18.98
RWY_02_THRESHOLD_POINT = ["411715.93N", "020505.41E"]

#%%
tableHeaderKeys = {
    "0":"RWY",
    "1":"Direction",
    "2":"Dimensions",
    "3":"Threshold",
    "4":"Threshold & Touchdown Elevation",
    "5":"StopWay",
    "6":"ClearWay",
    "7":"Strip",
    "8":"OFZ",
    "9":"RESA",
    "10":"RWY/SWY SFC PCN"
}
direction = {
    "Geographic":"",
    "Magnetic":""
}

dimensions = {
    "length":"",
    "width":""
}
