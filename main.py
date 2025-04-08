import requests
import json
from rich.console import Console
from rich.table import Table
from restaurant import Restaurant


def extract_restaurant_data(api_response, number_of_restaurants):
    restaurant_obj = []
    restaurants = api_response["restaurants"][0:number_of_restaurants]
    for restaurant in restaurants:
        restaurant_name = restaurant["name"]
        restaurant_rating = restaurant["rating"]["starRating"]
        restaurant_cuisines = restaurant["cuisines"]
        cuisines = []
        for cuisine in restaurant_cuisines:
            cuisines.append(cuisine["name"])
        restaurant_address = restaurant["address"]
        full_address = f"{restaurant_address['firstLine']}, {restaurant_address['postalCode']}, {restaurant_address['city']}"
        restaurant_obj.append(Restaurant(restaurant_name, full_address, cuisines, restaurant_rating))
    return restaurant_obj


def display_data(restaurant_list):
    console = Console()
    table = Table(title="Restaurants")

    table.add_column("Name")
    table.add_column("Address")
    table.add_column("Rating", justify="right")
    table.add_column("Cuisines")

    for restaurant in restaurant_list:
        if restaurant.rating != 0:
            table.add_row(restaurant.name, restaurant.address, str(restaurant.rating), ", ".join(restaurant.cuisine))
        else:
            table.add_row(restaurant.name, restaurant.address, "The restaurant does not have any reviews yet",
                          ", ".join(restaurant.cuisine))

    console.print(table)


if __name__ == '__main__':
    postcode = input("Type the postcode for the area where you would like to find information about restaurants. "
                     "Press enter to submit your answer. "
                     "Only UK based postcodes are supported currently! ")

    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")

    json_response = json.loads(json.dumps(response.json()))
    restaurants_json = json_response.get("restaurants", [])
    if not restaurants_json:
        print("No restaurants found for this postcode or the postcode is not UK based.")
        exit(0)
    else:
        display_data(extract_restaurant_data(json_response, 10))
