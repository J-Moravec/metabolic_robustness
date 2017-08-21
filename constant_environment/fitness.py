# metabolic_robustness/constant_environment/fitness.py

import attr
from metabolic_robustness.constant_environment.environment import Environment
from scipy.stats import truncnorm
from math import sqrt


@attr.attrs
class Fitness(object):
    """
    This class represent cell's fitness. All information and methods regarding
    specific cell's fitness are kept here.

    Fitness is defined as truncated normal distribution with mean and variance.
    Its truncation depends on definition of environment, its borders.

    Fitness is then value of said truncated normal distribution for specific
    value of environment.
    """

    mean = attr.attrib(
        default = 50
        )
    var = attr.attrib(
        default = 1
        )
    environment = attr.attrib(
        default = attr.Factory(Environment),
        validator = attr.validators.instance_of(Environment)
        )


    def fitness(self):
        a = (self.environment.min - self.mean) / sqrt(self.var)
        b = (self.environment.max - self.mean) / sqrt(self.var)
        val = truncnorm.pdf(
            self.environment.current,
            a,
            b,
            loc=self.mean,
            scale=self.var
            )
        return(val)
