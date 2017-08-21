# metabolic_robustness/constant_environment/cell.py

import attr
from metabolic_robustness.constant_environment.fitness import Fitness
from metabolic_robustness.constant_environment.mutation import Mutation

@attr.attrs
class Cell(object):
    """
    TODO


    """
    fitness = attr.attrib(
        default = attr.Factory(Fitness),
        validator = attr.validators.instance_of(Fitness)
        )
    mutation = attr.attrib(
        default = attr.Factory(Mutation),
        validator = attr.validators.instance_of(Mutation)
        )

    def get_fitness(self):
        return self.fitness.fitness()

    def mutate(self):
        this.mutation.mutate()
