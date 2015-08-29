import pygame
import math
import Util
import Teams
import CheckerType

class Checker:

	def __init__(self, surface, game_board, resource):
		# Information is going to be stored with the checker
		self.location = None
		self.team = None
		self.type = None
		self.animation_done_callback = None
		self.remove_checker_location = None

		self._game_board = game_board
		self._surface = surface
		self.res = resource
		self._animation_running = False
		self._checker_coords = None

		self._util = Util.Util()

		self._load_resource()

	def __str__(self):
		return "{} Checker {}".format(Teams.to_string(self.team)[0].upper(), self.location)

	def __repr__(self):
		return self.__str__()

	@property
	def type(self):
		return self.type

	@type.setter
	def type(self, type):
		if type != CheckerType.men() and type != CheckerType.king():
			raise ValueError('Team must be provided')

		self.type = type

	@property
	def res(self):
		return self.res

	@res.setter
	def res(self, res):
		self.res = res

	@property
	def team(self):
		return self.team

	@team.setter
	def team(self, team):
		if team != Teams.red() and team != Teams.black():
			raise ValueError('Team must be provided')

		self.team = team

	@property
	def location(self):
		return self.location

	@location.setter
	def location(self, loc):
		if loc == None:
			raise ValueError('Location must not be null')
			return

		if len(loc) != 2:
			raise ValueError('Location must be a sequence of length 2')
			return

		self.location = loc

	def _load_resource(self):
		self._checker = pygame.image.load(self.res.res)

		# Resize the checker
		side_length = self._game_board.get_side_length()
		side_length -= int(0.1 * side_length)
		self._checker = pygame.transform.scale(self._checker, (side_length, side_length))


	def animate_move(self, new_location):
		self._prev_location = self.location

		self.location = new_location
		self._animation_running = True
		new_loc = self._game_board.square_to_coord(new_location)
		loc = self._game_board.square_to_coord(self._prev_location)

		self._change = [0, 0]
		self._change[0] = new_loc[0] - loc[0]
		self._change[1] = new_loc[1] - loc[1]
		
		if self._change[0] == 0:
			
			if self._change[1] > 0:
				self._angle = (math.pi / 2)
			else:
				self._angle = -(math.pi / 2)

		elif self._change[1] == 0:
			self._angle = 0
		else:
			self._angle = math.atan2(self._change[1] , self._change[0])
		
		self._delta = [math.cos(self._angle), math.sin(self._angle)]
		# Edge case
		if self._change[1] == 0 and self._change[0] < 0:
			self._delta[0] *= -1

		self._checker_coords = [loc[0], loc[1]]
		self._target_location = new_location
		self._target_coords = self._game_board.square_to_coord(self._target_location)
		self._total_distance = self._util.distance(self._checker_coords, self._target_coords)

	def update(self):
		if not self._animation_running:
			return 

		# Check if animation is finished
		loc = self._game_board.square_to_coord(self._target_location)
		tolerence = int(0.1 * self._game_board.get_side_length())

		if self._util.equal(self._checker_coords[0], loc[0], tolerence) and self._util.equal(self._checker_coords[1], loc[1], tolerence):
			self._animation_running = False
			self.location = self._target_location

			if not self.animation_done_callback == None:
				self.animation_done_callback()

			return

		# Acceleration
		distance =  self._total_distance - self._util.distance(self._checker_coords, self._target_coords)

		if (distance / self._total_distance) < 0.75:
			self._delta[0] += 0.05 * self._delta[0]
			self._delta[1] += 0.05 * self._delta[1]
		else:
			self._delta[0] -= 0.1 * self._delta[0] 
			self._delta[1] -= 0.1 * self._delta[1] 


		self._checker_coords[0] += self._delta[0]
		self._checker_coords[1] += self._delta[1]


	def render(self):
		if self.location == None:
			return

		loc = self._game_board.square_to_coord(self.location)
		if not self._animation_running:	
		
			x_diff = self._game_board.get_side_length() - self._checker.get_size()[0]
			y_diff = self._game_board.get_side_length() - self._checker.get_size()[1]

			self._surface.blit(self._checker, (loc[0] + (x_diff / 2), loc[1] + (y_diff / 2)))
		else:
			self._surface.blit(self._checker, (self._checker_coords[0], self._checker_coords[1]))