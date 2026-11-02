import unittest
from types import SimpleNamespace
from aims.search import search_by_title


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.items = [
            SimpleNamespace(title="The Lion King"),
            SimpleNamespace(title="Star Wars")
        ]

    def test_search_lowercase(self):
        result = search_by_title(self.items, "lion")
        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King"]
        )

    def test_search_uppercase(self):
        result = search_by_title(self.items, "STAR")
        self.assertEqual(
            [dvd.title for dvd in result],
            ["Star Wars"]
        )


if __name__ == "__main__":
    unittest.main()
