# Pokemon_battle_simulator

## Description

This project consists on a pokemon battle simulator made with Python. It uses an graphical user interface (GUI) to display the battles, as in the original pokemon games. Four python scripts have been developed for this work: project.py, api.py, common.py, and test_project.py

The main script is project.py. Once it is executed, the program asks the user for the number of rounds, that will be the number of battles to be held. After that, some pokemon are suggested to the user, consequently asking to choose one, and then another for the enemy (in this case the computer via a random function). Any pokemon is eligible, as the data comes from a web api (https://pokeapi.co/api/v2/) and it is frequently updated. Once the pokemon is selected, a class Pokemon() is created, which contains several pokemon attributes (health, attack, movements...). When created, the Pokemon() class uses functions imported from api.py to download required data from the web api. There is also a Move() class to store movement-specfic attributes (power and type).

Finally, PokemonBattleGUI() class is created, thus constructing the GUI necessary for battle visualization. The use of this class is based on the Tkinter python module, to create a window, allowing the visualization of images of the pokemon, movements, and health status within it. Also Pygame.mixer module is used to play some music, enhancing the user experience with a more ambient feel. Feel free to explore it yourself! (don't worry, if its too much for you, an 'exit' button is available in the game :))

## Script files

project.py: Contains class PokemonBattleGUI(), together with main function, and several other important functions for the development of the project.

api.py: Contains get_move_data, get_pokemon_data, and read_json_data functions, which get pokemon data needed for this project. Concretely, they extract pokemon statistics (health, attack and defense), movements, sprites (images), and types ('fire', 'water', etc.), together with movement power and types.

common.py: Contains Pokemon() and Move() classes.

test_project.py: Contains tests of some project.py functions. To be executed with pytest.

## Design choices

- Pokemon() and Move Classes() were allocated in a different file so the main project.py was not too extensive.

- The GUI was encapsulated in PokemonBattleGUI() class because it allowed enhanced funcionality and control of the events.

- The full pokemon list, the type chart (the chart that contains type's efectiveness against other types), and the pokemon types list were stored in .txt files to allow a faster running time of the program. Information could be also obtained from the api, but the final option seemed more feasible.

- Damage formula is very similar to the one used in the original pokemon games (withouth the random values).



