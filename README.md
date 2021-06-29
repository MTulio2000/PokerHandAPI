# PokerHandAPI

In this API, you can do basic actions. Below, I will demonstrate how you can use that.

## Player

To create ->  ```POST://url/player/players```.
To update -> ```PUT://url/player/players/:id```.
To get -> ```GET://url/player/players```, or ```GET://url/player/players/:id`` to a specific player`.
To delete -> ```Delete://url/player/players/:id```.

Player table have 3 things:

* Id;
* name : String;
* won : Integer;
* total_played : Integer.

The facade of players, you can use ```set_hand````to set the Player's hand.

## Game

The Game is the part where the fun will be start.
To use game, you can start like a Player.
To create ->  ```POST://url/games/games```.
To update -> ```PUT://url/games/games/:id```.
To get -> ```GET://url/games/games```, or ```GET://url/games/games/:id`` to a specific player`.
To delete -> ```Delete://url/games/games/:id```.

Game have 4 attributes:

* Id;
* name : String;
* havePass : Boolean;
* password : String.

In the Game facade, you have these functions:

* ``` remove_player ``` to remove a player from the game
* ``` add_player ``` to add a player in the game
* ``` initialize_game ``` to start a new game
* ``` flip_card ``` to flip a hidden card a new game
* ``` check_winner ``` to flip a hidden card a new game
* ``` set_round_player ``` to set the player's action in the current round
* ``` new_round ``` to start a new round

