#pip install
import pokebase as pb

poke= pb.pokemon('charmander')

print(poke.height)
print(poke.moves) 

for i in poke.moves:
    print(i.name)

s1 = pb.SpriteResource('pokemon', 17)

print(s1)