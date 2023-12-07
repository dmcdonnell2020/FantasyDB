import mysql.connector

def CreateTables():
    connection = mysql.connector.connect(
    user='root', 
    password='fantasy',
    host='localhost',
    database = 'FantasyDB'
)
    
    cursor = connection.cursor()
    
   
    
    cursor.execute("CREATE TABLE IF NOT EXISTS TeamStats(Manager VARCHAR(30), Record VARCHAR(10), Score DECIMAL(6,2),PRIMARY KEY(Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Roster(Manager VARCHAR(30), QB VARCHAR(40), RB VARCHAR(40), WR VARCHAR(40), TE VARCHAR(40), DEF VARCHAR(20), K VARCHAR(40), PRIMARY KEY (Manager))")
    cursor.execute("CREATE TABLE IF NOT EXISTS QB(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name))")
    cursor.execute("CREATE TABLE IF NOT EXISTS RB(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name))")
    cursor.execute("CREATE TABLE IF NOT EXISTS WR(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name))")
    cursor.execute("CREATE TABLE IF NOT EXISTS TE(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name))")
    cursor.execute("CREATE TABLE IF NOT EXISTS DEF(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), PRIMARY KEY(Name))")
    cursor.execute("CREATE TABLE IF NOT EXISTS K(Name VARCHAR(40), Manager VARCHAR(30), PositionRank INT, Score DECIMAL(3, 1), PPG DECIMAL(3, 1), ProjPoints DECIMAL(3, 1), Status VARCHAR(20),TeamName VARCHAR(30), PRIMARY KEY(Name))")
    cursor.execute("INSERT IGNORE INTO TeamStats VALUES('Devin', '5-6', 1678.3);")
    cursor.execute("INSERT IGNORE INTO TeamStats VALUES('Cole', '6-5', 1768.3);")
    cursor.execute("INSERT IGNORE INTO TeamStats VALUES('Joe', '3-8', 1558.5);")
    cursor.execute("INSERT IGNORE INTO TeamStats VALUES('John', '8-3', 1868.7);")
    cursor.execute("INSERT IGNORE INTO QB VALUES('Joe Burrow', 'Devin', 1, 13.2, 14.3, 13.2, 'Healthy', 'Bengals');")
    cursor.execute("INSERT IGNORE INTO QB VALUES('Jalen Hurts', 'Joe', 2, 15.2, 24.3, 19.2, 'Healthy', 'Eagles');")
    cursor.execute("INSERT IGNORE INTO QB VALUES('Josh Allen', 'John', 3, 12.2, 15.3, 16.2, 'Healthy', 'Bills');")
    cursor.execute("INSERT IGNORE INTO QB VALUES('Lamar Jackson', 'Cole', 4, 17.2, 21.5, 19.2, 'Healthy', 'Ravens');")
    cursor.execute("INSERT IGNORE INTO QB VALUES('Kenny Picket', 'None', 13, 13.6, 16.3, 14.2, 'Healthy', 'Steelers');")
    cursor.execute("INSERT IGNORE INTO RB VALUES('Alvin Kamara', 'Devin', 5, 15.6, 14.3, 17.2, 'Healthy', 'Saints');")
    cursor.execute("INSERT IGNORE INTO RB VALUES('Najee Harris', 'Cole', 7, 14.7, 12.3, 15.2, 'Healthy', 'Steelers');")
    cursor.execute("INSERT IGNORE INTO RB VALUES('Deandre Swift', 'Joe', 3, 18.3, 16.7, 20.1, 'Healthy', 'Eagles');")
    cursor.execute("INSERT IGNORE INTO RB VALUES('David Montgomery', 'John', 2, 19.0, 16.4, 16.3, 'Healthy', 'Lions');")
    cursor.execute("INSERT IGNORE INTO RB VALUES('Nick Chubb', 'None', 14, 0.0, 19.5, 0.0, 'O', 'Browns');")
    cursor.execute("INSERT IGNORE INTO WR VALUES('Tyreek Hill', 'Devin', 1, 25.3, 19.3, 21.2, 'Healthy', 'Dolphins');")
    cursor.execute("INSERT IGNORE INTO WR VALUES('DJ Moore', 'Cole', 11, 16.7, 14.3, 17.2, 'Healthy', 'Bears');")
    cursor.execute("INSERT IGNORE INTO WR VALUES('Justin Jefferson', 'Joe', 22, 0.0, 16.7, 0.0, 'O', 'Vikings');")
    cursor.execute("INSERT IGNORE INTO WR VALUES('Nico Collins', 'John', 5, 17.0, 15.4, 18.3, 'Q', 'Texans');")
    cursor.execute("INSERT IGNORE INTO WR VALUES('George Pickens', 'None', 23, 13.4, 11.5, 15.2, 'Healthy', 'Steelers');")
    cursor.execute("INSERT IGNORE INTO TE VALUES('Travis Kelce', 'Devin', 3, 18.6, 15.3, 17.2, 'Healthy', 'Chiefs');")
    cursor.execute("INSERT IGNORE INTO TE VALUES('Darren Waller', 'Cole', 7, 14.7, 12.3, 13.2, 'Healthy', 'Giants');")
    cursor.execute("INSERT IGNORE INTO TE VALUES('George Kittle', 'Joe', 4, 14.3, 14.7, 13.1, 'Healthy', '49ers');")
    cursor.execute("INSERT IGNORE INTO TE VALUES('Mark Andrews', 'John', 2, 13.0, 13.4, 12.3, 'Healthy', 'Ravens');")
    cursor.execute("INSERT IGNORE INTO TE VALUES('Jake Ferguson', 'None', 12, 10.2, 9.5, 8, 'Q', 'Cowboys');")
    cursor.execute("INSERT IGNORE INTO DEF VALUES('Cowboys', 'Devin', 12, 10.2, 9.5, 8);")
    cursor.execute("INSERT IGNORE INTO DEF VALUES('Eagles', 'Cole', 9, 7, 9.1, 8);")
    cursor.execute("INSERT IGNORE INTO DEF VALUES('Steelers', 'Joe', 2, 10.2, 9, 8);")
    cursor.execute("INSERT IGNORE INTO DEF VALUES('Ravens', 'John', 8, 1, 5, 5);")
    cursor.execute("INSERT IGNORE INTO DEF VALUES('Browns', 'None', 3, 4, 9.5, 6);")
    cursor.execute("INSERT IGNORE INTO K VALUES('Harrison Butker', 'Devin', 1, 9.0, 8.0, 8.5, 'Healthy', 'Chiefs');")
    cursor.execute("INSERT IGNORE INTO K VALUES('Tyler Bass', 'Cole', 3, 6.0, 7.0, 8.0, 'Healthy', 'Bills');")
    cursor.execute("INSERT IGNORE INTO K VALUES('Chris Boswell', 'Joe', 5, 7.0, 7.0, 7.0, 'Healthy', 'Steelers');")
    cursor.execute("INSERT IGNORE INTO K VALUES('Justin Tucker', 'John', 7, 6.0, 7.0, 6.5, 'Healthy', 'Ravens');")
    cursor.execute("INSERT IGNORE INTO K VALUES('Evan Mcpherson', 'None', 9, 4.0, 6.0, 6.5, 'Healthy', 'Bengals');")
    
    connection.commit()
    connection.close()

def print_results(query):
    conn = mysql.connector.connect(
    user='root', 
    password='fantasy',
    host='localhost',
    database = 'FantasyDB'
)
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
    connection = mysql.connector.connect(
    user='root', 
    password='fantasy',
    host='localhost',
    database = 'FantasyDB'
)
    cursor = connection.cursor()
    cursor.execute(s)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def main():
    connection = mysql.connector.connect(
    user='root',  
    password='fantasy',
    host='localhost',
    database = 'FantasyDB'
)
    cursor = connection.cursor()
    CreateTables()
    
    print("Welcome to Fantasy DB!")
    ask = "Y"
    while(ask == "Y"):
        
        print("Select which feature you would like to use: ")
        choice = input(" (1) Insert a player into the database\n (2) Update a players injury status\n (3) Display a manager's roster\n (4) Delete a player from your roster\n (5) Display the top performers at a position\n (6) Insert your team statistics\n (7) Update another teams statistics\n (8) Update a Manager's Name\n (9) Display the current standings of your league\n (10) Add a Free Agent to your roster\n (11) Remove a team from the league \n (12) Quit\n SELECTION: ")
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
