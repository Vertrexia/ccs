import time

class Timer:
    start = 0.0
    stop = 0.0

    isRunning = False

    def Start(self):
        self.start = round(time.time(), 4)

    def Stop(self):
        self.stop = round(time.time(), 4)

    def GameTimer(self):
        gametimer = round(time.timer() - self.start, 4)
        return gametimer

    def Elapsed(self):
        elapsed = stop - start
        return elapsed

class Player:
    name = ""

    rounds = 0
    matchs = 0

    has_killed      = 0
    been_killed     = 0
    done_suicide    = 0
    has_teamkilled  = 0
    been_teamkilled = 0

    current_has_killed      = 0
    current_been_killed     = 0
    current_done_suicide    = 0
    current_has_teamkilled  = 0
    current_been_teamkilled = 0

    bestTimeAlive       = 0
    currentTimeAlive    = 0

    isAlive = False

players_ = {}
pCounter = 0

gameTimer = Timer()