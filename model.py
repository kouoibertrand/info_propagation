import numpy as np

def step(states, graph, threshold):
    new_states = states.copy()

    for i in graph.nodes:
        if states[i] == 0:
            informed_neighbors = sum(
                states[j] == 1 for j in graph.neighbors(i)
            )
            if informed_neighbors >= threshold:
                new_states[i] = 1

    return new_states