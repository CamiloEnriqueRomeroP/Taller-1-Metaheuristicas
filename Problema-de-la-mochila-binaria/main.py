import pandas as pd
import numpy as np
import time
from knapsack import knapsack
from algorithms.HC import HC
from algorithms.HCRR import HCRR
from algorithms.SA import SA
from plot_convergence_curve import plot_convergence_curve

myPath = "D:/Metaheuristicas/Taller 1/Problema-de-la-mochila-binaria/problems/"
#myPath = "content/sample_data/problems/"

max_efos = 5000
max_local = 1000
repetitions = 31
myP1 = knapsack(myPath +"f1.txt")
myP2 = knapsack(myPath +"f2.txt")
myP3 = knapsack(myPath +"f3.txt")
myP4 = knapsack(myPath +"f4.txt")
myP5 = knapsack(myPath +"f5.txt")
myP6 = knapsack(myPath +"f6.txt")
myP7 = knapsack(myPath +"f7.txt")
myP8 = knapsack(myPath +"f8.txt")
myP9 = knapsack(myPath +"f9.txt")
myP10 = knapsack(myPath +"f10.txt")
myP11 = knapsack(myPath +"Knapsack1.txt")
myP12 = knapsack(myPath +"Knapsack2.txt")
myP13 = knapsack(myPath +"Knapsack3.txt")
myP14 = knapsack(myPath +"Knapsack4.txt")
myP15 = knapsack(myPath +"Knapsack5.txt")
problems = [myP1, myP2, myP3, myP4, myP5, myP6, myP7, myP8,myP9, myP10, myP11, myP12, myP13, myP14, myP15]
#problems = [myP1]
hc = HC(max_efos = max_efos)
hcrr = HCRR(max_efos= max_efos, max_local = max_local)
sa = SA(max_efos = max_efos)
algorithms = [hc, hcrr, sa, hc]

df = pd.DataFrame({'Problem': pd.Series(dtype='str'),
                   'Average Fitness': pd.Series(dtype='float'),
                   'Standard Deviation': pd.Series(dtype='float'),
                   'Best Fitness': pd.Series(dtype='float'),
                   'Worst Fitness': pd.Series(dtype='float'),
                   'Execution Time': pd.Series(dtype='float')})
df2 = pd.DataFrame({'Problem': pd.Series(dtype='str'),
                   'Average Fitness': pd.Series(dtype='float'),
                   'Standard Deviation': pd.Series(dtype='float'),
                   'Best Fitness': pd.Series(dtype='float'),
                   'Worst Fitness': pd.Series(dtype='float'),
                   'Execution Time': pd.Series(dtype='float')})
df3 = pd.DataFrame({'Problem': pd.Series(dtype='str'),
                   'Average Fitness': pd.Series(dtype='float'),
                   'Standard Deviation': pd.Series(dtype='float'),
                   'Best Fitness': pd.Series(dtype='float'),
                   'Worst Fitness': pd.Series(dtype='float'),
                   'Execution Time': pd.Series(dtype='float')})
df4 = pd.DataFrame({'Problem': pd.Series(dtype='str'),
                   'Average Fitness': pd.Series(dtype='float'),
                   'Standard Deviation': pd.Series(dtype='float'),
                   'Best Fitness': pd.Series(dtype='float'),
                   'Worst Fitness': pd.Series(dtype='float'),
                   'Execution Time': pd.Series(dtype='float')})

for p in problems:

  names_alg = []
  avg_curve_alg = []
  best_avg_fitness_alg = []
  best_std_fitness_alg = []
  best_fitness_along_seeds = []  
  worst_fitness_along_seeds = []
  alg_avg_time = []

  for alg in algorithms:
    avg_curve = np.zeros(max_efos, float)
    best_fitnes = np.zeros(repetitions, float)
    time_by_repetition = np.zeros(repetitions, float)

    for s in range(0, repetitions):
      start_timer = time.time()
      curve_data = alg.evolve(seed=s, problem=p)
      end_timer = time.time()      
      time_spend = end_timer - start_timer
      avg_curve = avg_curve + curve_data
      time_by_repetition[s] = time_spend
      best_fitnes[s] = alg.best.fitness

    avg_curve = avg_curve/ repetitions
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

  plot_convergence_curve.plot_convergence_curve_comparison(avg_curve_alg, p, names_alg)
  
  new_row = pd.DataFrame({'Problem': str(p),
                           'Average Fitness':str(best_avg_fitness_alg[0]),
                           'Standard Deviation':str(best_std_fitness_alg[0]),
                           'Best Fitness':str(best_fitness_along_seeds[0]),
                           'Worst Fitness':str(worst_fitness_along_seeds[0]),
                           'Execution Time':str(alg_avg_time[0])}, index=[0])
  df = pd.concat([df.loc[:], new_row]).reset_index(drop=True)  
  
  new_row2 = pd.DataFrame({'Problem': str(p),
                           'Average Fitness':str(best_avg_fitness_alg[1]),
                           'Standard Deviation':str(best_std_fitness_alg[1]),
                           'Best Fitness':str(best_fitness_along_seeds[1]),
                           'Worst Fitness':str(worst_fitness_along_seeds[1]),
                           'Execution Time':str(alg_avg_time[1])}, index=[0])
  df2 = pd.concat([df2.loc[:], new_row2]).reset_index(drop=True)  
  
  new_row3 = pd.DataFrame({'Problem': str(p),
                           'Average Fitness':str(best_avg_fitness_alg[2]),
                           'Standard Deviation':str(best_std_fitness_alg[2]),
                           'Best Fitness':str(best_fitness_along_seeds[2]),
                           'Worst Fitness':str(worst_fitness_along_seeds[2]),
                           'Execution Time':str(alg_avg_time[2])}, index=[0])
  df3 = pd.concat([df3.loc[:], new_row3]).reset_index(drop=True)   
  
  new_row4 = pd.DataFrame({'Problem': str(p),
                           'Average Fitness':str(best_avg_fitness_alg[3]),
                           'Standard Deviation':str(best_std_fitness_alg[3]),
                           'Best Fitness':str(best_fitness_along_seeds[3]),
                           'Worst Fitness':str(worst_fitness_along_seeds[3]),
                           'Execution Time':str(alg_avg_time[3])}, index=[0])
  df4 = pd.concat([df4.loc[:], new_row4]).reset_index(drop=True)  

df.to_csv("D:/Metaheuristicas/Taller 1/Problema-de-la-mochila-binaria/HC.csv", index=False)
df2.to_csv("D:/Metaheuristicas/Taller 1/Problema-de-la-mochila-binaria/HCRR.csv", index=False)
df3.to_csv("D:/Metaheuristicas/Taller 1/Problema-de-la-mochila-binaria/SA.csv", index=False)
df4.to_csv("D:/Metaheuristicas/Taller 1/Problema-de-la-mochila-binaria/Compilado.csv", index=False)