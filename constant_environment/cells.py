#from metaboic_robustness.constant_environment.cell import Cell

class Cells(list):
    """
    This class of cells represent model where cells are in constant environment
    with constant population of cells.

    Growth of cells is generational according to modified Moran process.
    In Moran process, each step only single individual is chosen for death
    and another one for reproduction. In this case, k individuals are chosen
    for death and l individuals for reproduction. To keep population constant,
    k=l. In population of even size (divisible by two), i.e., 2n, size of
    k and l would ideally be half of the total population: k=l=n.

    Probability of choice of each individual is dependent on each individual's
    fitness.

    Fitness is defined as truncated normal distribution with mean and variance.
    Its truncation depends on definition of environment, its borders.

    Fitness is then value of said truncated normal distribution for specific
    value of environment.
    """
    def __init__(self):
        """
        Generate population of cells up to maximum population with current
        fitness according to constant value of environment and fitness variance.

        Maximum population must be odd.
        """
        pass


    def grow(self):
        """
        Takes population of cells and pick half of them that will survive and
        double, other will die.
        """
        pass


    def mutate(self):
        pass
