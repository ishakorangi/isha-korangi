games = []

while true:
     user_game = ("Enter a game,or press enter to stop")
     if user_game == "":
          break
     else:
          games.append(user_game)

print("your favourate games are:")
for game is games:
     print(game)
