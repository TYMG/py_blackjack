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
        pass


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
            pass
        else:
            self.curr_val += card.value


class Game:

    def __init__(self):
        self.player = None
        self.deck = None

    def start_game(self):
        '''
        1. Create Player (starts with $50)
        2. Play Game Until Player Quits
        3. Create a Hand, 
        '''
        print('Game Started')
        playerName = None
        while type(playerName) != str:
            try:
                playerName = input('Please enter a player\n')
            except:
                print("Please enter a name")
        self.player = Player(playerName)
        print(self.player)
