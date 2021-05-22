import requests
import json

base_url = "https://api.openweathermap.org/data/2.5/onecall?lat="
base_url2 = "&lon="
base_url3 = "&exclude=hourly,daily,minutely&appid="

api_key = "8bbc3242fc1979aa131985a43d2d8fb7"

def get_api_data(lat, lon):
	query_string = base_url + str(lat) + base_url2 + str(lon) + base_url3 + api_key
	req = requests.get(query_string)
	if req.status_code == 200:
		obj = req.json()
		return obj
	else:
		return False

