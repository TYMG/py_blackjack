from blackjack import engine

'''
Python Blackjack Game
'''


def main():
    print('Starting a game of Blackjack')
    curr_game = engine.Game()
    curr_game.start_game()


if __name__ == "__main__":
    main()
