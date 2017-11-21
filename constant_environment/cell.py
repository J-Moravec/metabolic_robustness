# metabolic_robustness/constant_environment/cell.py

import attr
from metabolic_robustness.constant_environment.fitness import Fitness
from metabolic_robustness.constant_environment.environment import Environment
from metabolic_robustness.constant_environment.mutation import Mutation

@attr.attrs
class Cell(object):
    """
    Implementation of cell for model.
    """
    fitness = attr.attrib(
        default = attr.Factory(Fitness),
        validator = attr.validators.instance_of(Fitness)
        )
    environment = attr.attrib(
        default = attr.Factory(Environment)
        )
    mutation = attr.attrib(
        default = attr.Factory(Mutation),
        validator = attr.validators.instance_of(Mutation)
        )


    def get_fitness(self):
        return self.fitness.fitness(self.environment)


    def mutate(self):
        self.mutation.mutate(self.fitness, self.environment)


    def divide(self):
        new_cell = Cell.daughter(self)
        return(new_cell)


    @classmethod
    def daughter(cls, cell):
        new_fitness = Fitness(
            cell.fitness.mean,
            cell.fitness.var
            )
        new_cell = cls(
            fitness = new_fitness,
            environment = cell.environment,
            mutation = cell.mutation
            )
        return(new_cell)
