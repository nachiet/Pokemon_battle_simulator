import api
import tkinter as tk
import random
import requests
from common import Pokemon, Move
from io import BytesIO
from difflib import get_close_matches
from PIL import Image, ImageTk  
from pygame import mixer


class PokemonBattleGUI:
    
    def __init__(self, master, user, enemy):
        #Initialize main variables
        self.master = master
        self.master.title("Pokemon Battle Simulator")
        self.user = user
        self.enemy = enemy
        
        # Load Pokemon images
        sprite_1= load_image(api.read_json_data(self.user)[0])
        sprite_2= load_image(api.read_json_data(self.enemy)[0])
        self.pokemon_image_1 = ImageTk.PhotoImage(sprite_1)
        self.pokemon_image_2 = ImageTk.PhotoImage(sprite_2)
        
        # Load and resize the background image
        background_image = Image.open("background.png")
        background_image = background_image.resize((400, 300))
        self.background_image = ImageTk.PhotoImage(background_image)

        # Initialize main screen 
        self.main_screen(f"What will your {self.user} do?")

        # Create initial buttons
        self.create_initial_buttons()
        
        #Play game music
        mixer.init()
        mixer.music.load("battle_music.mp3")
        mixer.music.play()
        

    def main_screen(self, prompt):
        # Create a canvas that will contain all the elements
        self.canvas = tk.Canvas(self.master, width=400, height=300, bg="white")
        self.canvas.pack()

        # Create the background image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        
        # Display Pokemon sprites
        self.pokemon1_sprite = self.canvas.create_image(125, 210, anchor=tk.CENTER, image=self.pokemon_image_1)
        self.pokemon2_sprite = self.canvas.create_image(277, 120, anchor=tk.CENTER, image=self.pokemon_image_2)
        
        # Display text label
        self.label_window = self.canvas.create_window(200, 280, window=tk.Label(self.canvas, text=prompt))

        # Create health bars
        self.health_bar1 = self.canvas.create_rectangle(75, 120, 75 + self.user.health_percentage(), 130, fill="green")
        self.damage_bar1 = self.canvas.create_rectangle(75 + self.user.health_percentage(), 120, 175, 130, fill="red")
        self.health_bar2 = self.canvas.create_rectangle(227, 50, 227 + self.enemy.health_percentage(), 60, fill="green")
        self.damage_bar2 = self.canvas.create_rectangle(227 + self.enemy.health_percentage(), 50, 327, 60, fill="red")
        
        
    def create_initial_buttons(self):
        self.fight_button = tk.Button(self.master, text="Fight", command=self.fight_action) 
        self.fight_button.pack(side=tk.LEFT, padx=80)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.exit_action)
        self.exit_button.pack(side=tk.LEFT, padx=80)
        
            
    def fight_action(self):
        # Remove previous buttons of the screen
        self.remove_initial_buttons()
        
        # Create a button for each move and display on the screen
        for move in self.user.moves():
            move_button = tk.Button(self.master, text=move, command = lambda move = move : self.perform_attack(move))
            move_button.pack(side=tk.LEFT, padx=25)
              
              
    def perform_attack(self, move):
        # Perform the attack, modifying each pokemon attributes
        attack_character(self.user, self.enemy, Move(move))
        
        # Check if any player is dead
        self.check_players_status()
        
        # Remove movement buttons
        self.remove_all_widgets()  
              
        # Perform enemy attack (automatically generated)       
        self.enemy_attack()


    def enemy_attack(self):
        # Randomly choose one of the enemys attack and perform it
        move = random.choice(self.enemy.moves())
        attack_character(self.enemy, self.user, Move(move))
        
        # Display actual situation of the pokemon and restore initial state
        self.remove_all_widgets()        
        self.main_screen(f"Wild {self.enemy} used {move}!")
        self.create_initial_buttons()


    def exit_action(self):
        # Exit the program
        print("Exit was successful.\n")
        exit()
        
        
    def remove_initial_buttons(self):
        # Destroy fight and exit button
        for widget in self.master.winfo_children():
            if widget in [self.fight_button, self.exit_button]:
                widget.destroy()
                
                
    def remove_all_widgets(self):
        # Destroy all widgets (buttons and canvas)
        for widget in self.master.winfo_children():
            widget.destroy()
                
    
    def check_players_status(self):
        # Exit the game if any of the players is dead
        if self.user.is_dead():
            print(f"Your {self.user} has fainted. Wild {self.enemy} won the battle! Closing the window.\n")
            self.master.destroy()
            exit()
            
        if self.enemy.is_dead():
            print(f"Wild {self.enemy} has fainted. Your {self.user} won the battle! Closing the window.\n")
            self.master.destroy()
            exit()
            
