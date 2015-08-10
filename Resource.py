import os

class Resource:

	def __init__(self, res):
		self._res = res

	def get_resource(self):
		# Note: Potential race condition, but 'good enough'
		# Worst case is that the program crashes

		if not os.path.isfile(self._res):
			print "Resource " + self._res + " does not exist"

		return self._res