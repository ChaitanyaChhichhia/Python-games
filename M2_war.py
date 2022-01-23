# -*- coding: utf-8 -*-

from random import shuffle

suits=('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Cards():
    '''
    Creates a card of the given suit and rank
    Parameters:
        suit- suit of the card
        rank- rank of the card
    '''
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():
    '''
    Creates  a deck of cards using the 'cards' class
    Parameters:
        None
    '''    
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Cards(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
    def __len__(self):
        return len(self.all_cards)


class Player():
    '''
    Adds/removes cards in the deck of a player
    Parameters:
        name- Name of the player
    '''
    
    def __init__(self, name):
        self.name=name
        self.player_cards_in_hand=[]    
            #list of class 'cards' held by a player
    
    def remove_card(self):
        return self.player_cards_in_hand.pop(0) 
            #pick card from the top
    
    def add_cards(self, new_cards):
        # add the cards at the bottom (end of the list)
        if (type(new_cards)==type([])): 
            #if multiple cards are to be added
            self.player_cards_in_hand.extend(new_cards)
        else:
            self.player_cards_in_hand.append(new_cards)
            
    def __str__(self):
        return f'{self.name} has {len(self.player_cards_in_hand)} cards.'
    
########################################################################  
#Game Setup

player1=Player("One")
player2=Player("Two")

deck_of_cards=Deck()
deck_of_cards.shuffle()

    #distributing the shuffled cards
for i in range (26):
    player1.add_cards(deck_of_cards.deal_one())
    player2.add_cards(deck_of_cards.deal_one())


game_on=True

round_no=0
while game_on:
    round_no+=1
    print (f"Round {round_no}")
    
    if len(player1.player_cards_in_hand)==0:
        print(f"{player1.name} is out of cards. {player2.name} won the game!!")
        game_on=False
        break
    if len(player2.player_cards_in_hand)==0:
        print(f"{player2.name} is out of cards. {player1.name} won the game!!")
        game_on=False
        break
    
    player1_cards_on_table=[]
    player1_cards_on_table.append(player1.remove_card())
    
    player2_cards_on_table=[]
    player2_cards_on_table.append(player2.remove_card())

    at_war=True
    
    while at_war:
        
        if (player1_cards_on_table[-1].value > player2_cards_on_table[-1].value):
            player1.add_cards(player1_cards_on_table)
            player1.add_cards(player2_cards_on_table)
            at_war=False
            
        elif (player1_cards_on_table[-1].value < player2_cards_on_table[-1].value):
            player2.add_cards(player1_cards_on_table)
            player2.add_cards(player2_cards_on_table)
            at_war=False
            
        else:
            print("War !!")
            
            if (len(player1.player_cards_in_hand) < 5):
                print(f"{player1.name} is out of Cards. {player2.name} won the game at WAR!!")
                game_on=False
                break
            elif (len(player2.player_cards_in_hand) < 5):
                print(f"{player2.name} is out of Cards. {player1.name} won the game at WAR!!")
                game_on=False
                break
            else:
                #get 5 cards form each player on the table
                for j in range(5):
                    player1_cards_on_table.append(player1.remove_card())
                    player2_cards_on_table.append(player2.remove_card())
