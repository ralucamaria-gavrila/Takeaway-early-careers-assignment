import requests
import json
from rich.console import Console
from rich.table import Table
from restaurant import Restaurant

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}

url = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/EC4M7RF"
response = requests.get(url, headers=headers)
json_response = json.loads(json.dumps(response.json()))

restaurant_obj = []
restaurants = json_response["restaurants"][0:10]
for restaurant in restaurants:
    restaurant_name = restaurant["name"]
    restaurant_rating = restaurant["rating"]["starRating"]
    print(restaurant_rating)
    restaurant_cuisines = restaurant["cuisines"]
    cuisines = []
    for cuisine in restaurant_cuisines:
        cuisines.append(cuisine["name"])
    print(cuisines)
    restaurant_address = restaurant["address"]
    full_address = ""
    full_address = f"{restaurant_address["firstLine"] + ", " + restaurant_address["postalCode"] + ", " 
                      + restaurant_address["city"]}"
    print(full_address)
    restaurant_obj.append(Restaurant(restaurant_name, full_address, cuisines, restaurant_rating))

console = Console()
table = Table(title="Restaurants")

table.add_column("Name")
table.add_column("Address")
table.add_column("Rating", justify="right")
table.add_column("Cuisines")

for restaurant in restaurant_obj:
    table.add_row(restaurant.name, restaurant.address, str(restaurant.rating), ", ".join(restaurant.cuisine))
console.print(table)