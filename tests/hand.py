import unittest
from blackjack import engine


class HandTestEngine(unittest.TestCase):

    def test_deal_hand(self):
        deck = engine.Deck()
        hand = engine.Hand()
        hand.add_card(deck.deal())
        print(hand.display_hand())

    def test_deal_hands(self):
        print('\n'+'*****'*20)
        print('Test: Dealing Cards to Player and Dealer\n')
        deck = engine.Deck()
        player_hand = engine.Hand()
        dealer = engine.Hand()

        player_hand.add_card(deck.deal())
        dealer.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        dealer.add_card(deck.deal())
        print('Reveal Hands')
        print("Player Hand\n" + player_hand.display_hand())
        print("Dealer Hand\n" + dealer.display_hand(True))

    def test_display_val(self):
        print('\n'+'*****'*20)
        print('Test: Display Value of Cards Dealtto Player\n')
        deck = engine.Deck()
        player_hand = engine.Hand()

        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        print("Player Hand\n" + player_hand.display_hand()+'\n')
        print(player_hand.display_value())

    def test_rand_display_val(self):
        print('\n'+'*****'*20)
        print('Test: Display Value of Random Cards Dealt to Player\n')
        deck = engine.Deck()
        deck.shuffle()
        player_hand = engine.Hand()

        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        print("Player Hand\n" + player_hand.display_hand()+'\n')
        print(player_hand.display_value())

    def test_handle_ace(self):
        print('\n'+'*****'*20)
        print('Test: Test Handle Ace Method\n')
        deck = engine.Deck()
        player_hand = engine.Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        print("Player Hand\n" + player_hand.display_hand()+'\n')
        player_hand.handle_ace()
        self.assertTrue(player_hand.curr_val ==
                        21 or player_hand.curr_val == 11)


if __name__ == '__main__':
    unittest.main()
