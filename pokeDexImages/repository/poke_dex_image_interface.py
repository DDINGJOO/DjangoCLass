class PokeDexImageDataBaseInterface:
    def setup_database(self):
        pass

    def save(self, pokemon_id, image_path):
        pass

    def find_by_id(self, pokemon_id):
        pass



    def delete_image(self, pokemon_id):
        pass

    def update_image_path(self, pokemon_id, new_image_path):
        pass

    def get_all_pokemon_ids(self):
        pass


    def get_pokemon_image_path(self, pokemon_id):
        pass
