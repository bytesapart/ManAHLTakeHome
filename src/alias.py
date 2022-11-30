import random
import logging

log = logging.getLogger('random_pick')


class AliasMethod(object):
    """ A random pick generator based on Alias Method.
    """

    def __init__(self, dist):
        """ (VoseAlias, dict) -> NoneType """
        self.dist = dist
        self.alias_initialisation()
        self.table_prob_list = list(self.table_prob)

    def alias_initialisation(self):
        """ Construct probability and alias tables. """
        log.info("Starting alias_initialisation() function")
        # Initialise variables
        n = len(self.dist)
        self.table_prob = {}  # probability table
        self.table_alias = {}  # alias table
        small = []  # stack for probabilities smaller than 1
        large = []  # stack for probabilities greater than or equal to 1

        # Construct and sort the scaled probabilities into their appropriate stacks
        for o, p in self.dist.items():
            self.table_prob[o] = float(p) * n

            if self.table_prob[o] < 1:
                small.append(o)
            else:
                large.append(o)

        # Construct the probability and alias tables
        while small and large:
            s = small.pop()
            l = large.pop()

            self.table_alias[s] = l

            self.table_prob[l] = (self.table_prob[l] + self.table_prob[s]) - float(1)

            if self.table_prob[l] < 1:
                small.append(l)
            else:
                large.append(l)

        # The remaining outcomes (of one stack) must have probability 1
        while large:
            self.table_prob[large.pop()] = float(1)

        while small:
            self.table_prob[small.pop()] = float(1)

        log.info("End alias_initialisation() function")

    def alias_generation(self):
        """ Return a random outcome """
        log.info("Starting alias_generation() function")
        # Determine which column of table_prob to inspect
        col = random.choice(self.table_prob_list)

        # Determine which outcome to pick in that column
        log.info("Starting alias_generation() function")
        if self.table_prob[col] >= random.uniform(0, 1):
            return col
        else:
            return self.table_alias[col]

