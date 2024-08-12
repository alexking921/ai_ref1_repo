import sys

sys.path.append('aima-python')
# from search import *
from games import *
import math


# *****GOMOKU X *******
# *****GOMOKU X *******
# *****GOMOKU X *******
# *****GOMOKU X *******
# BOARD IS JUDGED BY THE Num of consecutive X's it has (Only in columns for now)
def c4_evalMyVersionPRIME_gomoku(state):
    # The Count_in_Line() iterates through 1 col and gives it a val.
    # It is then called on every column of the game board, and summed together, to get a final eval of this state
    def count_in_line(start, dxy):  # THIS LOOP ASSESSES 1 COLUMN
        count = 0
        # mostConsecutive = 0
        tally = 0

        while start in state.board:  # THIS
            spot = state.board.get(start)
            if spot == 'X' or 'O':
                count = count + 1
                tally = tally + 1
                if tally > 1:
                    count = count + tally

                if spot == 'X':
                    count = count + tally

                # mostConsecutive = max(mostConsecutive, tally)
            else:
                tally = 0

                # increment start(x,y),
            start = (start[0] + dxy[0], start[1] + dxy[
                1])  # THIS NOTATION IS AWKWARD BUT IT ALLOWS YOU TO BE ABLE TO SEARCH VERTICALLY OR HORIZONTALLY WITHOUT CHANGING ANY OF THE BODYS CODE, SIMPLY BY PASSING A DIFF VAL FOR THE dxy(a,b) tuple

        # return mostConsecutive
        return count

    # LOOK AT ALL THE ROWS...STARTING AT BOTTOM, LEFT CORNER
    sumOfColEvals = 0
    for i in range(15, 0,
                   -1):  # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
        # look at all the column evaluation:
        # consec = count_in_line((1,i), (0,1)) # quick check if found winning verticals # THIS IS THE DEFAULT ITERATION IM SUS ABOUT...
        consec = count_in_line((i, 1),
                               (0, 1))  # quick check if found winning verticals # MY FIX BY SWAPPING (0,1) with (1,0)
        sumOfColEvals = sumOfColEvals + consec * 2

    # scale from -1 to 1
    # NORMALIZE THE COL & ROW EVALS
    a = sumOfColEvals / 1000
    # print(a)
    return a


# ****GOMOKU O White *******
# *****GOMOKU O White *******
# *****GOMOKU O White *******
# *****GOMOKU O White *******
# BOARD IS JUDGED BY THE Num of consecutive X's it has (Only in columns for now)
def c4_evalMyVersionPRIME_gomokuwhite(state):
    # The Count_in_Line() iterates through 1 col and gives it a val.
    # It is then called on every column of the game board, and summed together, to get a final eval of this state
    def count_in_line(start, dxy):  # THIS LOOP ASSESSES 1 COLUMN
        count = 0
        # mostConsecutive = 0
        tally = 0

        while start in state.board:  # THIS
            spot = state.board.get(start)
            if spot == 'X' or 'O':
                count = count + 1
                tally = tally + 1
                if tally > 1:
                    count = count + tally

                if spot == 'O':
                    count = count + tally

                # mostConsecutive = max(mostConsecutive, tally)
            else:
                tally = 0

                # increment start(x,y),
            start = (start[0] + dxy[0], start[1] + dxy[
                1])  # THIS NOTATION IS AWKWARD BUT IT ALLOWS YOU TO BE ABLE TO SEARCH VERTICALLY OR HORIZONTALLY WITHOUT CHANGING ANY OF THE BODYS CODE, SIMPLY BY PASSING A DIFF VAL FOR THE dxy(a,b) tuple

        # return mostConsecutive
        return count

    # LOOK AT ALL THE ROWS...STARTING AT BOTTOM, LEFT CORNER
    sumOfColEvals = 0
    for i in range(15, 0,
                   -1):  # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
        # look at all the column evaluation:
        # consec = count_in_line((1,i), (0,1)) # quick check if found winning verticals # THIS IS THE DEFAULT ITERATION IM SUS ABOUT...
        consec = count_in_line((i, 1),
                               (0, 1))  # quick check if found winning verticals # MY FIX BY SWAPPING (0,1) with (1,0)
        sumOfColEvals = sumOfColEvals + consec * 2

    # scale from -1 to 1
    # NORMALIZE THE COL & ROW EVALS
    a = sumOfColEvals / 1000
    # print(a)
    return a


