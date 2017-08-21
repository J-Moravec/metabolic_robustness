# metabolic_robustnest/tests/test_constant_environment.py

import pytest
from metabolic_robustness.constant_environment.environment import Environment
from metabolic_robustness.constant_environment.fitness import Fitness

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

    def test_init_fails_on_environment(self):
        with pytest.raises(TypeError):
            fitness = Fitness(environment="not_environment")

    def test_init_success(self):
        environment = Environment()
        fitness = Fitness(environment=environment)

    # require test for validity of fitness result
