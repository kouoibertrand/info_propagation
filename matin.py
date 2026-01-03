import numpy as np
import networkx as nx
from model import step
from metrics import fraction_informed
from visualize import plot_fraction

N = 100
threshold = 2
T = 50

graph = nx.erdos_renyi_graph(N, 0.05)
states = np.zeros(N, dtype=int)

# graine initiale
states[np.random.choice(N, 3, replace=False)] = 1

history = [states.copy()]

for _ in range(T):
    states = step(states, graph, threshold)
    history.append(states.copy())

#print("Fraction informée finale :", states.mean())

#print(fraction_informed(states))

#fractions = [(h == 1).mean() for h in history]
#import matplotlib.pyplot as plt
#plt.plot(fractions)
#plt.show()
plot_fraction(history)