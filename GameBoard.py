import pygame
import math
import pygame 

class GameBoard():

	def __init__(self, surface, dim):
		self._dim = dim
		self._surface = surface;
		self._calculate_sizes()
		self._squares_highlighted = []



	def _calculate_sizes(self):
		# Finds all of the padding and box dimentions for the surface size

		if self._dim[0] == 0 or self._dim[1] == 0:
			print "Dim can't be zero"
			return

		if len(self._dim) != 2:
			print "Dim size must be 2"


		width_side = math.ceil((self._surface.get_size()[0] - 700) / self._dim[0])
		height_side = math.ceil((self._surface.get_size()[1] - 100) / self._dim[1])

		self._side_length = int(min(width_side, height_side))
		
		self._padding_width = int((self._surface.get_size()[0] - (self._side_length * self._dim[0]))/2)
		self._padding_height = int((self._surface.get_size()[1] - (self._side_length * self._dim[1]))/2)

	def render(self):
		# IF odd row, then every odd col gets coloured, otherwise every even col gets coloured 
		# Hence, creating a checkerboard 

		for row in range(self._dim[1]):
			
			for col in range(self._dim[0]):

				if (row % 2) == 0:

					if (col % 2) == 0:
						self._draw_square(col, row)
				else:
					if not (col % 2) == 0:
						self._draw_square(col, row)

		self._draw_border()

		for square in self._squares_highlighted:
			self._draw_highlight(square)


	def _draw_square(self, col, row):
		x = self._padding_width + col * self._side_length
		y = self._padding_height + row * self._side_length

		pygame.draw.rect(self._surface, (0, 0, 0), (x, y, self._side_length, self._side_length), 0)

	def _draw_border(self):
		width = self._side_length * self._dim[0]
		height = self._side_length * self._dim[1]
		x = self._padding_width
		y = self._padding_height

		pygame.draw.rect(self._surface, (0, 0, 0), (x, y, width, height), 2)

	def _draw_highlight(self, square):
		HIGHLIGHT_BORDER = 6

		rect1_height = self._side_length
		rect1_width = HIGHLIGHT_BORDER
		rect1_x = self._padding_width + square[0] * self._side_length
		rect1_y = self._padding_height + square[1] * self._side_length
		
		pygame.draw.rect(self._surface, (255, 0, 0), (rect1_x, rect1_y, rect1_width, rect1_height), 0)
		pygame.draw.rect(self._surface, (255, 0, 0), (rect1_x + (self._side_length - HIGHLIGHT_BORDER), rect1_y, rect1_width, rect1_height), 0)


		rect2_height = HIGHLIGHT_BORDER
		rect2_width = self._side_length - 2 * HIGHLIGHT_BORDER
		rect2_x = rect1_x + HIGHLIGHT_BORDER
		rect2_y = rect1_y

		pygame.draw.rect(self._surface, (255, 0, 0), (rect2_x, rect2_y, rect2_width, rect2_height), 0)
		pygame.draw.rect(self._surface, (255, 0, 0), (rect2_x, rect2_y + (self._side_length - HIGHLIGHT_BORDER), rect2_width, rect2_height), 0)


	def coord_to_square(self, coord):
		# Converts a click on the screen to a squre
		if len(coord) != 2:
			print "Coord must have size of 2"
			return None

		if coord[0] - self._padding_width < 0 or coord[1] - self._padding_height < 0:
			return None

		if coord[0] > self._padding_width + self._dim[0] * self._side_length:
			return None
		
		if coord[1] > self._padding_height + self._dim[1] * self._side_length:
			return None

		# If program gets here, click was on board

		x = coord[0] - self._padding_width
		y = coord[1] - self._padding_height

		return (x / self._side_length, y / self._side_length)

	def add_square_highlight(self, square):
		self._squares_highlighted.append(square)

	def clear_highlighted(self):
		self._squares_highlighted = []

	def remove_cells_highlighted(self, square):
		index = 0

		for sq in self._squares_highlighted:
			if sq == square:
				break

			index += 1

		self._squares_highlighted.pop(index)

	def square_to_coord(self, square):
		if len(square) != 2:
			print "Square must have len 2"
			return 

		x = square[0] * self._side_length + self._padding_width
		y = square[1] * self._side_length + self._padding_height

		return (x, y)

	def get_side_length(self):
		return self._side_length

	def get_dimentions(self):
		return (self._side_length * self._dim[0], self._side_length * self._dim[1])

	def get_padding(self):
		return (self._padding_width, self._padding_height) 