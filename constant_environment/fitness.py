# metabolic_robustness/constant_environment/fitness.py

import attr
from metabolic_robustness.utils.normdist import truncnorm_pdf

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

    def fitness(self, environment):
        val = truncnorm_pdf(
            environment.current,
            self.mean,
            self.var,
            environment.min,
            environment.max
            )
        return(val)
