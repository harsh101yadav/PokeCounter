import type_match_up
import requests
from bs4 import BeautifulSoup
url = "https://pokemondb.net/type/dual"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

types = ("None","Normal","Fire","Water","Electric","Grass","Ice","Fighing","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon","Dark","Steel","FAiry")

# Creating list for all types
effectiveness_cells = soup.find_all("td", class_=lambda x: x and x.startswith("type-fx-cell"))
effectiveness_values = [cell.text.strip() for cell in effectiveness_cells]


#cearing lists within the list such that each type matchup has it's own list
chunk_size = 18
list_of_lists = []
for i in range(0, len(effectiveness_values), chunk_size):
    sublist = effectiveness_values[i:i+chunk_size]
    list_of_lists.append(sublist)
print(list_of_lists)

#Opening python file and creating dictionaries
# with open("type_match_up.py","w") as file:
#     for type_name in types[1:]:
#         file.write(f"type_matchup_{type_name} = {{}}\n")

# Filling up each list
# count = 0
# for i,type_name in enumerate(types[1:],start = 1):
#     # x = getattr(type_match_up, f"type_matchup_{type_name}")
#     x={}
#     print(type(x))
#     x["NA"]=types[1:]
#     for j,secondary_type in enumerate(types):
#         if(type_name==secondary_type):
#             continue
#         if count < len(list_of_lists):
#             x.update({(type_name, secondary_type): list_of_lists[count]})
#             print("\n")
#             count += 1
#     print(x)
#     with open("type_match_up.py","a") as file:
#         file.write(f"type_matchup_{type_name} = {x}\n" )
            
        
