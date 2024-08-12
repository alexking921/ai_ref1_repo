import sys
sys.path.append('aima-python')
#from search import *
from games import *
import math

def c4_eval(state):
    '''Example of a bad evaluation function: It gives a high
    score to any state whose board has a lot of Xs in the same
    column. Doesn't account for 'O', doesn't check other things
    that really would make sense.
    '''
    def count_in_line(start, dxy):
        count = 0
        while start in state.board:
            if state.board.get(start) == 'X':
                count += 1
            start = (start[0] + dxy[0], start[1] + dxy[1]) 
        return count

    ev = 0
    for i in range(1,8):
        ev += count_in_line((1,i), (0,1)) * 2
    # scale from -1 to 1
    return ev / 48

def ab_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state, game, eval_fn=c4_eval)

class HW3:
    def __init__(self):
        pass

    def example_problem(self):
        tt = TicTacToe()
        tt.play_game(alpha_beta_player,query_player)

    def example_problem2(self):
        c4 = ConnectFour()
        c4.play_game(ab_cutoff_player,query_player)

    def problem_1d():
        # write your code for problem 1d here
        pass

    def problem_2b():
        # write your code for problem 2d here
        pass
    
def main():
    hw3 = HW3()
    # An example for you to follow to get you started on Games
    print('Example Problem result:')
    print('=======================')
    print(hw3.example_problem())
    
if __name__ == '__main__':
    main()
