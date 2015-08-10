import Teams
import CheckerType

class BoardState:

	def __init__(self, board):
		self._board = board

		self.checkers = []

	@property
	def checkers(self):
		return self.checkers

	def add_checker(self, checker):
		self.checkers.append(checker)

	def remove_checker(self, location):
		index = self._get_checker_index_from_location(location)
		del self.checkers[index]

	def move_checker(self, start_location, end_location):
		checker = self.get_checker_from_location(start_location)
		checker.animate_move(end_location)


	def get_team_checkers(self, team):
		team_checkers = []
		for checker in self.checkers:
			if checker.team == team:
				team_checkers.append(checker)

		return team_checkers

	def _get_checker_index_from_location(self, location):
		current_index = 0

		for checker in self.checkers:
			if checker.location == location:
				return current_index

			current_index += 1

		return None

	def get_checker_from_location(self, location):
		index = self._get_checker_index_from_location(location)
		if index == None:
			return None

		return self.checkers[index]

