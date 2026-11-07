import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearch(unittest.TestCase):
    def test_search_by_category(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", category="Science Fiction"))
        cart.add_dvd(DigitalVideoDisc("Aladdin", category="Animation"))
        cart.add_dvd(DigitalVideoDisc("The Lion King", category="Animation"))

        result = search_by_category(cart, "Animation")

        self.assertEqual(
            [dvd.title for dvd in result],
            ["Aladdin", "The Lion King"]
        )

    def test_search_by_category_case_insensitive(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", category="Science Fiction"))

        result = search_by_category(cart, "science fiction")

        self.assertEqual([dvd.title for dvd in result], ["Star Wars"])


if __name__ == "__main__":
    unittest.main()
