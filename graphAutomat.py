from graphviz import Digraph

add =[
["q0", "0", "q1", "X", "R"],
["q0", "c", "q5", "B", "R"],
["q1", "0", "q1", "0", "R"],
["q1", "c", "q2", "c", "R"],
["q2", "0", "q2", "0", "R"],
["q2", "B", "q3", "0", "L"],
["q3", "0", "q3", "0", "L"],
["q3", "c", "q4", "c", "L"],
["q4", "0", "q4", "0", "L"],
["q4", "X", "q0", "X", "R"],
["q5", "0", "q5", "0", "R"],
["q5", "c", "q5", "c", "R"],
["q5", "B", "q5", "B", "R"],
["q5", "X", "q5", "X", "R"],
]
estadosAdd = ["q0", "q1", "q2", "q3", "q4", "q5"]
def graphAutomata(states, transitionsA, name="automata.gv"):
    g = Digraph('G', filename=name, format='png')
    g.attr(rankdir='LR', size='80,5')
    # print(transitions)
    cont = 0
    for state in states:
        if cont == 0:
            g.attr('node', shape='doublecircle')
            cont += 1
        else:
            g.attr('node', shape='circle')
        g.node(state)

    for transition in transitionsA:
        g.edge(transition[0], transition[2], label=f"{transition[1]}, {transition[3]}/{transition[4]}")
    g.view()
      
graphAutomata(estadosAdd, add)