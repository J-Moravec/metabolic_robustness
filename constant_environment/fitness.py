from scipy.stats import truncnorm
from math import sqrt

class Fitness(object):
    """
    This class represent cell's fitness. All information and methods regarding
    specific cell's fitness are kept here.

    Fitness is defined as truncated normal distribution with mean and variance.
    Its truncation depends on definition of environment, its borders.

    Fitness is then value of said truncated normal distribution for specific
    value of environment.
    """

    def __init__(self, mean, var, environment):
        this.mean = mean
        this.var = var
        this.environment = environment


    def fitness(self):
        a = (environment.min - mean) / sqrt(var)
        b = (environment.max - mean) / sqrt(var)
        truncnorm(a,b)
