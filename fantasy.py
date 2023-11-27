import sqlite3

def CreateTables():
    connection = sqlite3.connect("FantasyDB.db")
    cursor = connection.cursor()
    cursor.execute("DROP TABLE QB")
    cursor.execute("DROP TABLE RB")
    cursor.execute("DROP TABLE WR")
    cursor.execute("DROP TABLE TE")
    cursor.execute("DROP TABLE DEF")
    cursor.execute("DROP TABLE K")
    cursor.execute("CREATE TABLE IF NOT EXISTS TeamStats(Manager VARCHAR(30), Record VARCHAR(10), Score DECIMAL(5,2),PRIMARY KEY(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Roster(Manager VARCHAR(30), QB VARCHAR(40), RB VARCHAR(40), WR VARCHAR(40), TE VARCHAR(40), DEF VARCHAR(20), K VARCHAR(40), PRIMARY KEY (Manager), FOREIGN KEY (Manager) REFERENCES TeamStats(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS QB(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS RB(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS WR(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS TE(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS DEF(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS K(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name), FOREIGN KEY (Manager) REFERENCES Roster(Manager))")

    connection.commit()
    connection.close()

def sqlcommands(s):
    connection = sqlite3.connect("FantasyDB.db")
    cursor = connection.cursor()
    cursor.execute(s)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def main():
    CreateTables()
    sqlcommands("INSERT INTO QB VALUES('Josh Allen', 'Devin McDonnell', 2, 19.8, 20.6, 21.4, 'Healthy','Eagles');")
    sqlcommands("INSERT INTO RB VALUES('Christian Mccaffery', 'Devin McDonnell', 1, 18.8, 18.6, 19.4, 'Healthy', '49ers');")
    sqlcommands("INSERT INTO WR VALUES('Tyreek Hill', 'Devin McDonnell', 2, 19, 20.4, 22.4, 'Healthy', 'Dolphins');")
    sqlcommands("INSERT INTO TE VALUES('Travis Kelce', 'Devin McDonnell', 1, 17, 15.6, 18.4, 'Healthy', 'Cheifs');")
    sqlcommands("INSERT INTO DEF VALUES('Cowboys', 'Devin McDonnell', 5, 10, 9.2, 8.3);")
    sqlcommands("INSERT INTO K VALUES('Justin Tucker', 'Devin McDonnell', 2, 8, 4.6, 7.6, 'Healthy', 'Ravens');")
    
    print("Welcome to Fantasy DB!")
    while(True):
        
        print("Select which feature you would like to use: ")
        choice = input("(1) Insert a player into the database\n (2) Update a players injury status\n (3) Insert a player into your roster\n (4) Delete a player from your roster\n (5) Display the top performers at a position\n (6) Insert your team statistics\n (7) Update another teams statistics\n (8) Update a Manager's UserName\n (9) Display the top teams in your league\n (10) Add a Free Agent to your roster\n")
        if( choice == "1"):
            position = input("Select position of the player(QB, RB, WR, TE, DEF, K): ")
            if position == "DEF":
                #Get vals for def and execute
                name = input("Enter the team name:")
            else:
                #Get alternate vals and execute query
                name = input("Enter the players name:")
        if(choice == "2"):
            position = input("Select position of the player(QB, RB, WR, TE, K): ")            
            name = input("Enter the players name:")
            status = input("Enter the players updated status:(Healthy, Q, O)")
            sqlcommands("UPDATE " + position + " SET Status = \'" + status + "\' WHERE NAME = \'" + name + "\';")
        
        if(choice == '3'):
            mname = input("Enter the manager's name: ")
            sqlcommands("INSERT INTO Roster SELECT q.Manager, q.Name r.Name, w.Name, t.Name, d.Name, k.Name FROM QB q, RB r, WR w, TE t, DEF d, K k WHERE q.Manager = \'" + mname + "\' AND  r.Manager = \'" + mname + "\' AND  w.Manager = \'" + mname + "\' AND  t.Manager = \'" + mname + "\' AND  d.Manager = \'" + mname + "\' AND  k.Manager = \'" + mname + "\';" )

        if(choice == '4'):
            position = input("Select position of the player(QB, RB, WR, TE, DEF, K): ")
            #Copy from 1 but delete
        
        if(choice == '5'):
            position = input("Select position you would like to sort(QB, RB, WR, TE, DEF, K): ")
            print(sqlcommands("SELECT * FROM " + position + " ORDER BY PositionRank LIMIT 5;"))
        
        
        break


if __name__ == "__main__":
    main()
