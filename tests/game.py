import unittest
from blackjack import engine


class GameTestEngine(unittest.TestCase):

    def test_player_take_cards(self):
        print('\n'+'*****'*20)
        print('Test: Player Take Cards\n')
        game = engine.Game()
        deck = engine.Deck()
        game.deck = deck
        player_hand = engine.Hand()
        player_hand.add_card(deck.deal())
        card = engine.Card('Spades', 'Six')
        player_hand.add_card(card)
        print("Player Hand\n" + player_hand.display_hand()+'\n')
        game.player_take_cards(player_hand)

    def test_rand_player_take_cards(self):
        print('\n'+'*****'*20)
        print('Test: Player Take Cards\n')
        game = engine.Game()
        deck = engine.Deck()
        game.deck = deck
        deck.shuffle()
        player_hand = engine.Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        print("Player Hand\n" + player_hand.display_hand()+'\n')
        game.player_take_cards(player_hand)

    def test_dealer_take_cards(self):
        print('\n'+'*****'*20)
        print('Test: Dealer Take Cards\n')
        game = engine.Game()
        deck = engine.Deck()
        game.deck = deck
        deck.shuffle()
        dealer = engine.Hand()
        # for i in range(2):
        dealer.add_card(game.deck.deal())
        dealer.add_card(game.deck.deal())
        print("Dealer Hand\n" + dealer.display_hand()+'\n')
        game.dealer_take_cards(dealer)
        print("Updated Hand\n" + dealer.display_hand()+'\n')
        print(f'Dealer Hand\n{dealer.curr_val}\n')


if __name__ == '__main__':
    unittest.main()
