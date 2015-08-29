import os

class Resource:

	def __init__(self, res):
		self.res = res

	@property
	def res(self):
		if not os.path.isfile(self.res):
			print "Resource " + self.res + " does not exist"

		return self.res