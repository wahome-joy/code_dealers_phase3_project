import random
from scores import register_win,register_loss,check_score

def main (name):
    
    print(f"Hey, {name} Welcome to blackjack!")
    start_game()
    return ""
def start_game():
    start = input("To start game, press enter: ")
    if start == "":
        play()
    else:
        print("Invalid input")
    return 
  
    
cards =[2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'A',2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'A',2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'A']
downside_up_card = "?"
total_dealer_points = list()
total_player_points = list()
player_cards=[random.choice(cards),random.choice(cards)]
dealer_cards = [random.choice(cards), downside_up_card]
def play():
    for card in dealer_cards:
        my_points = int(points(card))
        total_dealer_points.append(my_points)
    for card in player_cards:
        my_points = int(points(card))
        total_player_points.append(my_points)
    
    print(f"Dealer's cards : {[dealer_cards]}  Total points= {sum(total_dealer_points)}")
    print(f"Your cards : {[player_cards]} Total points= {sum(total_player_points)}")
    win_lose(sum(total_dealer_points),sum(total_player_points))


def points(card):
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'A':
        return 11
    elif card == '2' or card == '3' or card == '4' or card == '5' or card == '6' or card == '7' or card == '8' or card == '9':
        return int(card)
    elif card == '?':
        return 0
    else:
        return card
    
def deal():
    global total_dealer_points
    global total_player_points
    player_cards.append(random.choice(cards)) 
    total_player_points = list()
    for card in player_cards:
        my_points = int(points(card))
        total_player_points.append(my_points)
    total_dealer_points = list()
    for card in dealer_cards:
        my_points = int(points(card))
        total_dealer_points.append(my_points)

    print(f"Dealer's cards : {[dealer_cards]}  Total points= {sum(total_dealer_points)}")
    print(f"Your cards : {[player_cards]} Total points= {sum(total_player_points)}")
    win_lose(sum(total_dealer_points),sum(total_player_points))

def stand():
    global total_dealer_points
    global total_player_points

    if  downside_up_card in dealer_cards: 
        dealer_cards.remove (downside_up_card) 
        dealer_cards.append(random.choice(cards))       
        total_dealer_points = list()
        for card in dealer_cards:
            my_points = int(points(card))
            total_dealer_points.append(my_points)
    else:
        dealer_cards.append(random.choice(cards))
        total_dealer_points = list()
        for card in dealer_cards:
            my_points = int(points(card))
            total_dealer_points.append(my_points)        

    print(f"Dealer's cards : {[dealer_cards]}  Total points= {sum(total_dealer_points)}")
    print(f"Your cards : {[player_cards]} Total points= {sum(total_player_points)}")
    win_lose(sum(total_dealer_points),sum(total_player_points))        
#class Report:

def win_lose(dealer_points,player_points):
    global total_dealer_points
    global total_player_points   
    global dealer_cards
    global player_cards


    if dealer_points > 21 or player_points == 21: 

        print (f"Congats {load_current_user()}! You win with {player_points} points")
        register_win(load_current_user())
        print (f"Your Total score is {check_score(load_current_user())}")
        start_new_or_quit = input("To play again, type enter: To quit type quit: ")
        if start_new_or_quit == "":
            play_again()
        elif start_new_or_quit == "quit":
            quit()
        else:
            print("Invalid input")


    elif player_points > 21 or dealer_points == 21:
        total_dealer_points = list()
        total_player_points=  list()
        print ("You lose")
        register_loss(load_current_user())
        print (f"Your Total score is {check_score(load_current_user())}")
        start_new_or_quit = input("To play again, press enter: To quit type quit: ")
        if start_new_or_quit == "":
            play_again()
        elif start_new_or_quit == "quit":
            quit()
        else:
            print("Invalid input")

    else:
        hit_or_stand()
def play_again():
    global total_dealer_points
    global total_player_points
    global player_cards
    global dealer_cards
    total_dealer_points = list()
    total_player_points = list()
    player_cards=[random.choice(cards),random.choice(cards)]
    dealer_cards = [random.choice(cards), downside_up_card]
    for card in dealer_cards:
        my_points = int(points(card))
        total_dealer_points.append(my_points)
    for card in player_cards:
        my_points = int(points(card))
        total_player_points.append(my_points)
    
    print(f"Dealer's cards : {[dealer_cards]}  Total points= {sum(total_dealer_points)}")
    print(f"Your cards : {[player_cards]} Total points= {sum(total_player_points)}")
    win_lose(sum(total_dealer_points),sum(total_player_points))    

def hit_or_stand():
    choose_option = input("to hit, type hit, to stand, type stand: ")
    if choose_option == "hit":
        deal()
    elif choose_option == "stand":
        stand()

def load_current_user():
    with open("current_user.txt", "r") as file:
        user_name = file.read()
    return user_name

