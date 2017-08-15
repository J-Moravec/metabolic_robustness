#from metabolic_robustness.constant_environment.fitness import Fitness

class Cell(object):
    """
    TODO


    """
    def __init__(self, fitness, mutation, environment):
        self.fitness = fitness
        self.mutation = mutation
        self.environment = environment

    def fitness(self, environment):
        return self.fitness(environment)

    def mutate(self):
        this.mutation()
