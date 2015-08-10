import math

class Util:

	def __init__(self):
		pass

	def equal(self, num1, num2, tolerence):
		return abs(num1 - num2) <= tolerence

	def distance(self, point1, point2):
		if point1 == None or point2 == None:
			print "Points must not be None"
			return 
		if len(point1) != 2or len(point2) != 2:
			print "Points must have two values"
			return


		x = math.pow(point1[0] - point2[0], 2)
		y = math.pow(point1[1] - point2[1], 2)
		return math.sqrt(abs(x+y));
