import tkinter as tk
from PIL import Image, ImageTk  # Install Pillow using: pip install pillow
import requests
from io import BytesIO

def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

s1 = load_image('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png')

class PokemonBattleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Pokemon Battle Simulator")

        # Load Pokemon images
        self.pokemon_image1 = ImageTk.PhotoImage(s1)
        self.pokemon_image2 = ImageTk.PhotoImage(s1)

        # Create canvas for Pokemon sprites
        self.canvas = tk.Canvas(master, width=400, height=300, bg="white")
        self.canvas.pack()

        # Display Pokemon sprites
        self.pokemon1_sprite = self.canvas.create_image(100, 150, anchor=tk.CENTER, image=self.pokemon_image1)
        self.pokemon2_sprite = self.canvas.create_image(300, 150, anchor=tk.CENTER, image=self.pokemon_image2)

        # Create health bars
        self.health_bar1 = self.canvas.create_rectangle(50, 20, 150, 30, fill="green")
        self.health_bar2 = self.canvas.create_rectangle(250, 20, 350, 30, fill="green")

        # Create action buttons
        self.fight_button = tk.Button(master, text="Fight", command=self.fight_action)
        self.fight_button.pack(side=tk.LEFT, padx=10)

        self.pokemon_button = tk.Button(master, text="Pokemon", command=self.pokemon_action)
        self.pokemon_button.pack(side=tk.LEFT, padx=10)

        self.bag_button = tk.Button(master, text="Bag", command=self.bag_action)
        self.bag_button.pack(side=tk.LEFT, padx=10)

        self.run_button = tk.Button(master, text="Run", command=self.run_action)
        self.run_button.pack(side=tk.LEFT, padx=10)

    def fight_action(self):
        print("Fight action")

    def pokemon_action(self):
        print("Pokemon action")

    def bag_action(self):
        print("Bag action")

    def run_action(self):
        print("Run action")

if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonBattleGUI(root)
    root.mainloop()
