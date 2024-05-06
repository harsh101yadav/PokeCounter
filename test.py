# typeweekness ={}
# typeweekness["Fire"] = "Water"
# typeweekness["Water"] = "Electric"
# typeweekness["Electric"] = "Ground"

# # Print the dictionary
# print("Initial Dictionary:", typeweekness)

# # Perform dictionary methods
# # Add a new key-value pair
# typeweekness["Grass"] = "Fire"
# print("After adding 'Grass':", typeweekness)

# # Remove a key-value pair
# del typeweekness["Fire"]
# print("After removing 'Fire':", typeweekness)

# # Get the value for a specific key
# print("Value for 'Water':", typeweekness.get("Water"))

# # Get all keys in the dictionary
# print("Keys:", typeweekness.keys())

# # Get all values in the dictionary
# print("Values:", typeweekness.values())

import json

with open('cleaned_data.json', 'r') as file:
    data = json.load(file)

normal = data["Normal"]["None"]
print(normal["Nor"]) 