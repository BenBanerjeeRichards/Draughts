import Teams
import CheckerType


def get_possible_moves(state, team):
	enemy = Teams.opposite(team)
	direction = Teams.direction(team)
	king_row = None

	if direction < 0:
		king_row = 7
	else:
		king_row = 0

	ret_coord = []
	for checker in state.get_team_checkers(team):
		if checker.type == CheckerType.king():
			direction = 0

		moves = _find_moves(state, checker, direction, king_row)
		if len(moves[0]) == 0:
			continue

		if not moves[1]:
			for move in moves[0]:
				ret_coord.append([checker, move])
		else:
			# Handle multiple jumps
			current_place = moves[0][0]
			coord_history = [checker[1], current_place]

			while not current_place[0] == king_row:
				
				new_moves = _find_moves(state, current_place, direction, team, king_row)

				# PEP8 violation, but this is far more readable than 'if not new_moves'
				if new_moves == []:
					break

				if new_moves[1]:
					coord_history.append(new_moves[0][0])
					current_place = new_moves[0][0]
				else:
					break

			ret_coord.append(coord_history)

	return ret_coord



	
def _find_moves(state, checker, direction, king_row):
	empty_moves = []
	take_moves = []

	enemy = Teams.opposite(checker.team)
	diagonals = _get_diagonals(checker.location, direction)

	for square in diagonals:
		checker = state.get_checker_from_location(tuple(square))

		if checker == None:
			empty_moves.append(square)
		elif checker.team == enemy:					# TODO fix this
			dx = square[0] - checker.location[0]
			dy = square[1] - checker.location[1]

			new_square = (square[0] + dx, square[1] + dy)
			
			if not _valid_square(new_square):
				continue
			if checker == None:
				take_moves.append(new_square)
			
	if not len(take_moves) == 0:
		return (take_moves, True)
	return (empty_moves, False)



def _get_diagonals(square, y_restrict):
	# y_restrict: -1 implies that y can only decrease from that given in square [max 2 diagonals]
	# 			   0 that y can increase and decrease [max 4 diagonals]
	#			   1 that y can increase [max 2 diagonals]
	coords = []

	c1 = [square[0] + 1, square[1] + 1]
	c2 = [square[0] - 1, square[1] + 1]

	c3 = [square[0] + 1, square[1] - 1]
	c4 = [square[0] - 1, square[1] - 1]

	if _valid_square(c1) and y_restrict >= 0:
		coords.append(c1)
	if _valid_square(c2) and y_restrict >= 0:
		coords.append(c2)
	if _valid_square(c3) and y_restrict <= 0:
		coords.append(c3)
	if _valid_square(c4) and y_restrict <= 0:
		coords.append(c4)

	return coords

def _valid_square(square):
	if square[0] < 0 or square[1] < 0:
		return False

	if square[0] > 7 or square[1] > 7:
		return False

	return True