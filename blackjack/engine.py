import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return ('\n').join([card.__str__() for card in self.deck])

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.money = 50

    def __str__(self):
        return f"Player Name: {self.name}, and current money: ${self.money}"


class Hand:

    def __init__(self):
        self.cards = []
        self.curr_val = 0
        self.contain_ace = False
        self.bet = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'Ace':
            self.contain_ace = True
        self.curr_val += card.value

    def handle_ace(self):
        val = self.curr_val
        lo = val-10
        hi = val
        updated_curr_val = None
        if hi < 21:
            while updated_curr_val != lo and updated_curr_val != hi:
                updated_curr_val = int(input(f'Select a val {lo} or {hi}\n'))
                print(updated_curr_val)
                if updated_curr_val != lo and updated_curr_val != hi:
                    print('Incorrect Value\n')
        else:
            self.contain_ace = False
            updated_curr_val = lo
        self.curr_val = updated_curr_val
        print(f'Current hand value: {self.curr_val}')

    def make_bet(self, player, bet_amt):
        if player.money > bet_amt:
            print(f"Bet Made: ${bet_amt}")
            self.bet += bet_amt
        else:
            raise ValueError("Insufficient Funds")

    def display_hand(self, hide_cards=False):
        display = ''
        if hide_cards == False:
            display = '\n'.join([card.__str__() for card in self.cards])
        else:
            display = self.cards[1].__str__()
        return display

    # What about multiple  aces???
    def display_value(self):
        display = ''
        val = 0
        if self.contain_ace:
            for card in self.cards:
                if card.rank != 'Ace':
                    val += card.value
            print(val)
            display = f'Value is either {val-10} or {val}'
        else:
            for card in self.cards:
                val += card.value
            display = f'Value is {val}'
        return display


class Game:

    def __init__(self):
        self.player = None
        self.deck = None
        self.hand = 1

    def start_game(self):
        '''
        1. Create Player (starts with $50)
        2. Play Game Until Player Quits
        3. Create a Hand,
        '''
        print('Game Started')
        playerName = None
        game_on = True
        while type(playerName) != str:
            try:
                playerName = input('Please enter a player\n')
            except:
                print("Please enter a name")
        self.player = Player(playerName)
        print(self.player)
        self.deck = Deck()
        while game_on:
            game_on = self.play_hand()

    def play_hand(self):
        self.deck.shuffle()
        dealer = Hand()
        player_hand = Hand()
        while True:
            try:
                bet_amt = int(input("Please Enter A Bet:\n"))
                player_hand.make_bet(self.player, bet_amt)
            except:
                print("Invalid bet amount")
                continue
            else:
                break
        print('Dealing Cards....')
        player_hand.add_card(self.deck.deal())
        dealer.add_card(self.deck.deal())
        player_hand.add_card(self.deck.deal())
        dealer.add_card(self.deck.deal())
        print('Reveal Hands')
        print(dealer.display_hand(True))
        print(player_hand.display_hand())
        print(player_hand.display_value())
        self.player_take_cards(player_hand)
        print(player_hand.display_hand() +
              f"\nPlayer stands at {player_hand.curr_val}")
        return False

    def hit_question(self, hand):
        resp = input(
            f'Do you want to hit? Current Val: {hand.curr_val} (Yes or No)\n')
        while resp != 'Yes' and resp != 'No':
            resp = input(
                f'Incorrect Response\nDo you want to hit? Current Val: {hand.curr_val} (Yes or No)\n')
        return resp

    def player_take_cards(self, hand):
        while hand.curr_val < 21:
            resp = self.hit_question(hand)
            if resp == 'No':
                break
            card = self.deck.deal()
            print(card)
            hand.add_card(card)
            if hand.contain_ace == True:
                hand.handle_ace()
            print(f'Current Val: {hand.curr_val}\n')

    def dealer_take_cards(self, dealer):
        while dealer.curr_val < 17:
            card = self.deck.deal()
            if dealer.curr_val + card.value > 21 and dealer.contain_ace == True:
                dealer.curr_val -= 10
                dealer.add_card(card)
                dealer.contain_ace = False
            else:
                dealer.add_card(card)
            print(f'Dealer Value {dealer.curr_val}')
