import sqlite3

def CreateTables():
    connection = sqlite3.connect("FantasyDB.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    
    cursor.execute("DROP TABLE Roster")
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

def print_results(query):
    conn = sqlite3.connect("FantasyDB.db")
    cursor = conn.cursor()
    cursor.execute(query)
    headers = [description[0] for description in cursor.description]
    rows = cursor.fetchall()

    if not rows:
        print("No data found")
        return

        
    for header in headers:
        print(f"{header.ljust(20)}", end=" | ")
    print()  
    print("-" * (20 * len(headers) + len(headers) - 1)) 

    for row in rows:
        for value in row:
            print(f"{str(value).ljust(20)}", end=" | ")
        print()  
    conn.close()

def sqlcommands(s):
    connection = sqlite3.connect("FantasyDB.db")
    cursor = connection.cursor()
    cursor.execute(s)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def main():
    connection = sqlite3.connect("FantasyDB.db")
    cursor = connection.cursor()
    CreateTables()
    
    print("Welcome to Fantasy DB!")
    ask = "Y"
    while(ask == "Y"):
        
        print("Select which feature you would like to use: ")
        choice = input(" (1) Insert a player into the database\n (2) Update a players injury status\n (3) Display a manager's roster\n (4) Delete a player from your roster\n (5) Display the top performers at a position\n (6) Insert your team statistics\n (7) Update another teams statistics\n (8) Update a Manager's Name\n (9) Display the current standings of your league\n (10) Add a Free Agent to your roster\n (11) Remove a team from the league \n (12) Quit\n")
        if( choice == "1"):
            position = ""
            while(position not in ["QB", "RB", "WR", "TE", "DEF", "K"] ):
                position = input("Select position of the player(QB, RB, WR, TE, DEF, K): ")    
                if position not in ["QB", "RB", "WR", "TE", "DEF", "K"]:
                    print("Enter a valid position")  
            if position == "DEF":
                #Get vals for def and execute
                name = input("Enter the team name of the defense: ")
                manager = input("Enter the manager name(None if player is a free agent): ")
                rank = 0
                score = -1
                ppg = -1
                proj = -1
                while(rank < 1):
                    rank = int(input("Enter the position rank of the defense you would like to add: "))
                    if rank < 1:
                        print("Please enter a value greater than 0")
                while(score < 0.00):
                    score = float(input("Enter this weeks score for the defense you would like to add: "))
                    if score < 0.00:
                        print("Please enter a value greater than 0.0")
                while(ppg < 0.00):
                    ppg = float(input("Enter the number of points the defense scores per game: "))
                    if ppg < 0.00:
                        print("Please enter a value greater than 0.0")
                while(proj < 0.00):
                    proj = float(input("Enter the number of points the defense is projected to score this week: "))
                    if proj < 0.00:
                        print("Please enter a value greater than 0.0")
                sqlcommands("INSERT INTO DEF VALUES(\'" + name + "\', \'" + manager + "\', " + str(rank) + ", " + str(score) + ", " + str(ppg) + ", " + str(proj)  + ");")
                print("Updated Defenses:")
                print_results("SELECT * FROM DEF;")
            else:
                #Get alternate vals and execute query
                name = input("Enter the players name: ")
                manager = input("Enter the manager name(None if player is a free agent): ")
                rank = 0
                score = -1
                ppg = -1
                proj = -1
                while(rank < 1):
                    rank = int(input("Enter the position rank of the player you would like to add: "))
                    if rank < 1:
                        print("Please enter a value greater than 0")
                while(score < 0.00):
                    score = float(input("Enter this weeks score for the player you would like to add: "))
                    if score < 0.00:
                        print("Please enter a value greater than 0.0")
                while(ppg < 0.00):
                    ppg = float(input("Enter the number of points the player scores per game: "))
                    if ppg < 0.00:
                        print("Please enter a value greater than 0.0")
                while(proj < 0.00):
                    proj = float(input("Enter the number of points the player is projected to score this week: "))
                    if proj < 0.00:
                        print("Please enter a value greater than 0.0")
                status = input("Enter the player's status(Healthy, Q, O): ")
                team = input("Enter the team that the player plays for: ")
                sqlcommands("INSERT INTO " + position + " VALUES(\'" + name + "\', \'" + manager + "\', " + str(rank) + ", " + str(score) + ", " + str(ppg) + ", " + str(proj)  + ", \'" + status + "\', \'" + team + "\');")
                print("Updated " + position + "s:")
                print_results("SELECT * FROM " + position + ";")

        if(choice == "2"):
            position = ""
            while(position not in ["QB", "RB", "WR", "TE", "K"] ):
                position = input("Select position of the player(QB, RB, WR, TE, K): ")    
                if position not in ["QB", "RB", "WR", "TE", "K"]:
                    print("Enter a valid position")    
            name = input("Enter the players name: ")
            status = input("Enter the player's updated status(Healthy, Q, O): ")
            sqlcommands("UPDATE " + position + " SET Status = \'" + status + "\' WHERE NAME = \'" + name + "\';")
            print("Updated " + position + "s:")
            print_results("SELECT * FROM " + position + ";")
        
        if(choice == '3'):
            mname = input("Enter the manager's name: ")
            sqlcommands("INSERT INTO Roster SELECT q.Manager, q.Name, r.Name, w.Name, t.Name, d.Name, k.Name FROM QB q, RB r, WR w, TE t, DEF d, K k WHERE q.Manager = \'" + mname + "\' AND  r.Manager = \'" + mname + "\' AND  w.Manager = \'" + mname + "\' AND  t.Manager = \'" + mname + "\' AND  d.Manager = \'" + mname + "\' AND  k.Manager = \'" + mname + "\';" )
            print_results("SELECT * FROM Roster;")

        if(choice == '4'):
            position = ""
            while(position not in ["QB", "RB", "WR", "TE", "DEF", "K"] ):
                position = input("Select position of the player(QB, RB, WR, TE, DEF, K): ")    
                if position not in ["QB", "RB", "WR", "TE", "DEF", "K"]:
                    print("Enter a valid position")  
            name = input("Enter the name of the player you would like to drop: ")
            sqlcommands("UPDATE Roster SET " + position + " = 'None';")
            sqlcommands("UPDATE " + position + " SET Manager = 'None' WHERE Name = \'" + name + "\';")
            print("Updated " + position + "s:")
            print_results("SELECT * FROM " + position + ";")
        
        if(choice == '5'):
            position = ""
            while(position not in ["QB", "RB", "WR", "TE", "DEF", "K"] ):
                position = input("Select position of the player(QB, RB, WR, TE, DEF, K): ")    
                if position not in ["QB", "RB", "WR", "TE", "DEF", "K"]:
                    print("Enter a valid position")  
            print_results("SELECT * FROM " + position + " ORDER BY PositionRank LIMIT 5;")
        
        if(choice == '6'):
            name = input("Enter the manager's name: ")
            record = ""
            while("-" not in record):
                    record = input("Enter the record of this team: ")
                    if "-" not in record:
                        print("Please enter a valid record with a dash")
            score = -1
            while(score < 0.00):
                    score = float(input("Enter this team's total points for: "))
                    if score < 0.00:
                        print("Please enter a value greater than 0.0")
            sqlcommands("INSERT INTO TeamStats VALUES(\'" + name + "\', \'" + record + "\', " + str(score) +");")
            print("Updated Team Stats:")
            print_results("SELECT * FROM TeamStats;")
        
        if(choice == '7'):
            name = input("Enter the manager's name: ")
            record = ""
            while("-" not in record):
                    record = input("Enter this teams updated record: ")
                    if "-" not in record:
                        print("Please enter a valid record with a dash")
            score = -1
            while(score < 0.00):
                    score = float(input("Enter the updated total score for this team: "))
                    if score < 0.00:
                        print("Please enter a value greater than 0.0")
            
            sqlcommands("UPDATE TeamStats SET Record = \'" + record + "\', Score = " + str(score) + " WHERE Manager = \'" + name + "\';")
            print("Updated Team Stats:")
            print_results("SELECT * FROM TeamStats;")
        
        if(choice == '8'):
            curr = input("Enter the old manager's name: ")
            new = input("Enter the manager's updated name: ")
            sqlcommands("UPDATE TeamStats SET Manager = \'" + new + "\' WHERE Manager = \'" + curr + "\';")
            print("Updated Team Stats:")
            print_results("SELECT * FROM TeamStats;")

        if(choice == '9'):
            print_results("SELECT * FROM TeamStats ORDER BY Record DESC, Score DESC;")

        if(choice == '10'):
            position = ""
            while(position not in ["QB", "RB", "WR", "TE", "DEF", "K"] ):
                position = input("Select position of the player(QB, RB, WR, TE, DEF, K): ")    
                if position not in ["QB", "RB", "WR", "TE", "DEF", "K"]:
                    print("Enter a valid position")  
            nName = input("Enter the name of the player you would like to pick up: ")
            Manager = input("Enter the manager's name: ")
            oName = input("Enter the name of the player you would like to drop: ")

            try:
                cursor.execute("BEGIN TRANSACTION")
                cursor.execute("UPDATE " + position + " SET Manager = \'None\' WHERE name = \'" + oName + "\'")
                cursor.execute("UPDATE " + position + " SET Manager = \'" + Manager + "\' WHERE name = \'" + nName + "\'")
    
            except:
                cursor.execute("ROLLBACK;")
            
            else:
                cursor.execute("COMMIT;")
            
        if(choice == '11'):
            manager = input("Enter the manager's name whose team you would like to delete: ")
            sqlcommands("DELETE FROM TeamStats WHERE Manager = \'" + manager + "\';")
            print("Updated Team Stats:")
            print_results("SELECT * FROM TeamStats;")

        if(choice == '12'):
            break

        ask = input("Would you like to perform another action?(Y/N): ")
        while(ask not in ["Y", "N"]):
            ask = input("Would you like to perform another action?(Y/N): ")
    print("Thank you for using FantasyDB!")


if __name__ == "__main__":
    main()
