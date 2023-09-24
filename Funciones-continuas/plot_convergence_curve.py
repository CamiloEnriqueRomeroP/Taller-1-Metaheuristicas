import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class plot_convergence_curve:
    # Plot convergence curve    
    
    def plot_convergence_curve(fitness_history, f, names_alg, num_f, bw, max_local):
        efos = np.arange(len(fitness_history))
        plt.title("Convergence curve for " + str(f))
        plt.xlabel("EFOs")
        plt.ylabel("Fitness")
        plt.plot(efos, fitness_history, label=str(names_alg))
        plt.legend()
        name = "Funciones-continuas/result/Convergence curve for " + str(num_f) + "-bw-" + str(bw) + "-max_local-" + str(max_local) + ".png"
        plt.savefig(name)
        #plt.show()
        plt.clf()

    # Plot convergence curve comparison for two or more algorithms
    def plot_convergence_curve_comparison(fitness_history, f, names_alg, num_f, bw, max_local):
        efos = np.arange(len(fitness_history[0]))
        plt.title("Convergence curve for " + str(f))
        plt.xlabel("EFOs")
        plt.ylabel("Fitness")
        algorithms = len(fitness_history)
        for a in range(algorithms):
            plt.plot(efos, fitness_history[a], label=str(names_alg[a]))            
        plt.legend()
        name = "Funciones-continuas/result/Convergence curve for " + str(num_f) + "-bw-" + str(bw) + "-max_local-" + str(max_local) + ".png"
        print(name)
        plt.savefig(name)    
        #plt.show()
        plt.clf()        

    def print_alorithms_with_avg_fitness(alg, avg_fitness):
        rows = len(alg)
        for r in range(rows):
            print(alg[r] + " {0:12.6f}".format(avg_fitness[r]))
                 
