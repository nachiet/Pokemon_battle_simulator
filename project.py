#Script for pokemon battle simulator 
import Pokemon_Battle_GUI
import api
from difflib import get_close_matches


BULBASAUR = {"health": 450, "attack": 49, "defense": 49, "speed": 45}
CHARMANDER = {"health": 390, "attack": 52, "defense": 43, "speed": 65}
SQUIRTLE = {"health": 440, "attack": 48, "defense": 65, "speed": 43}

POKES = {"bulbasaur": BULBASAUR, "charmander": CHARMANDER, "squirtle": SQUIRTLE}

class Pokemon:
    def __init__(self, name):
        self._name = name
        
        poke_dict = POKES[self._char_type]
        self._health = poke_dict["health"]
        self._attack = poke_dict["attack"]
        self._defense = poke_dict["defense"]
        
        data = api.read_json_data(self)
        self._sprite = data[0]
        self._moves = data[1]
        self._stats = data[2]
        self._types = data[3]

    def __str__(self):
        return self._name
    
    def attack(self):
        return self._attack

    def take_damage(self, damage):
        self._health -= damage
        return f"{self._name} took {damage} damage."

    def is_dead(self):
        return self._health <= 0
    
def attack_character(user, enemy, first, second): #attacker, target
        
    damage = first.attack()
    second.take_damage(damage)
    print(user, user._health)
    print(enemy, enemy._health)
    
    
def game_loop(user, enemy): 
    first, second = user, enemy
    while True:
        if input("attack?") == "a":
            attack_character(user, enemy, first, second)
            first, second = second, first 
        if user.is_dead():
            print(f"{user} has fainted. {enemy} won the battle")
            break
        if enemy.is_dead():
            print(f"{enemy} has fainted. {user} won the battle")
            break
    
def get_input_poke(prompt, poke_list):
    while True:
        answer= input(prompt)
        
        if answer in poke_list:
            return answer
        
        close_matches = get_close_matches(answer, poke_list, n=1, cutoff=0.8)
        
        if close_matches:
            suggestion = close_matches[0]
            user_confirmation = input(f"Did you mean '{suggestion}' instead of '{answer}'? (y/n): ")

            if user_confirmation.lower() == 'y':
                return suggestion

        print("Invalid input. Please try again.")

        
def choose_poke():
    poke_list = [key for key in POKES.keys()]
    user = get_input_poke(f"Choose your pokemon from the list: {poke_list} \n", POKES.keys())
    enemy = get_input_poke(f"Choose your enemy's pokemon from the list: {poke_list} \n", POKES.keys())
    return Pokemon(user), Pokemon(enemy)

def main():
    # choose characters and number of fights
    user, enemy = choose_poke()
    
    
    game_loop(user, enemy)
     
if __name__ == "__main__":
    main()
    

    
    