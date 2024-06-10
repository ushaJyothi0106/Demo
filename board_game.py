import random

# Define the board size
BOARD_SIZE = 100

def play_game(num_players):
    player_positions = {}
    
    if num_players <= 2:
        print("Error: At least two players are required to play the game.")
    else:    
        player_positions = {i: [0] for i in range(1, num_players + 1)}
        print("Let's start the game!")
        
        game_flag = True
        
        while game_flag:
            for player in range(1, num_players + 1):
                dice_roll = random.randint(1, 6)
                print(f"Player {player} rolled a {dice_roll}.")
                new_position = player_positions[player][-1] + dice_roll
                
                if new_position == BOARD_SIZE:
                    player_positions[player].append(new_position)
                    game_flag = False
                    print(f"Player {player} wins!")
                    break
                elif new_position < BOARD_SIZE:
                    player_positions[player].append(new_position)
                    
                    
    return player_positions

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    game_history = play_game(num_players)
    if game_history is not None:
        print("Game History:")
        for player, positions in game_history.items():
            print(f"Player {player}: {positions}")
