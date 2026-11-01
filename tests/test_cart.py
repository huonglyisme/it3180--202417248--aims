import unittest
from types import SimpleNamespace

from aims.cart import Cart


class TestCartLimit(unittest.TestCase):

    def test_accepts_20_dvds(self):
        cart = Cart()

        for i in range(20):
            dvd = SimpleNamespace(title=f"DVD {i}", cost=10)
            self.assertTrue(cart.add_dvd(dvd))

        self.assertEqual(len(cart.items), 20)

    def test_rejects_21st_dvd(self):
        cart = Cart()

        for i in range(20):
            dvd = SimpleNamespace(title=f"DVD {i}", cost=10)
            cart.add_dvd(dvd)

        extra = SimpleNamespace(title="DVD 21", cost=10)

        self.assertFalse(cart.add_dvd(extra))
        self.assertEqual(len(cart.items), 20)


if __name__ == "__main__":
    unittest.main()