# -------- CONNECT-4 X -------- *
# -------- CONNECT-4 X -------- *
# -------- CONNECT-4 X -------- *
# -------- CONNECT-4 X -------- *
# -------- CONNECT-4 X -------- *
# BOARD IS JUDGED BY THE Num of consecutive X's it has (Only in columns for now)
def c4_evalMyVersionPRIME(state):
    '''Example of a bad evaluation function: It gives a high
    score to any state whose board has a lot of Xs in the same
    column. Doesn't account for 'O', doesn't check other things
    that really would make sense.
    '''

    # The Count_in_Line() iterates through 1 col and gives it a val.
    # It is then called on every column of the game board, and summed together, to get a final eval of this state
    def count_in_line(start, dxy):  # THIS LOOP ASSESSES 1 COLUMN
        count = 0
        mostConsecutive = 0
        tally = 0

        while start in state.board:  # THIS
            if state.board.get(start) == 'X':
                count = count + 1
                tally = tally + 1
                if tally > 1:
                    count = count + tally

                mostConsecutive = max(mostConsecutive, tally)
            else:
                tally = 0

                # increment start(x,y),
            start = (start[0] + dxy[0], start[1] + dxy[
                1])  # THIS NOTATION IS AWKWARD BUT IT ALLOWS YOU TO BE ABLE TO SEARCH VERTICALLY OR HORIZONTALLY WITHOUT CHANGING ANY OF THE BODYS CODE, SIMPLY BY PASSING A DIFF VAL FOR THE dxy(a,b) tuple

        # return mostConsecutive
        return count

    # LOOK AT ALL THE ROWS...STARTING AT BOTTOM, LEFT CORNER
    sumOfColEvals = 0
    for i in range(7, 0, -1):  # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
        # look at all the column evaluation:
        # consec = count_in_line((1,i), (0,1)) # quick check if found winning verticals # THIS IS THE DEFAULT ITERATION IM SUS ABOUT...
        consec = count_in_line((i, 1),
                               (0, 1))  # quick check if found winning verticals # MY FIX BY SWAPPING (0,1) with (1,0)
        sumOfColEvals = sumOfColEvals + consec * 2

    # scale from -1 to 1
    # NORMALIZE THE COL & ROW EVALS
    a = sumOfColEvals / 85
    # print(a)
    return a


# -------- CONNECT-4 O white -------- *
# -------- CONNECT-4 O white -------- *
# -------- CONNECT-4 O white -------- *
# -------- CONNECT-4 O white -------- *
# -------- CONNECT-4 O white -------- *
# TWEAK FOR BEING THE 'O' player
# BOARD IS JUDGED BY THE Num of consecutive X's it has (Only in columns for now)
def c4_evalMyVersionPRIMEwhite(state):
    '''Example of a bad evaluation function: It gives a high
    score to any state whose board has a lot of Xs in the same
    column. Doesn't account for 'O', doesn't check other things
    that really would make sense.
    '''

    # The Count_in_Line() iterates through 1 col and gives it a val.
    # It is then called on every column of the game board, and summed together, to get a final eval of this state
    def count_in_line(start, dxy):  # THIS LOOP ASSESSES 1 COLUMN
        count = 0
        mostConsecutive = 0
        tally = 0

        while start in state.board:  # THIS
            if state.board.get(start) == 'O':
                count = count + 1
                tally = tally + 1
                if tally > 1:
                    count = count + tally

                mostConsecutive = max(mostConsecutive, tally)
            else:
                tally = 0

                # increment start(x,y),
            start = (start[0] + dxy[0], start[1] + dxy[
                1])  # THIS NOTATION IS AWKWARD BUT IT ALLOWS YOU TO BE ABLE TO SEARCH VERTICALLY OR HORIZONTALLY WITHOUT CHANGING ANY OF THE BODYS CODE, SIMPLY BY PASSING A DIFF VAL FOR THE dxy(a,b) tuple

        # return mostConsecutive
        return count

    # LOOK AT ALL THE ROWS...STARTING AT BOTTOM, LEFT CORNER
    sumOfColEvals = 0
    for i in range(7, 0,
                   -1):  # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
        # look at all the column evaluation:
        # consec = count_in_line((1,i), (0,1)) # quick check if found winning verticals # THIS IS THE DEFAULT ITERATION IM SUS ABOUT...
        consec = count_in_line((i, 1),
                               (0, 1))  # quick check if found winning verticals # MY FIX BY SWAPPING (0,1) with (1,0)
        sumOfColEvals = sumOfColEvals + consec * 2

    # scale from -1 to 1
    # NORMALIZE THE COL & ROW EVALS
    a = sumOfColEvals / 100
    # print(a)
    return a


