import GameMode
import GameAnalyser
import Teams

class Game:

    def __init__(self, state, board):
        self.mode = None
        self._state = state
        self._board_ui = board

        self.current_clicks = []
        self.current_team = Teams.black()

    def new_game(self, mode):
        self.mode = mode
        self.current_team = Teams.black()

    def left_click(self, coord):
        if self._is_human_player():
            self.current_clicks.append(coord)
            self._board_ui.add_square_highlight(coord)

    def right_click(self):
        if self._is_human_player():
            if len(self.current_clicks) <= 1:
                return

            deleted = GameAnalyser.check_move_is_valid(self.current_clicks,  self._state, self.current_team)

            if deleted == False:
                 self.current_clicks = []
                 self._board_ui.clear_highlighted()

            while (len(self.current_clicks)) > 1:
                start = self.current_clicks[0]
                end = self.current_clicks[1]

                if len(deleted) > 0:
                    self._state.move_checker(start, end)
                    self._state.remove_checker(deleted[0])
                    del deleted[0]
                else:
                    self._state.move_checker(start, end)

                del self.current_clicks[0]

            if not deleted == False:
                self.current_team = Teams.opposite(self.current_team)
            self.current_clicks = []
            self._board_ui.clear_highlighted()

    def _is_human_player(self):
        if self.current_team == Teams.black():
            return True

        # Previous condition => the team is red -> only human if in PvP
        return self.mode == GameMode.player_v_player()


