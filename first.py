class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        return self.get_state()

    def get_state(self):
        return ''.join(self.board)

    def available_actions(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def make_move(self,position,player):
        if self.board[position] == ' ':
            self.board[position] = player
            if self.check_winner(position,player):
                self.current_winner = player
            return True
        return False

    def check_winner(self,pos,player):
        row_ind = pos//3
        row = self.board[row_ind*3: (row_ind+1)*3]
        if all([s == player for s in row]):
            return True

        col_ind = pos %3
        col = [self.board[col_ind + i*3] for i in range(3)]
        if all([s == player for s in col]):
            return True

        if pos % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([s == player for s in diagonal1]) or all([s == player for s in diagonal2]):
                return True

        return False

    def is_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.current_winner is not None or self.is_full()

    def render(self):
        for i in range(3):
            print('| ' + ' |'.join(self.board[i*3:(i+1)*3]) + ' |')
        print()
