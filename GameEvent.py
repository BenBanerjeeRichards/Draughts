class GameEvent:

    def __init__(self):
        self.start = None
        self.end = None
        self.delete_pos = None

    def move(self, start, end):
        self.start = start
        self.end = end
        self.delete_pos = None  # Just to be sure

    def delete(self, coord):
        self.delete_pos = coord
        self.start = self.end = None

    def __repr__(self):
        if self.delete_pos:
            return "Delete {}".format(self.delete_pos)
        else:
            return "Move {}->{}".format(self.start, self.end)

    def __str__(self):
        return self.__repr__()