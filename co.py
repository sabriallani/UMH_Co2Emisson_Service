import requests
from requests.structures import CaseInsensitiveDict

url = "https://beta3.api.climatiq.io/estimate"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer WB253X2YR3MBJ4JAHA2T9DP90CE8"
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = """
{
        "emission_factor": "electricity-energy_source_grid_mix",
        "parameters":
            {
            "energy": 4200,
            "energy_unit": "kWh"
            }
        }
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.json())

