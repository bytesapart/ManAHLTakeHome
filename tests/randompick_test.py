import unittest
import random
import sys
import os


class RandomPickTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        random.seed(42)

    def setUp(self) -> None:
        self.numbers = [1, 2, 3]
        self.probabilities = [[0.1, 0.8, 0.1], [0.33, 0.33, 0.34], [0.25, 0.5, 0.25]]
        sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

    def test_naive_method_once(self):
        import randompick
        probabilities = self.probabilities[0]
        random_obj = randompick.RandomGen(self.numbers, probabilities)
        naive_value = random_obj.naive_random_pick()
        self.assertEqual(naive_value, 2)

    def test_naive_method_one_hundred(self):
        import randompick
        probabilities = self.probabilities[0]
        random_obj = randompick.RandomGen(self.numbers, probabilities)
        naive_value = [random_obj.naive_random_pick() for i in range(100)]
        self.assertEqual(naive_value.count(1), 12)
        self.assertEqual(naive_value.count(2), 76)
        self.assertEqual(naive_value.count(3), 12)

    def test_efficient_method_linear_search_once(self):
        import randompick
        random_objs = [randompick.RandomGen(self.numbers, probability) for probability in self.probabilities]
        value = [random_obj.efficient_random_pick(use_binary_search=False) for random_obj in random_objs]
        self.assertEqual(value[0], 2)
        self.assertEqual(value[1], 2)
        self.assertEqual(value[2], 3)

    def test_efficient_method_linear_search_one_hundred(self):
        import randompick
        random_objs = [randompick.RandomGen(self.numbers, probability) for probability in self.probabilities]
        value_0 = [random_objs[0].efficient_random_pick(use_binary_search=False) for i in range(100)]
        value_1 = [random_objs[1].efficient_random_pick(use_binary_search=False) for i in range(100)]
        value_2 = [random_objs[2].efficient_random_pick(use_binary_search=False) for i in range(100)]

        count_value_0 = [value_0.count(1), value_0.count(2), value_0.count(3)]
        count_value_1 = [value_1.count(1), value_1.count(2), value_1.count(3)]
        count_value_2 = [value_2.count(1), value_2.count(2), value_2.count(3)]

        self.assertEqual(count_value_0, [10, 76, 14])
        self.assertEqual(count_value_1, [31, 34, 35])
        self.assertEqual(count_value_2, [22, 55, 23])

    def test_efficient_method_binary_search_once(self):
        import randompick
        random_objs = [randompick.RandomGen(self.numbers, probability) for probability in self.probabilities]
        naive_value = [random_obj.efficient_random_pick(use_binary_search=True) for random_obj in random_objs]
        self.assertEqual(naive_value[0], 3)
        self.assertEqual(naive_value[1], 2)
        self.assertEqual(naive_value[2], 3)

    def test_efficient_method_binary_search_one_hundred(self):
        import randompick
        random_objs = [randompick.RandomGen(self.numbers, probability) for probability in self.probabilities]
        value_0 = [random_objs[0].efficient_random_pick(use_binary_search=True) for i in range(100)]
        value_1 = [random_objs[1].efficient_random_pick(use_binary_search=True) for i in range(100)]
        value_2 = [random_objs[2].efficient_random_pick(use_binary_search=True) for i in range(100)]

        count_value_0 = [value_0.count(1), value_0.count(2), value_0.count(3)]
        count_value_1 = [value_1.count(1), value_1.count(2), value_1.count(3)]
        count_value_2 = [value_2.count(1), value_2.count(2), value_2.count(3)]

        self.assertEqual(count_value_0, [8, 82, 10])
        self.assertEqual(count_value_1, [42, 30, 28])
        self.assertEqual(count_value_2, [24, 49, 27])

    def test_alias_method_once(self):
        import randompick
        random_objs = [randompick.RandomGen(self.numbers, probability) for probability in self.probabilities]
        naive_value = [random_obj.alias_method() for random_obj in random_objs]
        self.assertEqual(naive_value[0], 3)
        self.assertEqual(naive_value[1], 3)
        self.assertEqual(naive_value[2], 1)

    def test_alias_method_one_hundred(self):
        import randompick
        random_objs = [randompick.RandomGen(self.numbers, probability) for probability in self.probabilities]
        value_0 = [random_objs[0].alias_method() for i in range(100)]
        value_1 = [random_objs[1].alias_method() for i in range(100)]
        value_2 = [random_objs[2].alias_method() for i in range(100)]

        count_value_0 = [value_0.count(1), value_0.count(2), value_0.count(3)]
        count_value_1 = [value_1.count(1), value_1.count(2), value_1.count(3)]
        count_value_2 = [value_2.count(1), value_2.count(2), value_2.count(3)]

        self.assertEqual(count_value_0, [8, 80, 12])
        self.assertEqual(count_value_1, [40, 31, 29])
        self.assertEqual(count_value_2, [25, 49, 26])


if __name__ == '__main__':
    unittest.main()
