import type_match_up
# import requests
# from bs4 import BeautifulSoup
# url = "https://pokemondb.net/type/dual"
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')

types = ["None","Normal","Fire","Water","Electric","Grass","Ice","Fighing","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon","Dark","Steel","FAiry"]

#Creating list for all types
# effectiveness_cells = soup.find_all("td", class_=lambda x: x and x.startswith("type-fx-cell"))
# effectiveness_values = [cell.text.strip() for cell in effectiveness_cells]


#cearing list of list
# chunk_size = 18
# list_of_lists = []
# for i in range(0, len(effectiveness_values), chunk_size):
#     sublist = effectiveness_values[i:i+chunk_size]
#     list_of_lists.append(sublist)


#Opening python file and creating dictionaries
with open("type_match_up.py","w") as file:
    for type_name in types[1:]:
        file.write(f"type_matchup_{type_name} = {{}}\n")

# Filling up each list
count = 0
for i,type_name in enumerate(types,start = 1):
    
    from type_match_up import type_matchup_
