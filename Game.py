import GameMode
import Player
import Teams

class Game:

    def __init__(self):
        self.player1 = None
        self.player1 = None

    def new_game(self, mode):
        self.player1 = Player.HumanPlayer(Teams.black())

        if mode == GameMode.player_v_player():
            self.player2 = Player.HumanPlayer(Teams.red())
        else:
            self.player2 = Player.AIPlayer(Teams.red())

        self.current_team = Teams.black()

    def left_click(self, coord):
        if self.current_team == Teams.black():
            self.player1.add_move(coord)

        if self.current_team == Teams.red() and self.mode == GameMode.player_v_player():
            self.player2.add_move(coord)

    def right_click(self):
        if self.current_team == Teams.black():
            self.player1.confirm()

        if self.current_team == Teams.red() and self.mode == GameMode.player_v_player():
            self.player2.confirm()




