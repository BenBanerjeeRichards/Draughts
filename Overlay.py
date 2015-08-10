import pygame
import Teams


class Overlay:

	def __init__(self, screen, board, timer_in_use):
		self._screen = screen

		# Stats are in the form men, king, score
		self._black_stats = [0, 0, 0]
		self._red_stats = [0, 0, 0]

		@property
		def current_team(self):
		    return self.current_team
		
		self.current_team = Teams.black()
		self._timer_in_use = timer_in_use
		
		self._timer_black = None
		self._timer_red = None
		self._board = board

		self._init_font()

	def _init_font(self):
		font = pygame.font.SysFont("Courier New", 35, True)
		self._sidebar_font = pygame.font.SysFont("Courier New", 25, True)
		self._sidebar_font_large = pygame.font.SysFont("Courier New", 28, True)

		turn_black = "Current Player: Black"
		turn_red = "Current Player: Red"

		self._turn_red_text = font.render(turn_red, 1, (0xFF, 0x00, 0x00))
		self._turn_black_text = font.render(turn_black, 1, (0x00, 0x00, 0x00))

		self._size_black_turn =  font.size(turn_black)
		self._size_red_turn =  font.size(turn_red)

	def set_stats(self, team, stats):
		
		if Teams.black() == team:
			self._black_stats = stats
		else:
			self._red_stats = stats

	def _draw_team_sidebar(self, team):
		text_title = None
		text_title_rendered = None
		stats = None

		if team == Teams.red():
			text_title = "Red Team"
			stats = self._red_stats
			start_x = self._board.get_padding()[0] + self._board.get_dimentions()[0]
		else:
			text_title = "Black Team"
			stats = self._black_stats
			start_x = 0

		text = [
			"Men     {}".format(stats[0]),
			"Kings   {}".format(stats[1]),
			"Score   {}".format(stats[2])
		]

		# Render ALL the things
		black = (0x00, 0x00, 0x00)
		grey = (0x44, 0x44, 0x44)

		title_rendered = self._sidebar_font_large.render(text_title, 1, black)
		text_rendered = []

		for item in text:
			text_rendered.append(self._sidebar_font.render(item, 1, grey))

		
		# Calculate the coordinates for everything		
		text_padding = 10
		title_text_size = self._sidebar_font_large.size(text_title)
		total_height =  sum(
							map(get_second, 
							map(self._sidebar_font.size, text))
						)
		total_height += title_text_size[1]
		total_height += text_padding * (len(text) + 1)

		total_width = title_text_size[0]

		top_x = start_x + int(0.1 * self._board.get_padding()[0])
		top_y = (self._board.get_dimentions()[1] - total_height) / 2
		self._screen.blit(title_rendered, (top_x, top_y))

		curr_y = top_y + title_text_size[1] + text_padding
		height = self._sidebar_font.size("aa")[1]

		for item in text_rendered:
			self._screen.blit(item, (top_x, curr_y))

			curr_y += text_padding + height

	def _draw_current_team(self):
		size = None
		text = None

		if self.current_team == Teams.black():
			size = self._size_black_turn
			text = self._turn_black_text
		else:
			size = self._size_red_turn
			text = self._turn_red_text

		padding = self._board.get_padding()[1]

		x = (self._screen.get_size()[0] - size[0]) / 2
		y = self._board.get_dimentions()[1] + padding + (size[1] - padding) / 2

		self._screen.blit(text, (x, y))

	def render(self):
		self._draw_current_team()
		self._draw_team_sidebar(Teams.red())
		self._draw_team_sidebar(Teams.black())

	def update(self):
		pass

def get_first(tur):
	return tur[0]


def get_second(tur):
	return tur[1]


