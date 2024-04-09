class Pokemon:
    def __init__(self, name, types, moveset, stats, abilities, evolution_line, base_experience):
        self.name = name
        self.types = types
        self.moveset = moveset
        self.stats = stats
        self.abilities = abilities
        self.evolution_line = evolution_line
        self.base_experience = base_experience

# Create a dictionary to store Pokémon data
pokemon_data = {}

# Add Pokémon data to the dictionary
def add_pokemon(name, types, moveset, stats, abilities, evolution_line, base_experience):
    pokemon = Pokemon(name, types, moveset, stats, abilities, evolution_line, base_experience)
    pokemon_data[name] = pokemon

# Add Pokémon data here
add_pokemon("Bulbasaur", ["Grass", "Poison"], ["Tackle", "Vine Whip"], {"HP": 45, "Attack": 49, "Defense": 49, "Sp. Atk": 65, "Sp. Def": 65, "Speed": 45}, ["Overgrow"], ["Bulbasaur", "Ivysaur", "Venusaur"], 64)
add_pokemon("Charmander", ["Fire"], ["Scratch", "Ember"], {"HP": 39, "Attack": 52, "Defense": 43, "Sp. Atk": 60, "Sp. Def": 50, "Speed": 65}, ["Blaze"], ["Charmander", "Charmeleon", "Charizard"], 62)
# Add more Pokémon data as needed

# Example usage: accessing data for Bulbasaur
print("Name:", pokemon_data["Bulbasaur"].name)
print("Types:", pokemon_data["Bulbasaur"].types)
print("Moveset:", pokemon_data["Bulbasaur"].moveset)
print("Stats:", pokemon_data["Bulbasaur"].stats)
print("Abilities:", pokemon_data["Bulbasaur"].abilities)
print("Evolution Line:", pokemon_data["Bulbasaur"].evolution_line)
print("Base Experience:", pokemon_data["Bulbasaur"].base_experience)
