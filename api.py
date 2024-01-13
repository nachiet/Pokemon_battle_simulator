import requests

def get_pokemon_data(pokemon_name):
    base_url = "https://pokeapi.co/api/v2/pokemon"
    response = requests.get(f"{base_url}/{pokemon_name}")
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {pokemon_name}. Status code: {response.status_code}")
        return None
    
def read_json_data(pokemon_name):
       
    sprite_url = get_pokemon_data(pokemon_name)['sprites']['front_default']
    
    moves = [move['move']['name'] for move in get_pokemon_data(pokemon_name)['moves']]
    
    stats = {stat['stat']['name']: stat['base_stat'] for stat in get_pokemon_data(pokemon_name)['stats']}
    
    types = [type_info['type']['name'] for type_info in get_pokemon_data(pokemon_name)['types']]    
    
    return sprite_url, moves, stats, types
