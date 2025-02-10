from pokeDexImages.config.database_selector import DataBaseSelector
from pokeDexImages.entity.PokeDexImage import PokeDexImage
from pokeDexImages.repository.impl.PokeDexImageSqlite3 import PokeDexImageSqlite3


## TODO : Transaction impl?

class PokeDexImageService:
    def __init__(self):
        self.db_manager = DataBaseSelector().get_database()


    def set_pokemon_image_by_id(self, poke_id):
        pokemon = PokeDexImage(poke_id)
        self.db_manager.save(pokemon.pokemon_id)



##TODO : DATA SERIALIZATION & DESERIALIZATION
    def get_pokemon_image_by_id(self, poke_id):
        return self.db_manager.find_by_id(poke_id)

    def delete_pokemon_image_by_id(self, poke_id):

        pokemon = PokeDexImage(poke_id)
        pokemon.delete_image()
        self.db_manager.delete_by_id(poke_id)


if __name__ == "__main__":
    service = PokeDexImageService()
    for i in range(1, 20):
        service.set_pokemon_image_by_id(i)
        print(f"Set image for pokemon {i}")
