import sqlite3

def CreateTables():
    connection = sqlite3.connect("Fantasy.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS TeamStats(Manager VARCHAR(30), TeamName VARCHAR(30), Record VARCHAR(10), Score DECIMAL(5,2),PRIMARY KEY(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Roster(Manager VARCHAR(30), TeamName VARCHAR(30), QB VARCHAR(40), RB VARCHAR(40), WR VARCHAR(40), TE VARCHAR(40), DEF VARCHAR(20), K VARCHAR(40), PRIMARY KEY (Manager), FOREIGN KEY (Manager) REFERENCES TeamStats(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS QB(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS RB(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS WR(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS TE(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS DEF(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS K(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute(".tables")
def main():
    CreateTables()
    


if __name__ == "__main__":
    main()
