# CODE-DEALERS_PYTHON_PROJECT

## CONTRIBUTORS:
1. James Maroko
2. Hosea Mungai
3. Joy Wahome
4. Titus Kipchirchir


# OVERVIEW
Welcome to the Blackjack Game! This is a simple implementation of the classic card game Blackjack (also known as 21), built using Python. The project simulates a card game between a player and a dealer, following standard Blackjack rules. It is designed using object-oriented programming (OOP) principles for ease of maintenance and scalability.

# KEY FEATURES
- Object-Oriented Design
- Text-based interface
- Multiple players can be added in future versions
- Core components like deck management, hand calculations, player actions, and game flow are implemented in separate modules

# TABLE OF CONTENTS
1. Project Structure
2. Installation Instructions
3. Usage
4. Gameplay Rules
5. Testing
6. Technologies used
7. Contact
8. License


## PROJECT STRUCTURE

. 
├── blackjack.db
├──current_user.txt
├──lib
|  ├─game.py
|  ├──helpers.py
|  ├──logic.py
|  ├──pycache_
|  |___scores.py
├──logs.txt
├──Pipfile
├──Pipfile.lock
└── README.md           
2 directories , 11 files

### Key Components
1. game/

* deck.py: Defines the Deck class, responsible for shuffling, dealing, and managing the deck of cards.
* hand.py: Defines the Hand class, which represents the cards held by the player or dealer and provides methods for calculating hand totals.
* player.py: Defines the Player class, which models both human players and the dealer, with methods for actions like "hit", "stand", and "bust".
* game.py: Contains the core game logic, such as managing turns, determining win conditions, and enforcing Blackjack rules.

2. ui/

* display.py: Handles the user interface (text-based), including printing the current state of the game (e.g., hands of the player and dealer, scores).

3. tests/

* Contains unit tests for each module (deck.py, hand.py, player.py) ensuring correctness of the logic.

4. main.py: The entry point to the game, initializing and starting the game, accepting player actions, and managing the flow of the game.


## INSTALLATION INSTRUCTIONS
- Clone the Repository: Start by cloning the repository to your local machine.
   git clone git@github.com:wahome-joy/code_dealers_phase3_project.git
- Navigate to the Project Directory.
   cd code_dealers_phase3_project
- Install Dependencies: If there are any dependencies (like libraries for testing or extra features), you can install them with:
  pip install -r requirements.txt
- Ensure Python Version: The game is compatible with Python 3.x. Ensure that you have Python 3 installed on your machine. You can verify by running:
  python --version


## USAGE
To start the game, simply run the main.py file. 


## GAME FLOW
* Upon running the game, the deck is shuffled, and both the player and the dealer receive two cards.
* The player is shown their hand and the dealer's first card (face-up).
* The player is prompted to either "hit" (draw another card) or "stand" (end their turn).
* If the player goes over 21 points (busts), they lose.
* After the player's turn, the dealer's hand is revealed, and the dealer plays according to standard Blackjack rules.
* The winner is determined by the player who has the highest hand without exceeding 21.


## GAMEPLAY RULES
The Blackjack rules are as follows:

1. Card Values:
Number cards (2-10) are worth their face value.
Face cards (Jack, Queen, King) are worth 10 points.
Aces are worth either 1 or 11, whichever is more beneficial for the hand.

2. Objective: Get as close to 21 points as possible without exceeding it.

3. Player's Turn: The player can choose to "hit" (take another card) or "stand" (end their turn). If the player’s total hand value exceeds 21, they are "busted" and lose the game.

4. Dealer's Turn: The dealer must "hit" if their hand is below 17 points. The dealer must "stand" if their hand is 17 points or higher.

5. Winning: If the player’s hand total is higher than the dealer’s without exceeding 21, the player wins. If the dealer’s total exceeds 21, the player wins. If both have the same total, it’s a tie.


## TESTING
To ensure that the game logic is working correctly, the project includes unit tests for each major module.
* To run the tests, use the following command:
pytest
This will run all the tests in the tests/ directory.

* For more specific testing, you can run tests for individual modules:
pytest tests/test_deck.py
pytest tests/test_hand.py
pytest tests/test_player.py


## TECHNOLOGIES USED
1. git
2. github
3. python3
4. jira
5. sqlite
6. SQL
7. sqlalchemy
8. markdown
9. pipenv

## Contact;
Mogusu2
wahome-joy
Karanja-23
Titus Kipchirchir


## LICENSE
MIT License Copyright (c) 2024 James Maroko, Joy Wahome, Hosea Karanja, Titus Kipchirchir

