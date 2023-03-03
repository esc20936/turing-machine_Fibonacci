from tm import *
import sys

def createMachine():

	f = open(sys.argv[1], "r")

	nStates, nTransitions = map(int, f.readline().strip().split())
	machine = TuringMachine()

	#lee los estados
	for i in range (0, nStates):
		line = f.readline().strip().split()
		value = line[0]
		state = State(value)
		machine.addState(state)

	#lee las transiciones
	for i in range (0, nTransitions):
		line = f.readline().strip().split()

		# source = line[0]
		# destination = line[1]
		# read = line[2]
		# write = line[3]
		# direction = Transition.Direction.RIGHT if line[4] == 'R' else Transition.Direction.LEFT

		source = line[0]
		read = line[1]
		destination = line[2]
		write = line[3]
		direction = Transition.Direction.RIGHT if line[4] == 'R' else Transition.Direction.LEFT if line[4] == 'L' else Transition.Direction.NONE

		transition = Transition(read, write, machine.getState(destination), direction)
		machine.addTransition(source, transition)
		
	#lee el estado inicial
	initialState = f.readline().strip()
	machine.setInitState(initialState)

	return machine

def readTape():
	f = open(sys.argv[2], "r")

	string = f.readline().strip()
	tape = Tape(string)

	return tape

if __name__ == "__main__":
	#lee el archivo y crea la maquina
	machine = createMachine()
	#lee la cinta
	tape = readTape()
	machine.setTape(tape)
	#simular
	machine.simulate()
	print(tape.cells)
	cells = tape.cells
	cont = 0
	for i in range(0, len(cells)):
		if cells[i] == '0':
			cont+=1
	print(f"Res {cont}")
