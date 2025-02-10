from pokeDexImages.config.database_selector import DataBaseSelector
from pokeDexImages.entity.PokeDexImage import PokeDexImage
from pokeDexImages.repository.impl.PokeDexImageSqlite3 import PokeDexImageSqlite3


class PokeDexImageService:
    def __init__(self):
        self.db_manager = DataBaseSelector().get_database()


    def set_pokemon_by_id(self, poke_id):
        pokemon = PokeDexImage(poke_id)
        self.db_manager.insert_image(pokemon.pokemon_id,pokemon.image_path)



##TODO : DATA SERIALIZATION & DESERIALIZATION
    def get_pokemon_image_by_id(self, poke_id):
        return self.db_manager.get_image_path(poke_id)






if __name__ == "__main__":
    service = PokeDexImageService()
    service.set_pokemon_by_id(1)  # Assuming 1 is the id of Charmander for demonstration.
    pokeId = service.get_pokemon_image_by_id(1)
