# metabolic_robustness/constant_environment/mutation.py

import attr
from metabolic_robustness.utils.normdist import norm_sample
from metabolic_robustness.utils.normdist import truncnorm_sample
from math import sqrt

@attr.attrs
class Mutation(object):
    """
    This class represents mutations of fitness.

    Parameters of fitness (mean, variance) mutates according to parameters of
    Mutation class. Normal distribution is generated with mean of mutated
    parameter and varriance according to variance of mutation's parameter
    for mutated parameter.
    """
    fitness_var = attr.attrib(
        default = 0.1
        )
    fitness_mean = attr.attrib(
        default = 0.1
        )


    def mutate(self, fitness, environment):
        new_fitness_mean = self._mutate_fitness_mean(fitness, environment)
        new_fitness_var = self._mutate_fitness_var(fitness)

        fitness.mean = new_fitness_mean
        fitness.var = new_fitness_var


    def _mutate_fitness_mean(self, fitness, environment):
        new_mean = truncnorm_sample(
            mean = fitness.mean,
            var = self.fitness_mean,
            min = environment.min,
            max = environment.max
            )
        return(new_mean)


    def _mutate_fitness_var(self, fitness):
        new_var = norm_sample(
            mean = fitness.var,
            var = self.fitness_var
            )
        return(new_var)
