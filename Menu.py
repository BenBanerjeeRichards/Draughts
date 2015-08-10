import pygame

class Menu:

	def __init__(self, items, surface):
		self._surface = surface
		self._items = items
		self._visible = False
		self._item_positions = []

		# 1, 2, 3 ... N: Mouse hovering over item out of N items
		# -1: No hover event occuring
		self._hover_item = -1		

		pygame.font.init()
		self._font = pygame.font.SysFont("Courier New", 50, True)


		self._calculate_sizes()

	def show(self):
		self._visible = True

	def hide(self):
		self._visible = False

	def toggle(self):
		if self._visible:
			self._visible = False
		else:
			self._visible = True

	def is_visible(self):
		return self._visible

	def _calculate_sizes(self):
		screen_size = self._surface.get_size()
		width = int(screen_size[0] * 0.5)
		height = int(screen_size[1] * 0.6)

		x = int((screen_size[0] - width) / 2)
		y = int((screen_size[1] - height) / 2)

		self._box_dimentions = (width, height)
		self._box_pos = (x, y)

	def _draw_box(self):
		pygame.draw.rect(self._surface, (55, 55, 55), (self._box_pos[0], self._box_pos[1], self._box_dimentions[0], self._box_dimentions[1]), 0)

	def _draw_items(self):
		padding = 100
		width = self._box_dimentions[0]
		height = (self._box_dimentions[1] - padding) / len(self._items)
		
		# Needed later on for collision detection
		self._item_dimentions = (width, height)

		item_count = 0

		for item in self._items:
			text = None

			if (item_count + 1) == self._hover_item:
				text = self._font.render(item, 1, (0x66, 0xFF, 0x00))
			else:
				text = self._font.render(item, 1, (0xFF, 0x66, 0x00))

			size = self._font.size(item)
			
			x = ((width - size[0]) / 2) + self._box_pos[0]
			y = self._box_pos[1] + item_count * height + padding

			self._surface.blit(text, (x, y))
			
			item_count += 1
			self._item_positions.append((x, y))

	def coord_to_item(self, click_coord):
		item_count = 0

		for item_pos in self._item_positions:
			item_count += 1

			if click_coord[0] <= item_pos[0] or click_coord[0] >= self._item_dimentions[0] + item_pos[0]:
				continue
			if click_coord[1] <= item_pos[1] or click_coord[1] >= self._item_dimentions[1] + item_pos[1]:
				continue

			return item_count - 1
		return -1		# This can not be False because reasons

	def set_current_mouse_pos(self, pos):
		self._hover_item = self.coord_to_item(pos) + 1

	def render(self):
		if not self._visible:
			return

		self._draw_box()
		self._draw_items()

	def update(self):
		if not self._visible:
			return

