import requests

def fetch_pokemon_data(enemy_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{enemy_pokemon.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Failed to fetch data for", enemy_pokemon)
        return None
    

    
enemy_pokemon = input("Enter The pokemon you want to battle: ")
# enemy_pokemon = "pikachu"
pokemon_data = fetch_pokemon_data(enemy_pokemon)# returns all values as dictionary

print("Out of these moves")
all_moves = [move_data["move"]["name"] for move_data in pokemon_data["moves"]]
print(all_moves)
print(f"Which moves does {enemy_pokemon} knows?")
move_list = []
for i in range (4):
    move_list.append(input(f"{i+1}:"))
    #write code to check if move is available to the pokemon
print("Out",move_list)
