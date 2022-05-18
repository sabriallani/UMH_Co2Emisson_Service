from flask import Flask
from flask import request, jsonify
import requests
from requests.structures import CaseInsensitiveDict
app = Flask(__name__)

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer WB253X2YR3MBJ4JAHA2T9DP90CE8"
headers["Content-Type"] = "application/x-www-form-urlencoded"
url = "https://beta3.api.climatiq.io/estimate"
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/Co2Emission')
def getEmission():

 data = """
 {
         "emission_factor": "commercial_vehicle-vehicle_type_hgv-fuel_source_diesel-engine_size_na-vehicle_age_post_2015-vehicle_weight_gt_15t_lt_20t",
         "parameters":
             {
               "distance": 100,
               "distance_unit": "km"
             }
         }
 """
 resp = requests.post(url, headers=headers, data=data)
 return resp.json()


@app.route('/fuel_consumption')
def getfuel():
 data = """
 {
       "emission_factor": "heat-and-steam-type_purchased",
       "parameters": {
         "energy": 100,
         "energy_unit": "kWh"
       }
   }
 """
 resp = requests.post(url, headers=headers, data=data)
 return resp.json()


@app.route('/vehicleEmission')
def getvehicle_travelling_over_a_distance():

 data = """
 {
         "emission_factor": "commercial_vehicle-vehicle_type_hgv-fuel_source_diesel-engine_size_na-vehicle_age_post_2015-vehicle_weight_gt_15t_lt_20t",
         "parameters":
             {
               "distance": 100,
               "distance_unit": "km"
             }
         }
 """
 resp = requests.post(url, headers=headers, data=data)
 return resp.json()


@app.route('/PassengerOverDistance')
def getPassengerOverDistance():
 data = """
 {
         "emission_factor": {
    "id": "freight_flight-route_type_international-distance_long_haul-weight_na-contrails_included",
    "source": "BEIS",
    "year": "2021",
    "region": "GB",
    "category": "Air Transport",
    "lca_activity": "usephase"
},
         "parameters":
         {
         "passengers": 4,
         "distance": 100,
         "distance_unit": "km"
    
         }
 """
 resp = requests.post(url, headers=headers, data=data)
 return resp.json()







if __name__ == '__main__':
    app.run()