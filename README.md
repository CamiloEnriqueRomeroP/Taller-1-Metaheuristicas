# Taller-1-Metaheuristicas
Taller-1-Metaheuristicas

El proyecto cuenta con 4 carpetas, tres de ellas almacenan los códigos implementados junto con los resultados de los experimentos realizados y una última carpeta con los resultados seleccionados después de realizar el proceso de sintonización.

Las carpetas Funciones-continuas, Problema-de-la-mochila-binaria y Problema-viajero-TSP contienen la siguiente estructura:

- Subcarpeta algorithms, que contiene los algoritmos HC, HCRR, SA y GRASP
- Subcarpeta result, que contiene las tablas en formato csv correspondientes a: 1) la comparación de fitness promedio de los cuatro algoritmos para cada problema, 2) la comparación del tiempo de ejecución promedio de los cuatro algoritmos para cada problema, 3) Tablas de cada algoritmo donde se muestran el fitness promedio, distribución, mejor y peor valor, y tiempo de ejecución promedio. Adicionalmente, en esta carpeta se muestran todas las curvas de convergencia de los 3 experimentos realizados para obtener la sintonización, junto con un gráfico adicional para cada función que compara los resultados obtenidos en clase sin modificar el Tweak con el algoritmo GRASP implementado con el Tweak modificado. 
- Subcarpeta problems/functions, que contiene los problemas o funciones que va a buscar optimizar cada algoritmo
- Código main.py, que permite compilar el código completo para cada problema de optimización. El código se realizó de tal manera que pueda ser ejecutado sin interrupciones y utilizando los 4 algoritmos para cada problema o función en 50.000 evaluaciones de la función objetivo con 31 semillas.
- Código plot_convergence_curve.py, que contiene el método para crear y guardar las curvas de convergencia con base en los datos suministrados.
- Código solution.py, el cual contiene la inicialización de las soluciones, junto con el Tweak que modifica las soluciones buscando mejorar su fitness.
- Códigos knapsack.py y tsp.py, que se encuentran en sus respectivas carpetas y que inicializan a la solución y la evalúan.

Dentro de la carpeta Resultados-seleccionados se encuentran las tres carpetas correspondientes a los algoritmos implementados. Cada una cuenta con los datos seleccionados al realizar la sintonización, junto con la evaluación de los test no paramétricos de Friedman y Wilcoxson, además de un documento de Word con la interpretación de dichos tests.