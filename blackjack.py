#dealer class
#player Class
#deck class
#card class

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
game_on = True 

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand: 

	def __init__(self):
		self.hand = []
		self.value = 0 
		self.aces = 0

	def add_card(self, card): 
		self.hand.append(card)
		self.value = self.value + values[card.rank]

	def ace_adjust(self):
		while self.value > 21 and self.aces > 0: 
			self.value -= 10
			self.aces -= 1 

class Chips:

	def __init__(self): 
		self.total = 300
		self.bet = 0 

	def win_bet(self): 
		self.total += self.bet

	def lose_bet(self): 
		self.total += self.bet


def take_bet(chips):
	while True: 
		try:
			chips.bet = int(input("Enter your bet: "))
		except ValueError: 
			print("Sorry, a bet must be an integer!")

		else: 
			if chips.bet > chips.total: 
				print("Sorry, your bet can't exceed", chips.total)
			else:
				break 

def hit(deck, hand): 
	hand.add_card(deck.deal())
	hand.ace_adjust()

def hit_or_stand(deck, hand): 
	global playing

	while playing: 
		user_input = input("Would you like to hit or stand: (hit, stand)")

		if user_input == 'hit': 
			hit(deck, hand) 
			print(f"Player hits")

		elif user_input == 'stand': 
			print(f"Player stands, Dealer is now playing")
			playing = False 

		else: 
			print("type in the correct input please")
			continue 
		break 


#functions
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.hand[1])  
    print("\nPlayer's Hand:", *player.hand, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.hand, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.hand, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")





#game 

while game_on: 
	print("Welcome to Bobby K's Casino, lets play BlackJack bruh!\n\n\n\n")

	game_deck = Deck() #game_deck object of deck class
	game_deck.shuffle() #shuffle the deck before the game

	player_chips = Chips()  #create instance of player one chips

	
	print("Place blind bet player1 ")
	take_bet(player_chips)

	print("Dealer deals two cards to himself and the player")
	player_hand = Hand()
	dealer_hand = Hand() 

	player_hand.add_card(game_deck.deal())
	player_hand.add_card(game_deck.deal())
	dealer_hand.add_card(game_deck.deal())
	dealer_hand.add_card(game_deck.deal())

	show_some(player_hand, dealer_hand)

	while playing: #player hit or stand loop,

		hit_or_stand(game_deck, player_hand) 

		show_some(player_hand, dealer_hand)

		if player_hand.value == 21:
			player_wins(player_hand, dealer_hand, player_chips)
			playing = False

		elif player_hand.value > 21: 
			player_busts(player_hand, dealer_hand, player_chips)
			dealer_wins(playing_hand, dealer_hand, player_chips)
			playing = False

	while player_hand.value < 21 and dealer_hand.value < 17: #after player hit or stand, dealer does his hit loop
		hit(game_deck, dealer_hand)

	show_all(player_hand, dealer_hand)

	#win conditions 

	if dealer_hand.value == 21:
		dealer_wins(player_hand, dealer_hand, player_chips)

	elif dealer_hand.value > 21: 
		dealer_busts(player_hand, dealer_hand, player_chips)

	elif player_hand.value> 

	elif dealer_hand.value > player_hand.value: 
		dealer_wins(player_hand, dealer_hand, player_chips)

	elif dealer_hand.value < player_hand.value: 
		player_wins(player_hand, dealer_hand, player_chips)

	else: 
		push(player_hand, dealer_hand)

	print(f"The players cash is currently: {player_chips.total}")

	user_new = input("Would you like to play again: (yes or no)")

	if user_new == "yes": 
		playing = True 
		continue 

	else: 
		print("Goodbye!!")
		quit() 












	 













	


