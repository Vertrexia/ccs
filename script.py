import sys
import classes
import functions

for line in sys.stdin:
    if line.startswith("PLAYER_ENTERED") or line.startswith("PLAYER_AI_ENTERED"):
        lineExt = line.split(" ")
        functions.playerEntered(lineExt[1])

    elif line.startswith("PLAYER_LEFT") or line.startswith("PLAYER_AI_LEFT"):
        lineExt = line.split(" ")