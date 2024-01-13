import tkinter as tk
from PIL import Image, ImageTk  # Install Pillow using: pip install pillow
import api

import requests

from io import BytesIO


def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


class PokemonBattleGUI:
    def __init__(self, master, poke_1, poke_2):
        self.master = master
        self.master.title("Pokemon Battle Simulator")
        
        sprite1= load_image(api.read_json_data(poke_1)[0])
        sprite2= load_image(api.read_json_data(poke_2)[0])

        # Load Pokemon images
        self.pokemon_image1 = ImageTk.PhotoImage(sprite1)
        self.pokemon_image2 = ImageTk.PhotoImage(sprite2)

        # Create canvas for Pokemon sprites
        self.canvas = tk.Canvas(master, width=400, height=300, bg="white")
        self.canvas.pack()

        # Display Pokemon sprites
        self.pokemon1_sprite = self.canvas.create_image(100, 150, anchor=tk.CENTER, image=self.pokemon_image1)
        self.pokemon2_sprite = self.canvas.create_image(300, 150, anchor=tk.CENTER, image=self.pokemon_image2)
        
        self.label_window = self.canvas.create_window(200, 280, window=tk.Label(self.canvas,  text=f"What will {poke_1} do?" ))

        # Create health bars
        self.health_bar1 = self.canvas.create_rectangle(50, 20, 150, 30, fill="green")
        self.health_bar2 = self.canvas.create_rectangle(250, 20, 350, 30, fill="green")

        # Create action buttons
        self.fight_button = tk.Button(master, text="Fight", command=self.fight_action) #(poke_1)) #width=10, height=2
        self.fight_button.pack(side=tk.LEFT, padx=50)

        self.bag_button = tk.Button(master, text="Bag", command=self.bag_action)
        self.bag_button.pack(side=tk.LEFT, padx=50)

        self.run_button = tk.Button(master, text="Run", command=self.run_action)
        self.run_button.pack(side=tk.LEFT, padx=50)
        

    def fight_action(self):# , poke_1):
        print("Fight action")

        self.remove_movement_buttons()
        
        movements = ['moves', 'en', 'sil', 'encio'] #poke_1._moves
        for move in movements:
            move_button = tk.Button(self.master, text=move, command=lambda m=move: self.move_action(m))
            move_button.pack(side=tk.LEFT, padx=25)
        
        # Back button

    def bag_action(self):
        print("Bag action")

    def run_action(self):
        print("Run action")
        
    def remove_movement_buttons(self):
    # Destroy all buttons except the initial ones (Fight, Bag, Run)
        for widget in self.master.winfo_children():
            if widget in [self.fight_button, self.bag_button, self.run_button]:
                widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonBattleGUI(root, "bulbasaur", "pikachu")
    root.mainloop()
