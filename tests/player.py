import unittest
from blackjack import engine


class PlayerTestEngine(unittest.TestCase):
    def test_create_player(self):
        print('\n'+'*****'*20)
        player = engine.Player("test")
        print(player)

    def test_update_money_positive(self):
        print('\n'+'*****'*20)
        player = engine.Player("test")
        print(player)
        player.update_money(50)
        print(player)

    def test_update_money_negative(self):
        print('\n'+'*****'*20)
        print("Testing Taking Money")
        player = engine.Player("test")
        print(player)
        player.update_money(50*-1)
        print(player)


if __name__ == '__main__':
    unittest.main()
