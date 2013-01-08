import classes
import math

#   checks if players exist in the list
def playerExists(name):
    for key in classes.players_:
        player = classes.players_[key]

        if player.name == name:
            return True
    return False

#   player entered the server
def playerEntered(name):
    if playerExists(name) == False:
        classes.players_[classes.pCounter] = classes.Player()
        player = classes.players_[classes.pCounter]

        player.name = name

        classes.pCounter += 1

def getPlayer(name):
    if name != "":
        for key in classes.players_:
            player = classes.players_[key]

            if player.name == name:
                return player
    return False

#   player left the server
def playerLeft(name):
    if playerExists(name) == True:
        player = getPlayer(name)

        if player != False:
            player.isAlive = False