from pprint import pprint

from common.loggingManeger.logConfig import log_message
from pokeDex.entity.Pokemon import Pokemon, Pokemons
from pokeDex.config.database_selector import DataBaseSelector



class PokeDexService:
    def __init__(self):
        self.db_manager = DataBaseSelector().get_database()


    def insert_pokemons_by_number_until_number(self, number):
        pokemons = Pokemons()
        for i in range(1, number + 1):
            pokemons.add_pokemon(Pokemon(i))
        log_message("info","poke_service.insert_Pokemons_by_number_until_number",f"Inserted {number} Pokemons")
        return self.db_manager.insert_pokemons_data(pokemons.get_all_pokemons())


    def get_pokemon_by_id(self, id):
        raw_pokemon = self.db_manager.fetch_pokemon_by_number(id)
        return self.execute_dict(raw_pokemon)


    def get_pokemon_by_name(self, name):
        raw_pokemon = self.db_manager.fetch_pokemon_by_name(name)
        return self.execute_dict(raw_pokemon)

    def get_pokemons_by_number_ASC(self):
        raw_pokemons = self.db_manager.fetch_all_pokemons()
        return [self.execute_dict(p) for p in raw_pokemons]

    def get_pokemons_by_name_ASC(self):
        raw_pokemons = self.db_manager.fetch_pokemons_data_query_sorted()
        return [self.execute_dict(p) for p in raw_pokemons]

    def _format_pokemon(self, raw_pokemon):
        if raw_pokemon:
            return {
                "name": raw_pokemon[0],
                "id": raw_pokemon[1],
                "hp": raw_pokemon[2],
                "attack": raw_pokemon[3],
                "defense": raw_pokemon[4]
            }
        return None

    def execute_dict(self, raw_pokemon):
        if raw_pokemon:
            return self._format_pokemon(raw_pokemon)


        else:
            log_message("error","poke_service.execute", "No data founded")
            return "No data founded"


if __name__ == '__main__':
    poke_service = PokeDexService()
    # poke_service.insert_pokemons_by_number_until_number(122222221)
    pokemon = poke_service.get_pokemon_by_id(1)
    print(pokemon)
    print(poke_service.get_pokemon_by_name("bulbasaur"))
    pprint(poke_service.get_pokemons_by_number_ASC())
    pprint(poke_service.get_pokemons_by_name_ASC())

    # pokemon = poke_service.insert_pokemons_by_number_until_number(10)