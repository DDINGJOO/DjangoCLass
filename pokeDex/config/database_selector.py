import os
from common.loggingManeger.logConfig import log_message

class DataBaseSelector:
    def __init__(self):
        self.db_name = os.environ.get("DB_NAME")

    def get_database(self):
        if self.db_name == "SQLite3":
            log_message("info", "database_manager", "using SQLite3 database")
            from pokeDex.repository.impl.PokeDexSqlite3 import PokeDexSqlite3
            PokeDexSqlite3().setup_pokemon_database()
            return PokeDexSqlite3()

        if self.db_name == "MYSQL":
            print("아직 지원 준비중 ..ㅠ")
            return None

        else:
            log_message("error", "Database_manager.setup_database", "db_name is empty check environment variable")
            return None

## TEST

if __name__ == "__main__":
    DataBaseSelector().get_database()