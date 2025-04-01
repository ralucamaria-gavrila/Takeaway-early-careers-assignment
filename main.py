import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}

url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"
response = requests.get(url, headers=headers)
json_response = json.loads(json.dumps(response.json()))

for key in json_response:
    if key == "restaurants":
        restaurants_list = json_response[key]
        print(restaurants_list[0])


