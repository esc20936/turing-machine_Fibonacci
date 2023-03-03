#python3
import enum
class State():
	def __init__(self, value):
		self.value = value
		self.transitions = {}

	def addTransition(self, transition):
		self.transitions[transition.read] = transition

	def step(self, symbol):
		try:
			transition = self.transitions[symbol]
			return transition.nextState, transition.write, transition.direction
		except KeyError as e:
			return self, None, None

class Transition():
	class Direction(enum.Enum):
		RIGHT = 1
		LEFT  = 2
		NONE = 3

	def __init__(self, read, write, nextState, direction):
		self.read      = read
		self.write     = write
		self.nextState = nextState
		self.direction = direction

class Tape():
	def __init__(self, cells):
		cont = 0
		for i in range(len(cells)):
			if cells[i] == '0':
				cont += 1
		res=self.get_last_two_fibonacci_numbers(cont)
		n1 = res[0]
		n2 = res[1]
		tapeCells = '0'*n1 +"c"+ '0'*n2+"B"*100
		self.cells    = tapeCells
		self.position = 0
	def get_last_two_fibonacci_numbers(self,n):
		if n <= 1:
			return (0, 1) if n == 1 else (1, 0)
		else:
			fib_n_minus_1, fib_n_minus_2 = self.get_last_two_fibonacci_numbers(n-1)
			fib_n = fib_n_minus_1 + fib_n_minus_2
			return fib_n_minus_2, fib_n

	def reachEnd(self):
		return self.position < 0 or self.position >= len(self.cells)

	def head(self):
		if self.reachEnd():
			return -1
		return self.cells[self.position]

	def reset (self):
		self.position = 0

	def headPosition(self):
		return self.position

	def writeOnPosition(self, symbol):
		pos = self.position
		self.cells = self.cells[:pos] + symbol + self.cells[pos + 1:]
	
	def update(self, toWrite, direction):
		if self.reachEnd():
			raise Exception('End of computation.')
		self.writeOnPosition(toWrite)
		if direction == Transition.Direction.RIGHT:
			self.position += 1
		elif direction == Transition.Direction.LEFT:
			self.position -= 1
		elif direction == Transition.Direction.NONE:
			pass



class TuringMachine():
	def __init__(self):
		self.states = {}
		self.currentState = None
		self.tape = None
		self.visited = set()
		self.simulating = True
		self.initialState = None

	def addState(self, state):
		self.states[state.value] = state

	def addTransition(self, sourceState, transition):
		self.states[sourceState].addTransition(transition)

	def setInitState (self, state):
		self.currentState = self.states[state]
		self.initialState = self.states[state]

	def setTape (self, tp):
		self.tape = tp

	def startOver(self):
		self.currentState = self.initialState
		self.tape.reset()
		self.simulating = True
		self.visited = {(self.currentState.value, self.tape.headPosition())}
		log = "State:" + "(%3s) "%(self.currentState.value)
		log += self.tape.cells + "\n" + "            "
		log += " " * self.tape.headPosition() + "^\n"
		return log

	def getState (self, stateValue):
		return self.states[stateValue]

	def simulateStep(self):
		if not self.simulating:
			return "Stop.\n"
		self.currentState, toWrite, self.direction = self.currentState.step(self.tape.head())
		if toWrite:
			self.tape.update(toWrite, self.direction)
		if toWrite == None or self.tape.reachEnd():
			self.simulating = False
			return "\nFin\n"
		else:
			log = "State:" + "(%3s) "%(self.currentState.value)
			log += self.tape.cells + "\n" + "            "
			log += " " * self.tape.headPosition() + "^\n"
			return log

	def simulate(self):
		f = open("log.txt", "a")
		f.write("Inicio\n\n")
		f.write(self.startOver())
		while self.simulating:
			logEntry = self.simulateStep()
			f.write(logEntry);
		f.write("--------------------------------------\n")

