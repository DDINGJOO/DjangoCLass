from pokeDex.service.PokeDexService import PokeDexService

from pprint import pprint
if __name__ == "__main__":
    poke_service = PokeDexService()
    poke_service.insert_pokemons_by_number_until_number(20)
    pprint(poke_service.get_pokemon_by_id(3))
    pprint(poke_service.get_pokemons_by_name_ASC())

##   Client PostCall API for insertPokemons until set number ascendant
##   url    = "http://DNS.com/api/insertPokemons/{number} -> 15
##
##   Server Call API for insertPokemons until set number asc
##      Method insert_Pokemons_by_number_until_number