import unittest
from aims.discount import discounted_total


class TestDiscount(unittest.TestCase):

    def test_discount_20_percent(self):
        self.assertEqual(discounted_total(100, 20), 80)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            discounted_total(100, 150)


if __name__ == "__main__":
    unittest.main()
