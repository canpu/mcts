from gomoku import *
from mcts import *

# We create an example game; in this game, the black has taken great advantage
initial_state = GomokuState(use_default_heuristics=True)
initial_state.go((3, 5)).go((3, 6)).go((4, 6)).go((5, 7)).go((5, 5)) \
    .go((6, 4)).go((4, 5)).go((6, 5)).go((4, 4)).go((4, 7)).go((6, 6)) \
    .go((7, 7)).go((2, 5)).go((1, 5)).go((3, 3)).go((2, 2)).go((6, 7)) \
    .go((3, 4))

# This is a strategy for the black to win
suggested_state = initial_state.__copy__()
suggested_state.go((4, 3)).go((4, 2)).go((5, 3)).go((6, 3)).go((6, 2)).go((2, 6)) \
    .go((7, 1))

# Simulate a game using MCTS
state = initial_state.__copy__()
while not state.is_terminal:
    # TODO
    # Black goes

    # White goes
    break


A = Node(state)
B = Node(state.__copy__().go((0, 0)))
C = Node(state.__copy__().go((0, 1)))
A.add_child(GomokuAction(0, (0, 0)), B)
B.add_child(GomokuAction(0, (0, 0)), C)
B.__del__()
print(A.children)


mcts = MonteCarloSearchTree(samples=200)
action = mcts.search_for_action(initial_state)
print(action)