##########################################################################            
 
 
def attack_character(user, enemy, move): 
    # Obtains damage factors caused by movement efectiveness against enemies types. 
    damage_type_1 = get_type_damage(move.type(), enemy.type_1(), type_chart, pokemon_types)

    damage_type_2 = 1
    if enemy.type_2() is not None:
        damage_type_2 = get_type_damage(move.type(), enemy.type_2(), type_chart, pokemon_types)

    # Obtains damage factor caused by using a movement that is the same type as the user pokemon.
    stab = 1
    if move.type() in [user.type_1(), user.type_2()]:
        stab = 1.5

    # Damage formula
    damage = (((2/5 + 2) * move.power() * user.attack() / enemy.defense()) / 50 + 2 ) * stab * damage_type_1 * damage_type_2 
    enemy.take_damage(damage)
       
            
def get_input_poke(prompt, poke_list):
    # Ask user to select a pokemon, checking misspelling mistakes
    while True:
    
        answer= input(prompt)
                
        if answer in poke_list:
            return answer
        
        close_matches = get_close_matches(answer, poke_list, n=1, cutoff=0.7)
        
        if close_matches:
            suggestion = close_matches[0]
            user_confirmation = input(f"Did you mean '{suggestion}' instead of '{answer}'? (y/n): ")

            if user_confirmation.lower() == 'y':
                return suggestion

        print("Invalid input. Please try again.")
        

def get_number_rounds():
    # Ask user for number of battles
    while True:
        
        try:
            num_rounds = int(input("How many rounds do you wish to play?\n"))
            
            if num_rounds > 0:
                return num_rounds
            
            elif num_rounds < 0:
                print("Invalid input. Input most be a positive integer.")
                
            else:
                print("See you soon!")
                exit()
                
        except ValueError:
            print("Invalid input. Input most be a positive integer.")


def get_type_damage(move_type, enemy_type, type_chart, pokemon_types):
    # Obtain damage factor caused by type advantage
    return type_chart[pokemon_types.index(move_type)][pokemon_types.index(enemy_type)]


def get_txt_info():
    # Get all pokemon names from .txt file and stores it in a list
    with open("all_pokemon_list.txt", "r") as file:
        global all_poke_list
        raw_list = file.read().strip().split(',')
        all_poke_list = [poke.strip(" '") for poke in raw_list]
    
    # Get the type chart from . file and stores it in a list
    with open("type_chart.txt", "r") as file:
        global type_chart
        rows = file.read().split('\n')
        type_chart = [[eval(num) for num in row.split(", ")] for row in rows]
    
    # Get all pokemon types from .txt file and stores it in a list    
    with open('pokemon_types.txt', 'r') as file:
        global pokemon_types
        raw_list = file.read()
        pokemon_types = raw_list.strip().split(',')
        
        
def load_image(url):
    # Download images from url (for pokemon sprites)
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img
            
  
def welcome():
    print('''--------------------------------------------------
    WELCOME TO THE POKEMON BATTLE SIMULATOR
                    
         by Ignacio García Guadalupe
                    
--------------------------------------------------
          ''')
    
    
def main():
    
    welcome()
    n = get_number_rounds()
    print("\nIf you are new to pokemon, here are some examples: bulbasaur, pikachu, charizard. You can use every pokemon known!\n")
    
    for _ in range(0,n):
        
        prompt_user = f"Choose your pokemon\n"
        prompt_enemy = f"Choose your enemy's pokemon\n"
        
        get_txt_info()

        poke_1, poke_2 = get_input_poke(prompt_user, all_poke_list), get_input_poke(prompt_enemy, all_poke_list)
        
        print("Wait a few seconds...")
        
        root = tk.Tk()
        app = PokemonBattleGUI(root, Pokemon(poke_1), Pokemon(poke_2))
        root.mainloop()
        mixer.music.stop()
        
        print("\n\nSimulator is closed. Thanks for playing!\n\n")


if __name__ == "__main__":
    main()

