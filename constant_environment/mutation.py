# metabolic_robustnest/constant_environment/mutation.py

import attr

@attr.attrs
class Mutation(object):


    def mutate(self):
        raise NotImplemented()
