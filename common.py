import api

class Pokemon:
    
    def __init__(self, name):
        self._name = name

        # Store all data obtained from the api
        data = api.read_json_data(self)
        
        self._sprite = data[0]
        self._moves = data[1]
        self._types = data[2]
        
        poke_stats = data[3]
        self._health = poke_stats["hp"]
        self._attack = poke_stats["attack"]
        self._defense = poke_stats["defense"]
        
        self._initial_health = self._health
        
    def __str__(self):
        return self._name
    
    def health(self):
        return self._health
    
    def health_percentage(self):
        return round(self._health/self._initial_health*100)
    
    def attack(self):
        return self._attack
    
    def defense(self):
        return self._defense
    
    def type_1(self):
        return self._types[0]
    
    # Only some pokemon have a second type, so the situation has to be handled.
    def type_2(self):
        try:
            return self._types[1]
        except:
            return None
    
    def moves(self):
        return self._moves
    
    def heal(self, health_points):
        self._health += health_points 
        return f"{self._name} took {health_points} health points."
    
    def take_damage(self, damage):
        self._health -= damage
        return f"{self._name} took {damage} damage."

    def is_dead(self):
        return self._health <= 0
    
##########################################################

class Move:
    
    def __init__(self, name):
        self._name = name
        
        move_data = api.get_move_data(self._name)
        self._type = move_data[0]
        self._power = move_data[1] 
        
    def __str__(self):
        return self._name
        
    def type(self):
        return self._type
        
    # Movements with no power have been assigned a low power for convenience.
    def power(self):
        if self._power == None:
            self._power = 40
        return self._power

###########################################################





        


    
    