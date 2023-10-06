import numpy as np
import pandas as pd
import time
from plot_convergence_curve import plot_convergence_curve
from functions.sphere import sphere
from functions.step import step
from functions.schwefel import schwefel
from functions.ackley import ackley
from functions.griewank import griewank
from functions.rastrigin import rastrigin
from algorithms.HC import HC
from algorithms.HCRR import HCRR
from algorithms.SA import SA
from algorithms.GRASP import GRASP

d = 50
max_efos = 50000
repetitions = 31

# Afinamiento de parametros
bw = 0.1
max_local = 101

functions = [sphere(), step(), schwefel(), ackley(), griewank(), rastrigin()]
functions = [schwefel()]
hc = HC(max_efos=max_efos, bandwidth=bw)
hcrr = HCRR(max_efos=max_efos, max_local=max_local, bandwidth=bw)
sa = SA(max_efos=max_efos, bandwidth=bw)
grasp = GRASP(max_local=max_local, max_efos=max_efos, bandwidth=bw)
#algorithms = [hc, hcrr, sa, grasp]
algorithms = [grasp]

df = pd.DataFrame({'Problem': pd.Series(dtype='str'),
                   'Average Fitness': pd.Series(dtype='float'),
                   'Standard Deviation': pd.Series(dtype='float'),
                   'Best Fitness': pd.Series(dtype='float'),
                   'Worst Fitness': pd.Series(dtype='float'),
                   'Execution Time': pd.Series(dtype='float')})
df2 = df
df3 = df
df4 = df

df5 = pd.DataFrame({'Problem': pd.Series(dtype='str'),
                   'Average Fitness HC': pd.Series(dtype='float'),
                   'Average Fitness HCRR': pd.Series(dtype='float'),
                   'Average Fitness SA': pd.Series(dtype='float'),
                   'Average Fitness GRASP': pd.Series(dtype='float')})

num_f = 0

for f in functions:
    start_timer_p = time.time()
    names_alg = []
    avg_curve_alg = []
    best_avg_fitness_alg = []
    best_std_fitness_alg = []
    best_fitness_along_seeds = []
    worst_fitness_along_seeds = []
    alg_avg_time = []
    name_functions = ["Sphere", "Step", "Schwefel",
                      "Ackley", "Griewank", "Rastrigin"]

    for alg in algorithms:
        avg_curve = np.zeros(max_efos, float)
        best_fitnes = np.zeros(repetitions, float)
        time_by_repetition = np.zeros(repetitions, float)

        for s in range(0, repetitions):
            start_timer = time.time()
            curve_data, stop = alg.evolve(seed=s, d=d, f=f)
            end_timer = time.time()
            if stop:
                print("In " + str(name_functions[num_f])+ " " + str(alg) + " repetition "+ str(s) + " STOP")
            time_spend = end_timer - start_timer
            avg_curve = avg_curve + curve_data
            time_by_repetition[s] = time_spend
            best_fitnes[s] = alg.best.fitness

        avg_curve = avg_curve / repetitions
        avg_best_fitnes = np.average(best_fitnes)
        std_best_fitnes = np.std(best_fitnes)
        avg_time = np.average(time_by_repetition)
        names_alg.append(str(alg))
        avg_curve_alg.append(avg_curve)
        best_avg_fitness_alg.append(avg_best_fitnes)
        best_std_fitness_alg.append(std_best_fitnes)
        best_fitness_along_seeds.append(min(best_fitnes))
        worst_fitness_along_seeds.append(max(best_fitnes))
        alg_avg_time.append(avg_time)

    plot_convergence_curve.plot_convergence_curve_comparison(
        avg_curve_alg, f, names_alg, name_functions[num_f], bw, max_local)

    end_timer_p = time.time()
    time_p = end_timer_p - start_timer_p
    print("Tiempo de ejecucion " + str(name_functions[num_f]) + " : "+ str(time_p))
    num_f = num_f + 1

    new_row = pd.DataFrame({'Problem': str(f),
                            'Average Fitness': str(best_avg_fitness_alg[0]),
                            'Standard Deviation': str(best_std_fitness_alg[0]),
                            'Best Fitness': str(best_fitness_along_seeds[0]),
                            'Worst Fitness': str(worst_fitness_along_seeds[0]),
                            'Execution Time': str(alg_avg_time[0])}, index=[0])
    
    new_row2 = pd.DataFrame({'Problem': str(f),
                            'Average Fitness': str(best_avg_fitness_alg[1]),
                            'Standard Deviation': str(best_std_fitness_alg[1]),
                            'Best Fitness': str(best_fitness_along_seeds[1]),
                            'Worst Fitness': str(worst_fitness_along_seeds[1]),
                            'Execution Time': str(alg_avg_time[1])}, index=[0])
    
    new_row3 = pd.DataFrame({'Problem': str(f),
                            'Average Fitness': str(best_avg_fitness_alg[2]),
                            'Standard Deviation': str(best_std_fitness_alg[2]),
                            'Best Fitness': str(best_fitness_along_seeds[2]),
                            'Worst Fitness': str(worst_fitness_along_seeds[2]),
                            'Execution Time': str(alg_avg_time[2])}, index=[0])
    
    new_row4 = pd.DataFrame({'Problem': str(f),
                            'Average Fitness': str(best_avg_fitness_alg[3]),
                            'Standard Deviation': str(best_std_fitness_alg[3]),
                            'Best Fitness': str(best_fitness_along_seeds[3]),
                            'Worst Fitness': str(worst_fitness_along_seeds[3]),
                            'Execution Time': str(alg_avg_time[3])}, index=[0])
   
    
    new_row5 = pd.DataFrame({'Problem': str(f),
                   'Average Fitness HC': str(best_avg_fitness_alg[0]),
                   'Average Fitness HCRR': str(best_avg_fitness_alg[1]),
                   'Average Fitness SA': str(best_avg_fitness_alg[2]),
                   'Average Fitness GRASP': str(best_avg_fitness_alg[3])}, index=[0])
    
    df = pd.concat([df.loc[:], new_row]).reset_index(drop=True)
    df2 = pd.concat([df2.loc[:], new_row2]).reset_index(drop=True)
    df3 = pd.concat([df3.loc[:], new_row3]).reset_index(drop=True)
    df4 = pd.concat([df4.loc[:], new_row4]).reset_index(drop=True)
    df5 = pd.concat([df5.loc[:], new_row5]).reset_index(drop=True)

df.to_csv("Funciones-continuas/result/HC" + "-bw-" + str(bw) +
          "-max_local-" + str(max_local) + ".csv", index=False)
df2.to_csv("Funciones-continuas/result/HCRR" + "-bw-" + str(bw) +
           "-max_local-" + str(max_local) + ".csv", index=False)
df3.to_csv("Funciones-continuas/result/SA" + "-bw-" + str(bw) +
           "-max_local-" + str(max_local) + ".csv", index=False)
df4.to_csv("Funciones-continuas/result/GRASP" + "-bw-" + str(bw) +
           "-max_local-" + str(max_local) + ".csv", index=False)
df5.to_csv("Funciones-continuas/result/Comparison_dataset" + "-bw-" + str(bw) +
           "-max_local-" + str(max_local) + ".csv", index=False)
