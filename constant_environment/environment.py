import attr
import random


@attr.attrs
class Environment(object):
    """
    Environment class holds information on environmental limitation and current
    value of environment.

    In the case of constant_environment, these cannot be changed.
    """
    min = attr.attrib(
        default=0,
        frozen=True,
        validator = attr.validators.instance_of((int, float))
        )
    max = attr.attrib(
        default=100,
        frozen=True,
        validator = attr.validators.instance_of((int, float))
        )
    current = attr.atrrib()


    @current.default
    def initialize_current(self):
        return random.uniform(self.min, self.max)

    @current.validator
    def validate_current(self, attribute, value):
        if value < self.min or value > self.max:
            raise ValueError(
                "Current environment must be between minimum and maximum value"
                " of environment."
                )
