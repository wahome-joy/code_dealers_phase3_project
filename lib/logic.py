import random
from scores import register_win, register_loss, check_score

def main(name):
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

# Define a deck with suits
cards = [
    '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠',
    '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
    '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
    '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥'
]
downside_up_card = "?"
total_dealer_points = list()
total_player_points = list()
player_cards = [random.choice(cards), random.choice(cards)]
dealer_cards = [random.choice(cards), downside_up_card]

def play():
    for card in dealer_cards:
        my_points = int(points(card))
        total_dealer_points.append(my_points)
    for card in player_cards:
        my_points = int(points(card))
        total_player_points.append(my_points)
    
    print(f"Dealer's cards : {dealer_cards}  Total points= {sum(total_dealer_points)}")
    print(f"Your cards : {player_cards} Total points= {sum(total_player_points)}")
    win_lose(sum(total_dealer_points), sum(total_player_points))

def points(card):
    # Handle card values
    if card[0] in ['J', 'Q', 'K']:
        return 10
    elif card[0] == 'A':
        return 11
    elif card[0].isdigit():
        return int(card[0])
    elif card == '?':
        return 0
    else:
        return card

def deal():
    global total_dealer_points
    global total_player_points
    player_cards.append(random.choice(cards)) 
    total_player_points = [int(points(card)) for card in player_cards]
    total_dealer_points = [int(points(card)) for card in dealer_cards]

    print(f"Dealer's cards : {dealer_cards}  Total points= {sum(total_dealer_points)}")
    print(f"Your cards : {player_cards} Total points= {sum(total_player_points)}")
    win_lose(sum(total_dealer_points), sum(total_player_points))

def stand():
    global total_dealer_points
    global total_player_points

    if downside_up_card in dealer_cards: 
        dealer_cards.remove(downside_up_card) 
        dealer_cards.append(random.choice(cards))       
        total_dealer_points = [int(points(card)) for card in dealer_cards]
    else:
        dealer_cards.append(random.choice(cards))
        total_dealer_points = [int(points(card)) for card in dealer_cards]

    print(f"Dealer's cards : {dealer_cards}  Total points= {sum(total_dealer_points)}")
    print(f"Your cards : {player_cards} Total points= {sum(total_player_points)}")
    win_lose(sum(total_dealer_points), sum(total_player_points))

def win_lose(dealer_points, player_points):
    global total_dealer_points
    global total_player_points   
    global dealer_cards
    global player_cards

    if dealer_points > 21 or player_points == 21: 
        print(f"Congrats {load_current_user()}! You win with {player_points} points")
        register_win(load_current_user())
        print(f"Your Total score is {check_score(load_current_user())}")
        start_new_or_quit = input("To play again, type enter: To quit type quit: ")
        if start_new_or_quit == "":
            play_again()
        elif start_new_or_quit == "quit":
            quit()
        else:
            print("Invalid input")

    elif player_points > 21 or dealer_points == 21:
        total_dealer_points = []
        total_player_points = []
        print("You lose")
        register_loss(load_current_user())
        print(f"Your Total score is {check_score(load_current_user())}")
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
    total_dealer_points = []
    total_player_points = []
    player_cards = [random.choice(cards), random.choice(cards)]
    dealer_cards = [random.choice(cards), downside_up_card]
    for card in dealer_cards:
        total_dealer_points.append(int(points(card)))
    for card in player_cards:
        total_player_points.append(int(points(card)))

    print(f"Dealer's cards : {dealer_cards}  Total points= {sum(total_dealer_points)}")
    print(f"Your cards : {player_cards} Total points= {sum(total_player_points)}")
    win_lose(sum(total_dealer_points), sum(total_player_points))

def hit_or_stand():
    choose_option = input("to hit, type hit, to stand, type stand: ")
    if choose_option == "hit":
        deal()
    elif choose_option == "stand":
        stand()

def load_current_user():
    with open("current_user.txt", "r") as file:
        return file.read()
