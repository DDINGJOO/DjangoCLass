import requests
from dotenv import load_dotenv

from common.loggingManeger.logConfig import log_message
import os


# Entity, Model, Schema
class Pokemon:
    def __init__(self, number):
        self.number = number
        self.name = None
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.fetch_pokemon_data()

    def info_pokemon(self):
        return {
            "Number": self.number,
            "Name": self.name,
            "Hp": self.hp,
            "Attack": self.attack,
            "Defense": self.defense,
        }


    def print_pokemon(self):
        print(f"Number: {self.number}")
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")


    def fetch_pokemon_data(self):
        load_dotenv()
        try:
            log_message("info","pokemon.py -> Pokemon.fetch_pokemon_data", f"number: {self.number}")

            name_url = f"{os.environ.get("POKEAPI_STATS_BASE_URL")}/pokemon-form/{self.number}/"
            stats_url = f"{os.environ.get("POKEAPI_STATS_BASE_URL")}/pokemon/{self.number}/"
            print(f"Name URL: {name_url}")

            name_response = requests.get(name_url)
            stats_response = requests.get(stats_url)

            if name_response.status_code != 200 or stats_response.status_code != 200:
                log_message("error","pokemon.py -> Pokemon.fetch_pokemon_data", f"code = {name_response.status_code}")
                return

            self.name = name_response.json().get("pokemon", {}).get("name", "Unknown")
            stats = {stat["stat"]["name"]: stat["base_stat"] for stat in stats_response.json().get("stats", [])}
            self.hp = stats.get("hp", 0)
            self.attack = stats.get("attack", 0)
            self.defense = stats.get("defense", 0)

        except Exception as e:
            log_message("error","pokemon.py -> Pokemon.fetch_pokemon_data", f"code: {e}")




class Pokemons:
    def __init__(self):
        self.pokemons = []

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def get_pokemon(self, number):
        for pokemon in self.pokemons:
            if pokemon.number == number:
                return pokemon.info_pokemon()
        return "No Pokemon found with this number."



    def update_pokemon(self, number, attribute, new_value):
        for pokemon in self.pokemons:
            if pokemon.number == number:
                if hasattr(pokemon, attribute):
                    setattr(pokemon, attribute, new_value)
                    return pokemon.info_pokemon()
                return f"Attribute '{attribute}' not found."
        return "No Pokemon found with this number."



    def delete_pokemon(self, number):
        for i, pokemon in enumerate(self.pokemons):
            if pokemon.number == number:
                del self.pokemons[i]
                return f"Pokémon with number {number} deleted successfully."
        return "No Pokemon found with this number."

    def get_all_pokemons(self):
        return [pokemon.info_pokemon() for pokemon in self.pokemons]

    def print_all_pokemons(self):
        for pokemon in self.pokemons:
            pokemon.print_pokemon()
            print(os.environ.get("UNDER_LINE"))

if __name__ == "__main__":

    pokemons = Pokemons()
    pokemons.add_pokemon(Pokemon(1))
    pokemons.add_pokemon(Pokemon(2))
    pokemons.add_pokemon(Pokemon(3))
    pokemons.print_all_pokemons()