# -------- DEFAULT 'bad' eval -------- *
# -------- DEFAULT 'bad' eval -------- *
# -------- DEFAULT 'bad' eval -------- *
# -------- DEFAULT 'bad' eval -------- *
def c4_eval(state):
    '''Example of a bad evaluation function: It gives a high
    score to any state whose board has a lot of Xs in the same
    column. Doesn't account for 'O', doesn't check other things
    that really would make sense.
    '''

    def count_in_line(start, dxy):
        count = 0
        print(len(state.board))
        # print("ABOUT TO LOOK AT STATE-BOARD")
        # print("ENTERING count-in-line FUNCTION...")
        # r = len(start[0])
        # c = len(start)

        # print(start)
        # print("r reads as: ", r)
        # print(state.board)
        while start in state.board:
            if state.board.get(start) == 'X':
                count += 1

            start = (start[0] + dxy[0], start[1] + dxy[1])
            # print("start reads as:")
            # print(start)

        return count

    ev = 0
    for i in range(1, 8):
        ev += count_in_line((1, i), (0, 1)) * 2

    # scale from -1 to 1
    # print(ev/48)
    return ev / 48


###########################################
# PLAYER OPTIONS
###########################################

# DEFAULT
def ab_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state, game, eval_fn=c4_eval)


# PRIME
def ab_cutoff_playerPRIME(game, state):
    return alpha_beta_cutoff_search(state, game, eval_fn=c4_evalMyVersionPRIME)


# PRIME WITH CUTOFF OF 4 (1c)
def ab_cutoff_playerPRIME_cutoff(game, state):
    return alpha_beta_cutoff_search(state, game, 4, eval_fn=c4_evalMyVersionPRIME)


# PRIME (WHITE-PLAYER) WITH CUTOFF OF 4 (1c)
def ab_cutoff_playerPRIME_cutoff_white(game, state):
    return alpha_beta_cutoff_search(state, game, 4, eval_fn=c4_evalMyVersionPRIMEwhite)


# GOMOKU-BLACK PRIME WITH CUTOFF OF 2
def ab_cutoff_playerPRIME_cutoff_gomoku(game, state):
    return alpha_beta_cutoff_search(state, game, 2, eval_fn=c4_evalMyVersionPRIME_gomoku)


# GOMOKU-WHITE PRIME WITH CUTOFF OF 2
def ab_cutoff_playerPRIME_cutoff_gomokuwhite(game, state):
    return alpha_beta_cutoff_search(state, game, 2, eval_fn=c4_evalMyVersionPRIME_gomokuwhite)


###########################################
# CLASS DEFINITIONS + MAIN()
###########################################

class HW3:
    def __init__(self):
        pass

    def example_problem(self):
        tt = TicTacToe()
        tt.play_game(alpha_beta_player, query_player)
        ##tt.play_game(alpha_beta_player,alpha_beta_player)

    def example_problem2(self):
        c4 = ConnectFour()
        # diff players:
        # c4.play_game(ab_cutoff_player,query_player) #default/weakest
        # c4.play_game(ab_cutoff_playerPRIME,random_player)
        c4.play_game(ab_cutoff_playerPRIME_cutoff, random_player)

    # 1-D
    def problem_1d(self):
        # write your code for problem 1d here
        print("20 GAMES OF CONNECT-4...")
        print("10 GAMES FOR X")
        for i in range(10):
            print("___starting new game___")
            c4 = ConnectFour()
            c4.play_game(ab_cutoff_playerPRIME_cutoff, random_player)

        print("____________________________________________________________________________")
        print("10 GAMES FOR O......")

        for i in range(10):
            print("___starting new game___")
            c4 = ConnectFour()
            c4.play_game(ab_cutoff_playerPRIME_cutoff_white, random_player)

    # 2-B
    def problem_2b(self):
        print("20 GAMES OF GOMOKU...")
        print("10 GAMES FOR X")
        for i in range(10):
            print("___starting new game___")
            goku = Gomoku()
            goku.play_game(ab_cutoff_playerPRIME_cutoff_gomoku, random_player)  # playing as X

        # print("____________________________________________________________________________")
        print("10 GAMES FOR O......")
        for i in range(10):
            print("___starting new game___")
            goku = Gomoku()
            goku.play_game(random_player, ab_cutoff_playerPRIME_cutoff_gomokuwhite)  # playing as O


###########################################
# MAIN()
###########################################
def main():
    hw3 = HW3()
    # An example for you to follow to get you started on Games
    print('Example Problem result:')
    print('=======================')
    # print(hw3.example_problem()) #PLAYS 1a) TIC-TAC TOE
    # print(hw3.example_problem2()) #PLAYS 1b) CONNECT-4
    print(hw3.problem_1d())
    print(hw3.problem_2b())


if __name__ == '__main__':
    main()
