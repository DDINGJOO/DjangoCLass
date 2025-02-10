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

    def find_by_id(self, pokemon_id):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT image_url FROM pokedex_images WHERE id=?", (pokemon_id,))
            image_url = cursor.fetchone()
            return image_url


    def save(self, pokemon_id):
        with sqlite3.connect(self.DB_PATH) as conn:
            poke_dex_image = PokeDexImage(pokemon_id)
            poke_dex_image.download_image()
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO pokedex_images (id, image_url) VALUES (?,?)", (pokemon_id, poke_dex_image.image_path))
            conn.commit()
            print(f"Image inserted/updated for Pokémon ID {pokemon_id}")

    def delete_by_id(self, pokemon_id):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pokedex_images WHERE id=?", (pokemon_id,))
            conn.commit()
            print(f"Image deleted for Pokémon ID {pokemon_id}")


if __name__ == "__main__":

    poke_dex_image_repository = PokeDexImageSqlite3()
    poke_dex_image_repository.setup_database()
    poke_dex_image_repository.save(7)
    print(poke_dex_image_repository.find_by_id(7))
    poke_dex_image_repository.delete_by_id(7)


