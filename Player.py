class HumanPlayer:

    def __init__(self, team):
        self._team = team
        self._clicks = []

    def add_move(self, coord):
        self._clicks.append(coord)

    def confirm(self):
        print self._clicks
        self._clicks = []

class AIPlayer:

    def __init__(self, team):
        self._team = team
