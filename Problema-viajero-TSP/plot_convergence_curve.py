import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class plot_convergence_curve:
    def plot_convergence_curve(fitness_history, p, alg):
        efos = np.arange(len(fitness_history))
        plt.title("Convergence curve for " + str(p))
        plt.xlabel("EFOs")
        plt.ylabel("Fitness")
        plt.plot(efos, fitness_history, label=str(alg))
        plt.legend()
        plt.show()

    # Plot convergence curve comparison for two or more algorithms
    def plot_convergence_curve_comparison(fitness_history, p, alg):
        efos = np.arange(len(fitness_history[0]))
        plt.title("Convergence curve for " + str(p))
        plt.xlabel("EFOs")
        plt.ylabel("Fitness")
        algorithms = len(fitness_history)
        for a in range(algorithms):
            plt.plot(efos, fitness_history[a], label=str(alg[a]))
        plt.legend()
        plt.show()

    def print_alorithms_with_avg_fitness(alg, avg_fitness):
        rows = len(alg)
        for r in range(rows):
            print(alg[r] + " {0:12.6f}".format(avg_fitness[r]))