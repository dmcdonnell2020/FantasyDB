import sqlite3

def CreateTables():
    connection = sqlite3.connect("Fantasy.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS QB (Mangager VARCHAR(30), Teamname VARCHAR(30))")

def main():
    CreateTables()


if __name__ == "__main__":
    main()
