import sys

import pokeDex
from pokeDex import repository
from pokeDex.repository.poke_dex_database_interface  import PokeDexDatabaseInterface
import sqlite3
import os
PATH = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(PATH,"pokeDex.db")


class PokeDexSqlite3(PokeDexDatabaseInterface):

    def __init__(self):
        super().__init__()


        self.DB_PATH =  DB_NAME
        self.COMMANDS = {
            "create_pokemon_table_query": """
                CREATE TABLE IF NOT EXISTS pokemon (
                Name TEXT NOT NULL,
                Number INTEGER PRIMARY KEY,
                Hp INTEGER NOT NULL,
                Attack INTEGER NOT NULL,
                Defense INTEGER NOT NULL)
            """,
            "insert_pokemons_data_query": """
                INSERT OR IGNORE INTO pokemon (Name, Number, Hp, Attack, Defense)
                VALUES (?, ?, ?, ?, ?)
            """,
            "fetch_pokemons_data_query": "SELECT * FROM pokemon",
            "fetch_pokemon_by_number_query": "SELECT * FROM pokemon WHERE Number = ?",
            "update_pokemon_data_query": """
                UPDATE pokemon 
                SET Hp = ?, Attack = ?, Defense = ? 
                WHERE Number = ?
            """,
            "delete_pokemon_by_number_query": "DELETE FROM pokemon WHERE Number = ?",
            "fetch_pokemon_by_name_query":  "  SELECT * FROM pokemon WHERE Name = ?",
            "create_name_index_query": "CREATE INDEX IF NOT EXISTS idx_name ON pokemon(Name)",
            "fetch_pokemons_data_query_sorted": "SELECT * FROM pokemon ORDER BY Name ASC;"}





    def setup_pokemon_database(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(self.COMMANDS.get("create_pokemon_table_query"))
            cursor.execute(self.COMMANDS["create_name_index_query"])
            conn.commit()



    def insert_pokemons_data(self,poke_list):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.executemany(
                self.COMMANDS.get("insert_pokemons_data_query"),
                [(p["Name"], p["Number"], p["Hp"], p["Attack"], p["Defense"]) for p in poke_list],
            )
            conn.commit()
    def update_pokemon_data(self, number, hp, attack, defense):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(self.COMMANDS.get("update_pokemon_data_query"), (hp, attack, defense, number))
            conn.commit()
    def delete_pokemon_by_number(self, number):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(self.COMMANDS.get("delete_pokemon_by_number_query"), (number,))
            conn.commit()

    def fetch_pokemons_data_query_sorted(self):
            with sqlite3.connect(self.DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(self.COMMANDS.get("fetch_pokemons_data_query_sorted"))
                data = cursor.fetchall()
                return data


    def fetch_all_pokemons(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(self.COMMANDS.get("fetch_pokemons_data_query"))
            data = cursor.fetchall()
            return data


    def fetch_pokemon_by_number(self, number):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(self.COMMANDS.get("fetch_pokemon_by_number_query"), (number,))
            data = cursor.fetchone()
            return data

    def fetch_pokemon_by_name(self, name):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(self.COMMANDS.get("fetch_pokemon_by_name_query"), (name,))
            data = cursor.fetchone()
            return data


    def fetch_pokemons_data_query_sorted(self):
        with sqlite3.connect(self.DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(self.COMMANDS.get("fetch_pokemons_data_query_sorted"))
            data = cursor.fetchall()
            return data




if __name__ == "__main__":

    database = PokeDexSqlite3()
    database.setup_pokemon_database()


    # 데이터 입력
    pokemon_data = [
        {"Name": "pikachu", "Number": 25, "Hp": 35, "Attack": 55, "Defense": 40},
        {"Name": "squirtle", "Number": 7, "Hp": 48, "Attack": 65, "Defense": 65},
        {"Name": "charmander", "Number": 4, "Hp": 39, "Attack": 52, "Defense": 43},
        {"Name": "chArmAnder", "Number": 4, "Hp": 40, "Attack": 52, "Defense": 43},
    ]


    database.insert_pokemons_data(pokemon_data)
    database.delete_pokemon_by_number(25)
    print(database.fetch_pokemon_by_number(25))
    print(database.fetch_all_pokemons())
    database.update_pokemon_data(25, 45, 60, 50)
    print(database.fetch_pokemon_by_number(25))
    database.delete_pokemon_by_number(7)
    print(database.fetch_all_pokemons())
    print(database.fetch_pokemon_by_name("Pikachu"))
    print(database.fetch_pokemons_data_query_sorted())