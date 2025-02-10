from pokeDexImages.entity.PokeDexImage import PokeDexImage
from pokeDexImages.repository.poke_dex_image_interface import PokeDexImageDataBaseInterface
import sqlite3
import os
PATH = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(PATH,"pokeDexImage.db")


class PokeDexImageSqlite3(PokeDexImageDataBaseInterface):
    def __init__(self):
        super().__init__()
        self.DB_PATH =  DB_NAME

    def setup_database(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS pokedex_images
                             (id INTEGER PRIMARY KEY, image_url TEXT NOT NULL)''')
            conn.commit()

    def get_image_path(self, pokemon_id):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT image_url FROM pokedex_images WHERE id=?", (pokemon_id,))
            image_url = cursor.fetchone()
            return image_url


    def insert_image(self, pokemon_id, image_path):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO pokedex_images (id, image_url) VALUES (?,?)", (pokemon_id, image_path))
            conn.commit()
            print(f"Image inserted/updated for Pokémon ID {pokemon_id}")



if __name__ == "__main__":

    poke_dex_image_repository = PokeDexImageSqlite3()
    poke_dex_image_repository.setup_database()
    poke_dex_image_repository.insert_image(3,"https://example.com/image1.png")
    print(poke_dex_image_repository.get_image_path(3))

    # # Example usage
    # # Insert an image for a specific Pokémon
    # image_path = "example_image.png"
    # poke_dex_image_repository.insert_image(1, image_path)
    #
    # # Get the image path for a specific Pokémon
    # image_path = poke_dex_image_repository.get_pokemon_image_path(1)
    # print(f"Image path for Pokémon ID 1: {image_path}")
    #
    # # Delete an image for a specific Pokémon
    # # poke_dex_image_repository.delete_image(1)
    # #
    # # Update the image path for a specific Pokémon
    # new_image_path = "updated_example_image.png"

