import numpy as np
import pandas as pd
import time
from tsp import tsp
from algorithms.HC import HC
from algorithms.HCRR import HCRR
from algorithms.SA import SA
from algorithms.GRASP import GRASP
from plot_convergence_curve import plot_convergence_curve

# myPath = "/problems/"
myPath = "Problema-viajero-TSP/problems/"

max_efos = 50000
repetitions = 31

# Afinamiento de parametros
max_local = 500

myP1 = tsp(myPath + "01-easy5.txt")
myP2 = tsp(myPath + "02-ulysses16.txt")
myP3 = tsp(myPath + "03-fri26.txt")
myP4 = tsp(myPath + "04-dantzig42.txt")
myP5 = tsp(myPath + "05-att48.txt")
problems = [myP1, myP2, myP3, myP4, myP5]
hc = HC(max_efos=max_efos)
hcrr = HCRR(max_efos=max_efos, max_local=max_local)
sa = SA(max_efos=max_efos)
grasp = GRASP(max_efos=max_efos, max_local=max_local)
algorithms = [hc, hcrr, sa, grasp]

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

num_p = 0

for p in problems:
    start_timer_p = time.time()
    names_alg = []
    avg_curve_alg = []
    best_avg_fitness_alg = []
    best_std_fitness_alg = []
    best_fitness_along_seeds = []
    worst_fitness_along_seeds = []
    alg_avg_time = []
    name_problem = ["01-easy5", "02-ulysses16", "03-fri26", "04-dantzig42", "05-att48"]

    for alg in algorithms:
        avg_curve = np.zeros(max_efos, float)
        best_fitnes = np.zeros(repetitions, float)
        time_by_repetition = np.zeros(repetitions, float)

        for s in range(0, repetitions):
            start_timer = time.time()
            curve_data, stop = alg.evolve(seed=s, problem=p)
            end_timer = time.time()
            if stop:
                print("In " + str(name_problem[num_p])+ " " + str(alg) + " repetition "+ str(s) + " STOP")
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
        avg_curve_alg, p, names_alg, name_problem[num_p], max_local)  

    end_timer_p = time.time()
    time_p = end_timer_p - start_timer_p
    print("Tiempo de ejecucion " + str(name_problem[num_p]) + " : "+ str(time_p))
    num_p = num_p + 1
    
    new_row = pd.DataFrame({'Problem': str(p),
                            'Average Fitness': str(best_avg_fitness_alg[0]),
                            'Standard Deviation': str(best_std_fitness_alg[0]),
                            'Best Fitness': str(best_fitness_along_seeds[0]),
                            'Worst Fitness': str(worst_fitness_along_seeds[0]),
                            'Execution Time': str(alg_avg_time[0])}, index=[0])
    df = pd.concat([df.loc[:], new_row]).reset_index(drop=True)

    new_row2 = pd.DataFrame({'Problem': str(p),
                             'Average Fitness': str(best_avg_fitness_alg[1]),
                             'Standard Deviation': str(best_std_fitness_alg[1]),
                             'Best Fitness': str(best_fitness_along_seeds[1]),
                             'Worst Fitness': str(worst_fitness_along_seeds[1]),
                             'Execution Time': str(alg_avg_time[1])}, index=[0])
    new_row2 = new_row
    new_row3 = new_row
    new_row4 = new_row
    
    new_row5 = pd.DataFrame({'Problem': str(p),
                   'Average Fitness HC': str(best_avg_fitness_alg[0]),
                   'Average Fitness HCRR': str(best_avg_fitness_alg[1]),
                   'Average Fitness SA': str(best_avg_fitness_alg[2]),
                   'Average Fitness GRASP': str(best_avg_fitness_alg[3])}, index=[0])
    
    df = pd.concat([df.loc[:], new_row]).reset_index(drop=True)
    df2 = pd.concat([df2.loc[:], new_row2]).reset_index(drop=True)
    df3 = pd.concat([df3.loc[:], new_row3]).reset_index(drop=True)
    df4 = pd.concat([df4.loc[:], new_row4]).reset_index(drop=True)
    df5 = pd.concat([df5.loc[:], new_row5]).reset_index(drop=True)

df.to_csv("Problema-viajero-TSP/result/HC" +
          "-max_local-" + str(max_local) + ".csv", index=False)
df2.to_csv("Problema-viajero-TSP/result/HCRR" +
           "-max_local-" + str(max_local) + ".csv", index=False)
df3.to_csv("Problema-viajero-TSP/result/SA" +
           "-max_local-" + str(max_local) + ".csv", index=False)
df4.to_csv("Problema-viajero-TSP/result/GRASP" +
           "-max_local-" + str(max_local) + ".csv", index=False)
df5.to_csv("Problema-viajero-TSP/result/Comparison_dataset" +
           "-max_local-" + str(max_local) + ".csv", index=False)