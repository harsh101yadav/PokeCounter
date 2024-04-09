import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Failed to fetch data for", pokemon_name)
        return None

# Example usage: Fetch data for Pikachu
pikachu_data = fetch_pokemon_data("pikachu")
if pikachu_data:
    print("Name:", pikachu_data["name"])
    print("Types:", [type_data["type"]["name"] for type_data in pikachu_data["types"]])
    print("Moveset:", [move_data["move"]["name"] for move_data in pikachu_data["moves"]])
    print("Stats:", {stat_data["stat"]["name"]: stat_data["base_stat"] for stat_data in pikachu_data["stats"]})
    # Add more data extraction as needed
