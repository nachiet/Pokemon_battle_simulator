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
    global sprite_url
    
    sprite_url = get_pokemon_data(pokemon_name)['sprites']['front_default']
    
    return sprite_url

