from project import get_number_rounds, get_input_poke, get_type_damage
from unittest.mock import patch

def test_get_number_rounds():
    
    with patch("builtins.input", side_effect=["3"]):
        assert get_number_rounds() == 3
        
    with patch("builtins.input", side_effect=["-2", "5"]):
        result = get_number_rounds()
        assert result == 5
        
    with patch("builtins.input", side_effect=["abc", "2"]):
        result = get_number_rounds()
        assert result == 2
        
def test_get_input_poke(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 'Charmender')
    poke_list = ["Bulbasaur", "Charmander", "Squirtle"]
    assert get_input_poke("Select a Pokémon: ", poke_list) == "Charmender"
    

          
def test_get_type_damage():
    with open("type_chart.txt", "r") as file:
        rows = file.read().split("\n")
        type_chart = [[eval(num) for num in row.split(", ")] for row in rows]
    
    with open("pokemon_types.txt", "r") as file:
        raw_list = file.read()
        pokemon_types = raw_list.strip().split(",")
        
    assert get_type_damage("fire", "water", type_chart, pokemon_types) == 0.5

    assert get_type_damage("electric", "fire", type_chart, pokemon_types) == 1

    assert get_type_damage("fire", "grass", type_chart, pokemon_types)  == 2.0

    assert get_type_damage("electric", "ground", type_chart, pokemon_types)  == 0.0
    
    
        


    
#def test_get_number_rounds():
    