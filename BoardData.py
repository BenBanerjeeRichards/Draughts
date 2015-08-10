class BoardData:

	def __init__(self):
		self._board = [[],[],[],[],[],[],[],[]]

		for i in range(8):
			for j in range(8):
				self._board[i].append(0)


	def print_board(self):
		# Debug function
		for i in range(8):
			print self._board[i]

	def get_data(self, coord):
		return self._board[coord[0]][coord[1]]

	def set_data(self, (coord), data):
		self._board[coord[0]][coord[1]] = data
