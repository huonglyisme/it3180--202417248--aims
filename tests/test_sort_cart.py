import unittest
from types import SimpleNamespace
from aims.cart import Cart


class TestSortCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.cart.items = [
            SimpleNamespace(title="Zebra", cost=10),
            SimpleNamespace(title="Alpha", cost=30),
            SimpleNamespace(title="Beta", cost=20),
        ]

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        titles = [dvd.title for dvd in self.cart.items]
        self.assertEqual(titles, ["Alpha", "Beta", "Zebra"])

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        costs = [dvd.cost for dvd in self.cart.items]
        self.assertEqual(costs, [10, 20, 30])


if __name__ == "__main__":
    unittest.main()
