import numpy as np

def initialize_population(pop_size, dimensions, lower_bound, upper_bound):
    """
    تهيئة السكان الأولية للدالة التحسينية:
    تقوم بإنشاء مجموعة من الحلول (السكان) عشوائياً ضمن الحدود المحددة.

    Initialize the initial population for the optimization algorithm:
    Creates a population of candidate solutions randomly within the given bounds.
    """
    population = np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dimensions))
    return population
