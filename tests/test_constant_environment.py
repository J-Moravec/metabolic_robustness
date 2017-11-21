# metabolic_robustness/tests/test_constant_environment.py

import pytest
from metabolic_robustness.constant_environment.environment import Environment
from metabolic_robustness.constant_environment.fitness import Fitness
from metabolic_robustness.constant_environment.mutation import Mutation
from metabolic_robustness.constant_environment.cell import Cell

class TestEnvironment(object):

    def test_init_without_current_envir(self):
        environment = Environment(min=0, max=100)
        assert(environment.current > 0 and environment.current < 100)

    def test_init_with_current_env_fail(self):
        with pytest.raises(ValueError):
            environment = Environment(min=0, max=100, current=200)

    def test_init_with_current_env_pass(self):
        environment = Environment(min=0, max=100, current=50)


class TestFitness(object):
    def test_fitness(self):
        environment = Environment()
        fitness = Fitness()
        fitness.fitness(environment)
    # TODO require tests for validity of fitness result


class TestMutation(object):
    def test_mutate(self):
        environment = Environment()
        fitness = Fitness()
        mutation = Mutation()
        mutation.mutate(fitness, environment)
    # TODO require tests for mutation values


class TestCell(object):
    def test_cell_api(self):
        cell = Cell()
        cell.get_fitness()
        cell.mutate()


    def test_cell_divide_before_mutation(self):
        cell = Cell()
        new_cell = cell.divide()
        assert(cell == new_cell)


    def test_cell_divide_after_mutation(self):
        cell = Cell()
        new_cell = cell.divide()
        cell.mutate()
        assert(cell != new_cell)


    def test_cell_divide_shared_environment(self):
        cell = Cell()
        new_cell = cell.divide()
        assert(cell.environment is new_cell.environment)


    def test_cell_divide_shared_mutation(self):
        cell = Cell()
        new_cell = cell.divide()
        assert(cell.mutation is new_cell.mutation)


class TestCells(object):
    pass
    # TODO require tests for cells
