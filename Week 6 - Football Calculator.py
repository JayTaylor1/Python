season = 5
wins = 0
draws = 0
losses = 0
points = 0

team_name = input("Enter the Team Name:                      ")
for game in range(1, season + 1):
    scored = input("Goals Scored in match  #" + str(game) + ":     ")
    conceded = input("Goals Against in match #" + str(game) + ":     ")
    if scored > conceded:
        wins += 1
        points += 3
    elif scored < conceded:
        losses += 1
    else:
        draws += 1
        points += 1

print(team_name.title())
print("Wins:    " + str(wins))
print("Draws:   " + str(draws))
print("Losses:  " + str(losses))
print("Points:  " + str(points))



