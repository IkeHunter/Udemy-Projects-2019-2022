import shelve
game = shelve.open("game")

loc = 1
while True:
    availableExits = ", ".join(game["locations"][loc]['exits'].keys())

    print(game["locations"][loc]['desc'])

    if loc == 0:
        break
    else:
        allExits = game["locations"][loc]['exits'].copy()
        allExits.update(game["locations"][loc]['namedExits'])

    direction = input("Available exits are " + availableExits + ": ").upper()
    print()
    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than one letter, so check vocab
        words = direction.split()
        for word in words:
            if word in game["vocabulary"]:
                direction = game["vocabulary"][word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")
game.close()
