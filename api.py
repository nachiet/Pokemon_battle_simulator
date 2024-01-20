import requests
import random

def get_pokemon_data(pokemon_name):
    # Use an api to download all data available for pokemon requested 
    base_url = "https://pokeapi.co/api/v2/pokemon"
    response = requests.get(f"{base_url}/{pokemon_name}")
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {pokemon_name}. Status code: {response.status_code}")
        return None
    
    
def read_json_data(pokemon_name):
    # Extract sprite, move, stats and types of the pokemon 
    sprite_url = get_pokemon_data(pokemon_name)['sprites']['front_default']
    raw_moves = [move['move']['name'] for move in get_pokemon_data(pokemon_name)['moves']]
    moves = random.choices(raw_moves, k=4)
    stats = {stat['stat']['name']: stat['base_stat'] for stat in get_pokemon_data(pokemon_name)['stats']}
    types = [type_info['type']['name'] for type_info in get_pokemon_data(pokemon_name)['types']]    
    
    return sprite_url, moves, types, stats


def get_move_data(move_name):
    # Use an api to download and extract movement names, type, and power for a given pokemon
    base_url = "https://pokeapi.co/api/v2/move"
    response = requests.get(f"{base_url}/{move_name}")
    
    if response.status_code == 200:
        move_info = response.json()
        
        move_type = move_info['type']['name']
        move_power = move_info['power']
        
        return move_type, move_power
    else:
        print(f"Failed to retrieve data for {move_name}. Status code: {response.status_code}")
        return None




