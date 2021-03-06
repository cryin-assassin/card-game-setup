import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
'Eight':8, 'Nine':9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace':14}


# Card Class
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# Deck Class
class Deck:

    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        # Pop will remove a card from list all_cards & return as an object
        return self.all_cards.pop()


# Player Class
class player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        # Will remove 1 card from the top of the list
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # Multiple Card add
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # Single card add
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


# Create a Deck obect with all cards and shuffle
new_deck = Deck()
new_deck.shuffle_deck()

# Create player objects with Names
player_one = player('Nick')
player_two = player('Paul')

# Deal the deck evenly between the 2 players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# Print the amount of cards each player has
print('Player One has %s cards' % (str(len(player_one.all_cards))))
print('Player Two has %s cards' % (str(len(player_two.all_cards))))

# Print the top card from each Players Deck
print ('Player One top card is %s' %(player_one.remove_one()))
print ('Player Two top card is %s' %(player_two.remove_one()))
