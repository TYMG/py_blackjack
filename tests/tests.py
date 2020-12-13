import unittest
from blackjack import engine


class TestEngine(unittest.TestCase):

    def test_create_deck(self):
        deck = engine.Deck()
        print(deck)


if __name__ == '__main__':
    unittest.main()
