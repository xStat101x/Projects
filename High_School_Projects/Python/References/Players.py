from re import M


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print("Here are the first three players on my team:")
for player in players[:3]: # looping throught a slice
    print(player.title())
#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("my favorite foods are:")
print("my favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)