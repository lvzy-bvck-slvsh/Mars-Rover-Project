class Mars:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Rover:
	def __init__(self, x, y, orientation):
		self.x = x
		self.y = y
		self.orientation = orientation


def executeCommand(mars, rover, command):
	for i in range(0, len(command)):
		if command[i].upper() == "L":
			rover.orientation = setDirection(rover.orientation, "L")
		elif command[i].upper() == "R":
			rover.orientation = setDirection(rover.orientation, "R")
		elif command[i].upper() == "M":
			rover = moveRover(mars, rover)
		else:
			print(f'Invalid command : {command[i]}')
	return rover


def setDirection(ori, direction):
	if direction == "L":
		# Turn Left
		if ori == "N":
			return "W"
		elif ori == "E":
			return "N"
		elif ori == "S":
			return "E"
		elif ori == "W":
			return "S"
	elif direction == "R":
		# Turn Right
		if ori == "N":
			return "E"
		elif ori == "E":
			return "S"
		elif ori == "S":
			return "W"
		elif ori == "W":
			return "N"


def moveRover(mars, rover):
	if rover.orientation == "N":
		if rover.y < mars.y:
			rover.y = rover.y + 1
	elif rover.orientation == "E":
		if rover.x < mars.x:
			rover.x = rover.x + 1
	elif rover.orientation == "S":
		if rover.y > 0:
			rover.y = rover.y - 1
	elif rover.orientation == "W":
		if rover.x > 0:
			rover.x = rover.x - 1
	return rover


if __name__ == '__main__':
	Rovers = []
	rover = None
	mars = None

	nRovers = int(input("Enter number of Rovers : "))
	if nRovers < 1:
		print("Invalid number of rovers. Number of rovers needs to be greater than 0")
		exit()

	xmax, ymax = map(int, input("Enter size of Plateau (Separated by ' '): ").split())
	if xmax < 1:
		print("Invalid size of Mars. Length needs to be greater than 0")
		exit()

	if ymax < 1:
		print("Invalid size of Mars. Width needs to be greater than 0")
		exit()

	mars = Mars(xmax, ymax)
	for _ in range(nRovers):
		rx, ry, ro = input("Coordinates & Orientation for Rover %d : " % _).split()
		rx = int(rx)
		ry = int(ry)
		if rx < 0:
			print("Rover out of bounds. Invalid X-coordinate for Rover.")
			exit()
		if ry < 0:
			print("Rover out of bounds. Invalid Y-coordinate for Rover.")
			exit()
		if rx > xmax:
			print("Rover out of bounds. Invalid X-coordinate for Rover.")
			exit()
		elif ry > ymax:
			print("Rover out of bounds. Invalid Y-coordinate for Rover.")
			exit()


		if [rx, ry, ro] not in Rovers:
			rover = Rover(rx, ry, ro)
			command = input("Enter rover command : ")
			if len(command) < 0:
				print("No command entered.")
				exit()

			Rovers.append(executeCommand(mars, rover, command))
		else:
			print("Rover already exists here.")

	for i in Rovers:
		print(f'[{i.x} {i.y} {i.orientation}]')
