#%% All imports
import math
from numpy import arcsin
import dmsToddConverter as ddtodms
#%% Runway Dimensions and Co-Ordinate Constants
RWY_03_DIM =[2188,48] # units in meters
RWY_03_THRESHOLD_POINT = ["43173011N","008230874W"]
RWY_03_BEARING_POINT = 30.94 #Geographic North in degrees.
#%% Constants
#radius of Earth in KMS 
R = 632781370 *1000 #multiplying by 1000 for meters.