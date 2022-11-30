import logging
from typing import List, Union
import random
import alias

log = logging.getLogger('random_pick')


class RandomGen(object):

    def __init__(self, numbers, probabilities, methodology='alias'):
        """

        Parameters
        ----------
        numbers
        probabilities
        """
        self.numbers: List = numbers
        self.probabilities: List = probabilities
        self.__lookup_dictionary: dict = {'naive': self.naive_random_pick,
                                        'efficient': self.efficient_random_pick,
                                        'alias': self.alias_method}
        self._methodology = methodology

    @property
    def methodology(self):
        """
        Gets the methodology to use
        Returns
        -------
        str: The methodology to use for next_num()

        """
        return self._methodology

    @methodology.setter
    def methodology(self, methodology):
        """
        sets the methodology to use
        Parameters
        ----------
        methodology: str
            Returns the methodology to use
        Returns
        -------
        None
        """
        self._methodology = methodology

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        return self.__lookup_dictionary[self._methodology]()

    @staticmethod
    def random_pick_validation(numbers: List[Union[int, float]], probabilities: List[Union[int, float]]):
        """
        Validate numbers and probabilities
        Parameters
        ----------
        numbers: List[int, float]
            A list of numbers to choose form
        probabilities: List[int, float]
            A list of probabilities to construct a distribution for

        Returns
        -------
        None
        """
        if len(numbers) == 0:
            raise ValueError('Numbers must be a non-empty list')

        if len(probabilities) == 0:
            raise ValueError('Probabilities must be a non-empty list')

        if len(numbers) != len(probabilities):
            raise ValueError('Numbers list and their corresponding Probabilities list must be the same')

    @staticmethod
    def is_whole(d: List[Union[int, float]]):
        """
        Whether d is a whole number.
        Parameters
        ----------
        d: List[int, float]
            A list of integers and/or floats
        Returns
        -------
        bool: A boolean stating whether the floats and/or integers in the given list are whole numbers or not
        """
        return isinstance(d, int) or (isinstance(d, float) and (d * 100) % 10 == 0)

    def naive_random_pick(self):
        """
        This function accepts a numbers and a bunch of probabilitibes and returns a list
        Parameters
        Returns
        -------
        int: An integer from numbers based off of the probability that has been generated
        """
        log.info("Starting naive_random_pick() function")
        self.random_pick_validation(self.numbers, self.probabilities)

        log.info('Check for whole numbers')
        if not all(map(self.is_whole, self.probabilities)):
            raise ValueError('For naive method, all the probabilities must be whole numbers')

        log.info('Calculate choices')
        choices: List = []
        for index, weight in enumerate(self.probabilities):
            current_weight: float = 10 * weight
            choices.extend([self.numbers[index]] * int(current_weight))

        log.info("End naive_random_pick() function")
        return choices[random.randint(0, len(choices) - 1)]

    def efficient_random_pick(self, use_binary_search: float = True):
        """
        This function accepts a numbers and a bunch of probabilities and returns a number
        Parameters
        ----------
        use_binary_search: bool
            A boolean flag to indicate if one needs to use binary search for the integers or not
        Returns
        -------
        int: An integer from numbers based off of the probability that has been generated
        """
        log.info("Starting efficient_random_pick() function")
        self.random_pick_validation(self.numbers, self.probabilities)
        log.info("End efficient_random_pick() function")
        if use_binary_search is True:
            return self._efficient_random_pick_with_binary_search()
        else:
            return self._efficient_random_pick_with_linear_search()

    def _efficient_random_pick_with_linear_search(self):
        """
        This function accepts a numbers and a bunch of probabilities and returns a number, using binary search
        Parameters
        ----------

        Returns
        -------
        int: An integer from numbers based off of the probability that has been generated
        """
        log.info("Starting _efficient_random_pick_with_linear_search() function")

        cumulative_sum: float = sum(self.probabilities)
        target = cumulative_sum * random.random()

        for index, probability in enumerate(self.probabilities):
            target -= probability
            if target < 0:
                log.info("End _efficient_random_pick_with_linear_search() function")
                return self.numbers[index]

    def _efficient_random_pick_with_binary_search(self):
        """
        This function accepts a numbers and a bunch of probabilities and returns a number, using binary search
        Parameters
        ----------

        Returns
        -------
        int: An integer from numbers based off of the probability that has been generated
        """
        log.info("Starting _efficient_random_pick_with_binary_search() function")

        cumulative_accumulator: list = [0] * len(self.probabilities)
        cumulative_sum: float = sum(self.probabilities)

        for index, probability in enumerate(self.probabilities):
            if index > 0:
                cumulative_accumulator[index] = cumulative_accumulator[index - 1] + probability
            else:
                cumulative_accumulator[index] = probability

        target = cumulative_sum * random.random()
        low: int = 0
        high: int = len(self.probabilities)
        while low <= high:
            mid = low + (high - low) // 2
            if target <= cumulative_accumulator[mid]:
                if mid == 0 or (mid > 0 and target > cumulative_accumulator[mid - 1]):
                    log.info("End _efficient_random_pick_with_binary_search() function")
                    return self.numbers[mid]
                high = mid - 1
            else:
                low = mid + 1

    def alias_method(self):
        """
        This function accepts a numbers and a bunch of probabilities and returns a number, using alias method
        Parameters
        ----------

        Returns
        -------
        int: An integer from numbers based off of the probability that has been generated
        """
        log.info("Starting alias_method() function")
        alias_obj = alias.AliasMethod(dict(zip(self.numbers, self.probabilities)))
        log.info("End alias_method() function")
        return alias_obj.alias_generation()
