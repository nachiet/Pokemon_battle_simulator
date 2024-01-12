#Script for pokemon battle simulator 

BULBASAUR = {"health": 450, "attack": 49, "defense": 49, "speed": 45}
CHARMANDER = {"health": 390, "attack": 52, "defense": 43, "speed": 65}
SQUIRTLE = {"health": 440, "attack": 48, "defense": 65, "speed": 43}

POKES = {"bulbasaur": BULBASAUR, "charmander": CHARMANDER, "squirtle": SQUIRTLE}

class Pokemon:
    def __init__(self, char_type):
        self._char_type = char_type
        poke_dict = POKES[self._char_type]
        self._health = poke_dict["health"]
        self._attack = poke_dict["attack"]
        self._defense = poke_dict["defense"]

    def __str__(self):
        return self._char_type
    
    def attack(self):
        return self._attack

    def take_damage(self, damage):
        self._health -= damage
        return f"{self._char_type} took {damage} damage."

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

def main():
    # choose characters and number of fights
    user, enemy = choose_poke()
    
    
    game_loop(user, enemy)
    
def get_input(prompt, lista):
    while True:
        try:
            answer= input(prompt)
        except:
            for i in range(len(answer),0, -1):
                for key in lista:
                    if key.startswith(answer):
                        suggestion = key
            print(f"Did you mean {suggestion}")
        

def choose_poke():
    poke_list = [key for key in POKES.keys()]
    user= get_input(f"Choose your pokemon from the list: {poke_list} \n", POKES.keys())
    enemy= input(f"Choose your enemy's pokemon from the list: {poke_list} \n")
    return Pokemon(user), Pokemon(enemy)
    
    
if __name__ == "__main__":
    main()
    

    
    