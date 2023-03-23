import mysql.connector
import tkinter as tk

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="register"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM result")

myresult = mycursor.fetchall()

team_dict = {}

for x in myresult:
    home_team = x[0]
    away_team = x[1]
    home_score = x[2]
    away_score = x[3]
    if home_score > away_score:
        if home_team not in team_dict:
            team_dict[home_team] = [1, 1, 0, 0, 3]
        else:
            team_dict[home_team][0] += 1
            team_dict[home_team][1] += 1
            team_dict[home_team][4] += 3
        if away_team not in team_dict:
            team_dict[away_team] = [1, 0, 0, 1, 0]
        else:
            team_dict[away_team][0] += 1
            team_dict[away_team][3] += 1
    elif home_score < away_score:
        if away_team not in team_dict:
            team_dict[away_team] = [1, 1, 0, 0, 3]
        else:
            team_dict[away_team][0] += 1
            team_dict[away_team][1] += 1
            team_dict[away_team][4] += 3
        if home_team not in team_dict:
            team_dict[home_team] = [1, 0, 0, 1, 0]
        else:
            team_dict[home_team][0] += 1
            team_dict[home_team][3] += 1
    else:
        if home_team not in team_dict:
            team_dict[home_team] = [1, 0, 1, 0, 1]
        else:
            team_dict[home_team][0] += 1
            team_dict[home_team][2] += 1
            team_dict[home_team][4] += 1
        if away_team not in team_dict:
            team_dict[away_team] = [1, 0, 1, 0, 1]
        else:
            team_dict[away_team][0] += 1
            team_dict[away_team][2] += 1
            team_dict[away_team][4] += 1

for team in team_dict:
    team_dict[team][0] = team_dict[team][1] + team_dict[team][2] + team_dict[team][3]

sorted_teams = sorted(team_dict.items(), key=lambda x: x[1][4], reverse=True)

root = tk.Tk()
root.geometry("500x400")

label = tk.Label(root, text="{:<15} {:<10} {:<10} {:<10} {:<10}".format("Team", "Played", "Won", "Lost", "Points"), font=("Arial", 12, "bold"), borderwidth=2, relief="groove")
label.grid(row=0, column=0, sticky="w")

for i, team in enumerate(sorted_teams):
    label = tk.Label(root, text="{:<15} {:<15} {:<15} {:<15} {:<15}".format(team[0], team[1][0], team[1][1], team[1][3], team[1][4]), font=("Arial", 12), borderwidth=2, relief="groove")
    label.grid(row=i+1, column=0, sticky="w")

root.mainloop()