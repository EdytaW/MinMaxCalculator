import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []

for i in range(100000):
    argument_list.append(i/10)
    i += 1

for formula in formulas_list:
    results_list = []
    print("Calculating :" + formula)
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print("Minimum value of results list is: {}".format(min(results_list)))
    print("Maximum value of results list is: {}".format(max(results_list)))
    stop = time.time()
    print("Calculation time: {}".format(stop - start))

for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))

    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()

    print("Calculation time with compile: {}".format(stop - start))
