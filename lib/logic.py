from rich.console import Console
from rich.table import Table
import random
from scores import register_win, register_loss, check_score

console = Console()

def main(name):
    console.print(f"[bold green]Hey, {name}! Welcome to Blackjack![/bold green]")
    start_game()
    return ""

def start_game():
    start = input("To start the game, press enter: ")
    if start == "":
        play()
    else:
        console.print("[red]Invalid input[/red]")
    return

# Define a deck with suits
cards = [
    '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠',
    '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
    '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
    '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥'
]
downside_up_card = "?"
total_dealer_points = []
total_player_points = []
player_cards = []
dealer_cards = []

# Function to colorize a card based on its suit
def colorize_card(card):
    if "♥" in card:
        return f"[bold red]{card}[/bold red]"
    elif "♠" in card:
        return f"[bold white]{card}[/bold white]"
    elif "♣" in card:
        return f"[bold green]{card}[/bold green]"
    elif "♦" in card:
        return f"[bold blue]{card}[/bold blue]"
    else:
        return card

def initialize_game():
    global player_cards, dealer_cards, total_player_points, total_dealer_points
    player_cards = [random.choice(cards), random.choice(cards)]
    dealer_cards = [random.choice(cards), downside_up_card]
    total_player_points = [points(card) for card in player_cards]
    total_dealer_points = [points(card) for card in dealer_cards if card != downside_up_card]

def display_table():
    # Dealer's table
    dealer_table = Table(title="[bold magenta]Dealer[/bold magenta]", border_style="bright_magenta")
    dealer_table.add_column("Cards", justify="center", style="bold yellow")
    dealer_table.add_column("Total Points", justify="center", style="bold yellow")
    
    # Add each card in a separate row, total points only in the last row
    for card in dealer_cards[:-1]:
        dealer_table.add_row(colorize_card(card), "")
    dealer_table.add_row(colorize_card(dealer_cards[-1]), f"[bold green]{sum(total_dealer_points)}[/bold green]")

    # Player's table
    player_table = Table(title="[bold blue]Player[/bold blue]", border_style="bright_blue")
    player_table.add_column("Cards", justify="center", style="bold yellow")
    player_table.add_column("Total Points", justify="center", style="bold yellow")
    
    # Add each card in a separate row, total points only in the last row
    for card in player_cards[:-1]:
        player_table.add_row(colorize_card(card), "")
    player_table.add_row(colorize_card(player_cards[-1]), f"[bold green]{sum(total_player_points)}[/bold green]")

    console.print(dealer_table)
    console.print(player_table)

def play():
    initialize_game()
    display_table()
    hit_or_stand()

def points(card):
    if card[0] in ['J', 'Q', 'K']:
        return 10
    elif card[0] == 'A':
        return 11
    elif card[0].isdigit():
        return int(card[:-1])  # Correct for cards like '10♠'
    return 0

def deal():
    global total_player_points
    new_card = random.choice(cards)
    player_cards.append(new_card)
    total_player_points.append(points(new_card))
    display_table()
    if sum(total_player_points) > 21:
        win_lose(sum(total_dealer_points), sum(total_player_points))

def stand():
    global dealer_cards, total_dealer_points
    if downside_up_card in dealer_cards:
        dealer_cards.remove(downside_up_card)
    while sum(total_dealer_points) < 17:
        new_card = random.choice(cards)
        dealer_cards.append(new_card)
        total_dealer_points.append(points(new_card))
    display_table()
    win_lose(sum(total_dealer_points), sum(total_player_points))

def win_lose(dealer_points, player_points):
    player_name = load_current_user()
    if player_points > 21:
        console.print(f"[bold red] Dealer wins with {dealer_points} points![/bold red]")
    elif dealer_points > 21 or player_points > dealer_points:
        console.print(f"[bold green]Congrats! {player_name} wins with {player_points} points![/bold green]")
        register_win(player_name)
    elif dealer_points == player_points:
        console.print("[bold yellow]It's a tie![/bold yellow]")
    else:
        console.print(f"[bold red] Dealer wins with {dealer_points} points![/bold red]")
        register_loss(player_name)
    start_new_or_quit()

def start_new_or_quit():
    choice = input("Play again? (y/n): ").strip().lower()
    if choice == "y":
        play()
    else:
        console.print("[bold cyan]Thanks for playing![/bold cyan]")
        quit()

def hit_or_stand():
    while True:
        action = input("Choose an action: (hit/stand): ").strip().lower()
        if action == "hit":
            deal()
        elif action == "stand":
            stand()
            break
        else:
            console.print("[red]Invalid choice. Please type 'hit' or 'stand'.[/red]")

def load_current_user():
    with open("current_user.txt", "r") as file:
        return file.read()
