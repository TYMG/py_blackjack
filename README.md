# py_blackjack

A Python Implementation of the game Blackjack

<p>
To play a hand of Blackjack the following steps must be followed:

Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again

</p>

Running a single test module:

To run a single test module, in this case test_antigravity.py:

```
$ cd new_project
$ python -m unittest test.test_antigravity
```

Just reference the test module the same way you import it.

Running a single test case or test method:

Also you can run a single TestCase or a single test method:

```
$ python -m unittest test.test_antigravity.GravityTestCase
$ python -m unittest test.test_antigravity.GravityTestCase.test_method
Running all tests:
```

You can also use test discovery which will discover and run all the tests for you, they must be modules or packages named test\*.py (can be changed with the -p, --pattern flag):

```
$ cd new_project
$ python -m unittest discover
$ # Also works without discover for Python 3
$ # as suggested by @Burrito in the comments
$ python -m unittest
```
