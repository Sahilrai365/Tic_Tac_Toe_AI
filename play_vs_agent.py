from first import TicTacToe
from agent import QLearningAgent
import pickle

from train import agent_O, state

with open("q_table_O.pkl","rb") as f:
    q_table_O = pickle.load(f)

agent_O = QLearningAgent(player='O')
agent_O.q_table = q_table_O
agent_O.epsilon = 0
while True:
    game = TicTacToe()
    game.render()
    while not game.is_game_over():
        if game.board.count('X') == game.board.count('O'):
            try:
                move = int(input("Your move(0-8): "))
                if move not in game.available_actions():
                    print("invalid move.Try again.")
                    continue
            except ValueError:
                print("Please enter a number from 0 to 8.")
                continue
            game.make_move(move,'X')
        else:
            state = game.get_state()
            action = agent_O.choose_action(state,game.available_actions())
            print(f"AI chooses position: {action}")
            game.make_move(action,'O')

        game.render()

    if game.current_winner == 'X':
        print("You win!")
    elif game.current_winner == 'O':
        print("AI wins!")
    else:
        print("it's a draw!")

    again = input("Play again? (y/n): ")
    if again.lower() != 'y':
        break
