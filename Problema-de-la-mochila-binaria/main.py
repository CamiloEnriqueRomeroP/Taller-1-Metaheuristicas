import pandas as pd
import numpy as np
import time
from knapsack import knapsack
from algorithms.HC import HC
from algorithms.HCRR import HCRR
from algorithms.SA import SA
from algorithms.GRASP import GRASP
from plot_convergence_curve import plot_convergence_curve
import math

myPath = "Problema-de-la-mochila-binaria/problems/"

max_efos = 50000
repetitions = 31

# Afinamiento de parametros
max_local = 100

myP1 = knapsack(myPath + "f1.txt")
myP2 = knapsack(myPath + "f2.txt")
myP3 = knapsack(myPath + "f3.txt")
myP4 = knapsack(myPath + "f4.txt")
myP5 = knapsack(myPath + "f5.txt")
myP6 = knapsack(myPath + "f6.txt")
myP7 = knapsack(myPath + "f7.txt")
myP8 = knapsack(myPath + "f8.txt")
myP9 = knapsack(myPath + "f9.txt")
myP10 = knapsack(myPath + "f10.txt")
myP11 = knapsack(myPath + "Knapsack1.txt")
myP12 = knapsack(myPath + "Knapsack2.txt")
myP13 = knapsack(myPath + "Knapsack3.txt")
myP14 = knapsack(myPath + "Knapsack4.txt")
myP15 = knapsack(myPath + "Knapsack5.txt")
myP16 = knapsack(myPath + "Knapsack6.txt")
problems = [#myP1, myP2, myP3, myP4, myP5, myP6, myP7, myP8, myP9, myP10, myP11, myP12, myP13, myP14, myP15, 
            myP16]
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
                   'Average Execution Time': pd.Series(dtype='float')
                   #,"Total Execution Time": pd.Series(dtype='float')
                   })
df2 = df
df3 = df
df4 = df

df5 = pd.DataFrame({'Problem': pd.Series(dtype='str'),
                   'Average Fitness HC': pd.Series(dtype='float'),
                   'Average Fitness HCRR': pd.Series(dtype='float'),
                   'Average Fitness SA': pd.Series(dtype='float'),
                   'Average Fitness GRASP': pd.Series(dtype='float')})

df6 = pd.DataFrame({'Problem': pd.Series(dtype='str'),
                   'Execution Time HC': pd.Series(dtype='float'),
                   'Execution Time HCRR': pd.Series(dtype='float'),
                   'Execution Time SA': pd.Series(dtype='float'),
                   'Execution Time GRASP': pd.Series(dtype='float')})

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
    total_time = []
    iter_stop = 0
    copy_iteration = 0
    detect_iter_stop = False
    name_problem = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9",
                    "f10", "Knapsack1", "Knapsack2", "Knapsack3", "Knapsack4", "Knapsack5", "Knapsack6"]
    for alg in algorithms:
        avg_curve = np.zeros(max_efos, float)
        best_fitnes = np.zeros(repetitions, float)
        time_by_repetition = np.zeros(repetitions, float)
        print(alg)
        for s in range(0, repetitions):
            start_timer = time.time()
            curve_data, stop = alg.evolve(seed=s, problem=p)            
            end_timer = time.time()
            print(s)
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
        best_fitness_along_seeds.append(max(best_fitnes))
        worst_fitness_along_seeds.append(min(best_fitnes))
        alg_avg_time.append(avg_time)
        total_time.append(math.fsum(time_by_repetition))

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
    
    new_row2 = pd.DataFrame({'Problem': str(p),
                            'Average Fitness': str(best_avg_fitness_alg[1]),
                            'Standard Deviation': str(best_std_fitness_alg[1]),
                            'Best Fitness': str(best_fitness_along_seeds[1]),
                            'Worst Fitness': str(worst_fitness_along_seeds[1]),
                            'Execution Time': str(alg_avg_time[1])}, index=[0])
    
    new_row3 = pd.DataFrame({'Problem': str(p),
                            'Average Fitness': str(best_avg_fitness_alg[2]),
                            'Standard Deviation': str(best_std_fitness_alg[2]),
                            'Best Fitness': str(best_fitness_along_seeds[2]),
                            'Worst Fitness': str(worst_fitness_along_seeds[2]),
                            'Execution Time': str(alg_avg_time[2])}, index=[0])
    
    new_row4 = pd.DataFrame({'Problem': str(p),
                            'Average Fitness': str(best_avg_fitness_alg[3]),
                            'Standard Deviation': str(best_std_fitness_alg[3]),
                            'Best Fitness': str(best_fitness_along_seeds[3]),
                            'Worst Fitness': str(worst_fitness_along_seeds[3]),
                            'Execution Time': str(alg_avg_time[3])}, index=[0])
   
    
    new_row5 = pd.DataFrame({'Problem': str(p),
                   'Average Fitness HC': str(best_avg_fitness_alg[0]),
                   'Average Fitness HCRR': str(best_avg_fitness_alg[1]),
                   'Average Fitness SA': str(best_avg_fitness_alg[2]),
                   'Average Fitness GRASP': str(best_avg_fitness_alg[3])}, index=[0])
    
    
    new_row6 = pd.DataFrame({'Problem': str(p),
                    'Execution Time HC': str(alg_avg_time[0]),
                    'Execution Time HCRR': str(alg_avg_time[1]),
                    'Execution Time SA': str(alg_avg_time[2]),
                    'Execution Time GRASP': str(alg_avg_time[3])}, index=[0])
    
    df = pd.concat([df.loc[:], new_row]).reset_index(drop=True)
    df2 = pd.concat([df2.loc[:], new_row2]).reset_index(drop=True)
    df3 = pd.concat([df3.loc[:], new_row3]).reset_index(drop=True)
    df4 = pd.concat([df4.loc[:], new_row4]).reset_index(drop=True)
    df5 = pd.concat([df5.loc[:], new_row5]).reset_index(drop=True)
    df6 = pd.concat([df6.loc[:], new_row6]).reset_index(drop=True)
    
df.to_csv("Problema-de-la-mochila-binaria/result/HC" +
          "-max_local-" + str(max_local) + ".csv", index=False)
df2.to_csv("Problema-de-la-mochila-binaria/result/HCRR" +
           "-max_local-" + str(max_local) + ".csv", index=False)
df3.to_csv("Problema-de-la-mochila-binaria/result/SA" +
           "-max_local-" + str(max_local) + ".csv", index=False)
df4.to_csv("Problema-de-la-mochila-binaria/result/GRASP" +
           "-max_local-" + str(max_local) + ".csv", index=False)
df5.to_csv("Problema-de-la-mochila-binaria/result/Comparison_dataset" +
           "-max_local-" + str(max_local) + ".csv", index=False)
df6.to_csv("Funciones-continuas/result/Comparison_time" +
           "-max_local-" + str(max_local) + ".csv", index=False)