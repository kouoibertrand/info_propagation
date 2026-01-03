import matplotlib.pyplot as plt

def plot_fraction(history):
    fractions = [(h == 1).mean() for h in history]
    plt.plot(fractions)
    plt.xlabel("Temps")
    plt.ylabel("Fraction informée")
    plt.savefig("fractions.png")
    plt.close()