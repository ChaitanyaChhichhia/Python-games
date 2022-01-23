# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 22:10:29 2021

@author: Chaitanya Chhihhia
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing=True

class Cards():
    
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit
        self.value=values[rank]
        
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
    
    
class Deck():
    
    def __init__(self):
        self.all_cards=[]
        for rank in ranks:       # Creating the deck of cards
            for suit in suits:
                self.all_cards.append(Cards(rank, suit))

    def __len__(self):
        return len(self.all_cards)
    
    def shuffle(self):
        random.shuffle (self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
    def __str__(self):           # Lists all the cards in deck (for debugging purpose)
        cards_in_deck_str=''
        for card in self.all_cards:
            cards_in_deck_str+= '\n' + card.__str__()
        return "The deck has-"+cards_in_deck_str
    

class Hand():
    '''
    holds the cards of a player
    parameters:
        card-of class Card()
    '''
    def __init__(self):
        self.value=0             # value is the sum of cards in hand
        self.aces=0              # aces =1 or 11 to be decided
        self.cards_in_hand=[]    # list of Cards with the player
    
    def add_card(self, card):    # adds card and its value to player's hand
        self.cards_in_hand.append(card)
        self.value+=card.value
    
    def __str__(self):           # lists the card that the player has
        cards_in_hand_str=''
        for card in self.cards_in_hand:
            cards_in_hand_str= cards_in_hand_str + ', ' + card.__str__()
        return "The player has-"+cards_in_hand_str
    
    def adjust_for_ace(self):    # decides whether ace =1 or ace = 11
        while self.value>21 and self.aces>0:
            self.value-=10      #remove 11 and add 1
            self.aces-=1        #remove the count of adjusted ace
            

class Chips():
    '''
    It holds the no. of chips with a player
    parameters:
        none
    '''
    def __init__(self,  initial_chips=100):
        self.total=initial_chips
        self.bet=0
        
    def win(self):
        self.total+=self.bet
    
    def loose(self):
        self.total-=self.bet
        
        
def take_bet(chips):
    '''
    Parameters
    ----------
    chips : Chips
        accepts the amount of bet by a player.

    Returns
    -------
    None.

    '''
    while True:
        try:
            chips.bet=int (input("Please enter your bet : "))
        except:
            print("Enter a valid bet")
        else:
            if (chips.total<chips.bet):
                print("Not enough chips! You have {} chips only".format(chips.total))
            else:
                break;


def hit(deck, hand):
    '''
    Parameters
    ----------
    deck : Deck
        deck of cards with the dealer (of Card class)
    hand : Hand 
        cards with the player/dealer
    Returns
    -------
    None.

    '''
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()
    
    
def hit_or_stand(deck, hand):
    '''
    Parameters
    ----------
    deck : Deck
        deck of cards with the dealer
    hand : Hand
        
    Returns
    -------
    None.

    '''
    global playing
    
    while True:
        hs=input("Do you want to hit or stand (h/s)? ")
        
        if hs[0].lower() == 'h':
            hit (deck, hand)
            playing = True
        
        elif hs[0].lower() == 's':
            print ("The player stands, Dealer's turn.")
            playing = False
        
        else:
            continue
        
        break
    
    
def show_some (dealer, player):
    '''
    Parameters
    ----------
    dealer : Hand
        DESCRIPTION.
    hand : Hand
        DESCRIPTION.
    Shows one card in dealer's hand and all cards in player's hand
    
    Returns
    -------
    None.

    '''
    print (f"Dealer's one card : {dealer.cards_in_hand[1]}")    #displays the top card out of the two cards initially with the dealer
    
    print("Player's cards : {}, {} " .format(player.cards_in_hand[0], player.cards_in_hand[1]))
    print (f"Player's cards' value : {player.value}")
    
    
def show_all (dealer, player):
    '''
    Parameters
    ----------
    dealer : Hand
        DESCRIPTION.
    hand : Hand
        DESCRIPTION.
    Shows all card in dealer's hand and all cards in player's hand
    also shows the value (net sum of all cards in the hands)
    
    Returns
    -------
    None.

    '''
    #print ("Dealer's cards : ", *dealer.cards_in_hand)    #displays the top card out of the two cards initially with the dealer
    print("Player's cards : {}, {} " .format(dealer.cards_in_hand[0], dealer.cards_in_hand[1]))
    print (f"Dealer's cards' value : {dealer.value}")
    
    #print("Player's cards : ", *player.cards_in_hand)
    print("Player's cards : {}, {} " .format(player.cards_in_hand[0], player.cards_in_hand[1]))
    print (f"Player's cards' value : {player.value}")
    
    
def player_busts(player, dealer, chips):
    print ("Player Bust!!")
    chips.loose()
    
    
def player_wins(player, dealer, chips):
    print ("Player Wins!!")
    chips.win()
    
    
def dealer_busts(player, dealer, chips):
    print ("Dealer Bust!!")
    chips.loose()
    
    
def dealer_wins(player, dealer, chips):
    print ("Dealer Bust!!")
    chips.win()
    
    
def push(player, dealer):
    print ("It's a tie. Push!")
    

###############################################
#Game play

while True:
    # Print an opening statement
    print("Welcome to the game of Blackjack")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand()
    
    #geve two cards to the dealer and player
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
    
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(dealer_hand, player_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(dealer_hand, player_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value<=21:
        
        while True:
            if (dealer_hand.value<17):
                hit(deck, dealer_hand)
            else:
                break
            
        # Show all cards
        show_all(dealer_hand, player_hand)
        
        # Run different winning scenarios
        if (dealer_hand.value > 21):
            dealer_busts(player_hand, dealer_hand, player_chips)
            
        elif (player_hand.value > dealer_hand.value):
            player_wins(player_hand, dealer_hand, player_chips)
            
        elif (player_hand.value < dealer_hand.value):
            dealer_wins(player_hand, dealer_hand, player_chips)
            
        else:
            push(player_hand, dealer_hand)
    
    # Inform Player of their chips total 
    print(f"Player's chip total : {player_chips.total}")
    
    # Ask to play again
        
    p = input("Would you like to play again, y or n? ")
    if p[0].lower()=='y':
        playing=True
        continue
    else:
        print("Hope you enjoyed...")
        break
