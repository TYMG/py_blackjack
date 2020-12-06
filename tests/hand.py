import unittest
from blackjack import engine


class HandTest(unittest.TestCase):

    def test_create_deck(self):
        deck = engine.Deck()
        print(deck)


if __name__ == '__main__':
    unittest.main()
