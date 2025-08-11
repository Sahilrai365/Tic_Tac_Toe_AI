from first import TicTacToe
from agent import QLearningAgent
episodes = 50000
agent_X = QLearningAgent(player='X')
agent_O = QLearningAgent(player='O')
for episode in range(episodes):
    game = TicTacToe()
    state = game.get_state()

    agents = {'X' : agent_X, 'O': agent_O}
    current_player = 'X'
    transitions = []
    while not game.is_game_over():
        agent = agents[current_player]
        actions = game.available_actions()
        action = agent.choose_action(state,actions)

        game.make_move(action,current_player)
        next_state = game.get_state()
        next_actions = game.available_actions()
        transitions.append((state,action,current_player,next_state,next_actions))
        state = next_state
        current_player = 'O' if current_player == 'X' else 'X'

    winner = game.current_winner
    for state,action,player,next_state,next_actions in transitions:
        if winner is None:
            reward = 0
        elif player == winner:
            reward = 1
        else:
            reward = -1

        agents[player].update(state,action,reward,next_state,next_actions)

    if episode%5000 == 0:
        print(f"Episode{episode} complete.")

import pickle
with open("q_table_X.pkl","wb") as f:
    pickle.dump(agent_X.q_table,f)

with open("q_table_O.pkl","wb") as f:
    pickle.dump(agent_O.q_table,f)