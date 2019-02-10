# "Find The Treasure" is a simple adventure game where the player must find the
# treasure to win the game. The player must go through a series of rooms inside
# an abandoned house to retrieve it. Player will be have to enter where he or she
# navigates to find the treasure.

locations = {0: "You're now outside of the mansion. Goodbye.",
             1: "You're now in the hallway of the mansion.",
             2: "You're now in the kitchen",
             3: "You're now in the bathroom",
             4: "You're now in the living room",
             5: "You're now in the 2nd Floor",
             6: "You're now in the Blue Room.",
             7: "You're now in the Red Room",
             8: "You're now in the Dungeon",
             9: "You're now in the Yellow Room",
             10: "You're now in the 1st floor",
             11: "You found the treasure!",}

exits = {0: {"Outside": 0},
         1: {"Outside": 0, "Kitchen": 2, "Bathroom": 3, "Living Room": 4, "2nd Floor": 5},
         2: {"Living Room": 4, "Hallway": 1},
         3: {"Hallway": 1},
         4: {"Kitchen": 2, "Hallway": 1},
         5: {"Blue": 6, "Red": 7, "Yellow": 9, "1st Floor": 10},
         6: {"2nd Floor": 5},
         7: {"Dungeon": 8, "2nd Floor": 5},
         8: {"Outside": 0},
         9: {"Treasure": 11, "2nd Floor": 5},
         10: {"Hallway": 1},
         11: {"Treasure": 11}}

vocabulary = {"Outside": "Outside",
              "Hallway": "Hallway",
              "Kitchen": "Kitchen",
              "Bathroom": "Bathroom",
              "Living Room": "Living Room",
              "2nd Floor": "2nd Floor",
              "Blue": "Blue",
              "Red": "Red",
              "Dungeon": "Dungeon",
              "Yellow": "Yellow",
              "1st Floor": "1st Floor",
              "Treasure": "Treasure",
              }

loc = 1

while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        break

    direction = input("Available exits are " + availableExits)
    print()
    # Parse the user input, using our vocabulary dictionary if necessary
    # Also, searches through user's input for key words for optimization
    # if len(direction) > 1: # more than one letter, check vocabulary
    words = direction.split()
    # if word in user input
    for word in words:
        if word in vocabulary:
            direction = vocabulary[word]

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction.")







