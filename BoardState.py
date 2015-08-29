import GameEvent
import CheckerType
import Resource

class InvalidGameEventError(Exception):
	def __init__(self):
		pass


class BoardState:

	def __init__(self, board):
		self._board = board

		self.checkers = []
		self._game_event_backlog = []
		self.event_running = False

	@property
	def checkers(self):
		return self.checkers

	def add_checker(self, checker):
		self.checkers.append(checker)

	# FIXME change method name
	def event_completed(self):
		self.event_running = False

		if len(self._game_event_backlog) > 0:
			event = self._game_event_backlog[0]
			del self._game_event_backlog[0]

			if not event:
				raise Exception("ERROR ERROR ERROR ")
			self._run_event(event)

	def _run_event(self, event):
		if not event.delete_pos:
			checker = self.get_checker_from_location(event.start)
			checker.animation_done_callback = self.event_completed

			if not event.start or not event.end:
				raise InvalidGameEventError("Event must be a delete event or move event")

			checker = self.get_checker_from_location(event.start)
			checker.animate_move(event.end)
			self.event_running = True

		else:
			index = self._get_checker_index_from_location(event.delete_pos)
			del self.checkers[index]
			self.event_completed()


	def move_checker(self, start_location, end_location):
		self.king_checker(start_location)
		event = GameEvent.GameEvent()
		event.move(start_location, end_location)
		self._game_event_backlog.append(event)

		if not self.event_running:
			self.event_completed()


	def remove_checker(self, location):
		event = GameEvent.GameEvent()
		event.delete(location)
		self._game_event_backlog.append(event)
		if not self.event_running:
			self.event_completed()


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

	def king_checker(self, location):
		index = self._get_checker_index_from_location(location)
		checker = self.get_checker_from_location(location)
		if not checker:
			raise ValueError('No checker exists at given location')


		if checker.type == CheckerType.king():
			return

		checker.type = CheckerType.king()
		current_res = checker.res.res
		new_res = Resource.Resource(current_res.replace(".png", "_king.png"))
		checker.res = new_res
		checker._load_resource()
		self.checkers[index] = checker



