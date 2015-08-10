def red():
	return 1 

def black():
	return 2

def black_direction():
	return -1

def red_direction():
	return 1

def to_string(team):
	if team == red():
		return "red"
	if team == black():
		return "black"
	return "unknown"

def direction(team):
	if team == red():
		return red_direction()
	return black_direction()

def opposite(team):
	if team == red():
		return black()
	return red()