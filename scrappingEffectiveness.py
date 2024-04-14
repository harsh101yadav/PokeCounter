import requests 
from bs4 import BeautifulSoup
url = "https://pokemondb.net/type/dual"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# for heading in soup.find_all("h2"):
#   print(heading.text)

# Find all td elements with class starting with 'type-fx-cell'
effectiveness_cells = soup.find_all("td", class_=lambda x: x and x.startswith("type-fx-cell"))

# Extract the effectiveness values
effectiveness_values = [cell.text.strip() for cell in effectiveness_cells]

# print("Effectiveness values:", effectiveness_values)


chunk_size = 18
list_of_lists = [effectiveness_values[i:i+chunk_size] for i in range(0, len(effectiveness_values), chunk_size)]

print(list_of_lists[1])