import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCIDemo(unittest.TestCase):

    def test_total_cost(self):
        cart = Cart()

        cart.add_dvd(
            DigitalVideoDisc("The Lion King", "Animation",
                             "Roger Allers", 87, 19.95)
        )

        cart.add_dvd(
            DigitalVideoDisc("Star Wars", "Science Fiction",
                             "George Lucas", 87, 24.95)
        )

        self.assertAlmostEqual(cart.total_cost(), 44.90)


if __name__ == "__main__":
    unittest.main()
