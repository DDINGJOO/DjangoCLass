from pokeDexImages.entity.PokeDexImage import PokeDexImage
from pokeDexImages.service.PokeDexImageService import PokeDexImageService

if __name__ == "__main__":
    pokeimage= PokeDexImageService()
    pokeimage.set_pokemon_by_id(11)
    print(pokeimage.get_pokemon_image_by_id(11))