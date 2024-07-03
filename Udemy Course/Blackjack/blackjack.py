import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

class Hand():
    def __init__(self):
        self.cards = [] # cartas de mi mano
        self.value = 0 #valor de mi mano
        self.aces = 0 # ases con valor 11
    
    def add_card(self, card):
        self.cards.append(card) # guardamos la carta
        self.value += values[card.rank] # guardamos el valor de la mano
        
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # si tengo +21 puntos y tengo ases en mi mano los convierto en 1s en vez de 11s
        # así rebajo el valor de mi mano y puedo pedir mas cartas
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def __str__(self):
        cartas_mano = ""
        for card in self.cards:
            cartas_mano += card.__str__() + ', '
        return cartas_mano
    
class Chips:
    def __init__(self):
        self.total = 100 # fichas iniciales del user
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
    
def take_bet(player_chips):
    bet = ''
    while bet.isdigit() == False or int(bet) > player_chips.total:
        bet = input("Introduce your bet? ")
        
        if bet.isdigit() == False:
            print("Invalid input. Please enter a number")
        elif int(bet) > player_chips.total:
            print(f"Please enter a correct amount of chips. Available chips: {player_chips.total}")
        else:
            player_chips.bet = int(bet)
            return player_chips
    


def hit(deck,hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()
    
def hit_or_stand(deck, hand):
    global playing 
    while playing:
        opcion = input("1. Hit or 2. Stand? ")
        if opcion == "1":
            hit(deck, hand)
        elif opcion == "2":
            playing = False
        else:
            print("Option invalid. Try again")
            continue

def show_some(player,dealer):
    print("\nDealer's Hand")
    print(dealer.cards[1])

    print("\nPlayer's Hand")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("\nDealer's Hand")
    for card in dealer.cards:
        print(card)
    print(f"Dealer's hand value: {dealer.value}")
    
    print("\nPlayer's Hand", *player.cards, sep=",")
    print(f"Player's hand value: {player.value}")
    
    
def player_busts(player,dealer, chips):
    if player.value > 21:
        print(f"Busted! You have {player.value} points")
        print(f"Dealer has {dealer.value} points")
        print(f"Dealer wins!")
        chips.lose_bet()

def player_wins(player,dealer, chips):
    if player.value > dealer.value and player.value <= 21:
        print(f"Player has {player.value} points")
        print(f"Dealer has {dealer.value} points")
        print(f"Player wins!")
        chips.win_bet()

def dealer_busts(player,dealer, chips):
    if dealer.value > 21:
        print(f"Busted! Dealer has {dealer.value} points")
        print(f"Player has {player.value} points")
        print(f"Player wins!")
        chips.win_bet()
    
def dealer_wins(player,dealer, chips):
    if dealer.value > player.value and dealer.value <= 21:
        print(f"Dealer has {dealer.value} points")
        print(f"Player has {player.value} points")
        print(f"Dealer wins!")
        chips.lose_bet()
    
def push(player,dealer):
    if player.value == dealer.value and player.value <= 21:
        print(f"Player has {player.value} points")
        print(f"Dealer has {dealer.value} points")
        print(f"Player and dealer tie! PUSH")       
    


# empieza la partida
playing = True
while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    deck = Deck() # creamos la baraja
    deck.shuffle() # barajamos

    # inicializamos las manos de los jugadores
    player_hand = Hand()
    dealer_hand = Hand()
    
    for _ in range(2): # 2 cartas para cada jugador
        player_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

    # inicializamos las fichas del jugador
    player_chips = Chips()
    
    # el jugador apuesta
    take_bet(player_chips)
    
    #enseñamos las cartas iniciales (1 dealer, 2 el player)
    show_some(player_hand, dealer_hand)
    
    while playing:
        # el jugador pide o para
        hit_or_stand(deck,player_hand)
        
        # muestra las cartas
        show_some(player_hand, dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand, player_chips)
            break
            
    if player_hand.value <= 21:
        # el dealer pide cartas hasta superas los 17 puntos
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        
        show_all(player_hand, dealer_hand)

        # check de puntos para elegir el ganador
        if dealer_hand.value > 21:
            dealer_busts(dealer_hand,player_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand,)
            
    print("\nPlayer's winnings stand at",player_chips.total)

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
                
