import sys

sys.path.append('aima-python')
# from search import *
from games import *
import math


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

    # LOOK AT ALL THE COLUMNS...STARTING AT LEFT, BOTTOM CORNER
    # sumOfColEvals = 0
    # for i in range(6,0,-1): # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
    #     # look at all the column evaluation:
    #     #consec = count_in_line((1,i), (0,1)) # quick check if found winning verticals # THIS IS THE DEFAULT ITERATION IM SUS ABOUT...
    #     consec = count_in_line((7,i), (-1,0)) # quick check if found winning verticals # MY FIX BY SWAPPING (0,1) with (1,0)
    #     sumOfColEvals  = sumOfColEvals  + consec * 2

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

    # LOOK AT ALL THE COLUMNS...STARTING AT LEFT, BOTTOM CORNER
    # sumOfColEvals = 0
    # for i in range(6,0,-1): # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
    #     # look at all the column evaluation:
    #     #consec = count_in_line((1,i), (0,1)) # quick check if found winning verticals # THIS IS THE DEFAULT ITERATION IM SUS ABOUT...
    #     consec = count_in_line((7,i), (-1,0)) # quick check if found winning verticals # MY FIX BY SWAPPING (0,1) with (1,0)
    #     sumOfColEvals  = sumOfColEvals  + consec * 2

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


# BOARD IS JUDGED BY THE Num of consecutive X's it has (Only in columns for now)
def c4_evalMyVersionMID2(state):
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
                mostConsecutive = max(mostConsecutive, tally)
                # else:
                # tally = 0

                # increment start(x,y),
            start = (start[0] + dxy[0], start[1] + dxy[
                1])  # THIS NOTATION IS AWKWARD BUT IT ALLOWS YOU TO BE ABLE TO SEARCH VERTICALLY OR HORIZONTALLY WITHOUT CHANGING ANY OF THE BODYS CODE, SIMPLY BY PASSING A DIFF VAL FOR THE dxy(a,b) tuple

        # return mostConsecutive
        return count

    # LOOK AT ALL THE COLUMNS...STARTING AT LEFT, BOTTOM CORNER
    # sumOfColEvals = 0
    # for i in range(6,0,-1): # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
    #     # look at all the column evaluation:
    #     #consec = count_in_line((1,i), (0,1)) # quick check if found winning verticals # THIS IS THE DEFAULT ITERATION IM SUS ABOUT...
    #     consec = count_in_line((7,i), (-1,0)) # quick check if found winning verticals # MY FIX BY SWAPPING (0,1) with (1,0)
    #     sumOfColEvals  = sumOfColEvals  + consec * 2

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
    a = sumOfColEvals / 48
    print(a)
    return a


# BOARD IS JUDGED BY THE Num of consecutive X's it has, (both in cols AND rows)
def c4_evalMyVersionMID(state):
    '''Example of a bad evaluation function: It gives a high
    score to any state whose board has a lot of Xs in the same
    column. Doesn't account for 'O', doesn't check other things
    that really would make sense.
    '''

    # The Count_in_Line() iterates through 1 col and gives it a val.
    # It is then called on every column of the game board, and summed together, to get a final eval of this state
    def count_in_line(start, dxy):  # THIS LOOP ASSESSES 1 COLUMN
        # count = 0
        mostConsecutive = 0
        tally = 0

        while start in state.board:  # THIS
            if state.board.get(start) == 'X':
                tally = tally + 1
                mostConsecutive = max(mostConsecutive, tally)
            else:
                tally = 0

            # increment start(x,y),
            start = (start[0] + dxy[0], start[1] + dxy[
                1])  # THIS NOTATION IS AWKWARD BUT IT ALLOWS YOU TO BE ABLE TO SEARCH VERTICALLY OR HORIZONTALLY WITHOUT CHANGING ANY OF THE BODYS CODE, SIMPLY BY PASSING A DIFF VAL FOR THE dxy(a,b) tuple

        return mostConsecutive

    # LOOK AT ALL THE COLUMNS...
    sumOfColEvals = 0
    for i in range(1,
                   7):  # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
        # look at all the column evaluation:
        # consec = count_in_line((1,i), (0,1)) # quick check if found winning verticals # THIS IS THE DEFAULT ITERATION IM SUS ABOUT...
        consec = count_in_line((1, i),
                               (1, 0))  # quick check if found winning verticals # MY FIX BY SWAPPING (0,1) with (1,0)
        if consec == 4:
            # print("FOUND WINNING VERTICAL!!!!!!!!!")
            sumOfColEvals = 1
            return sumOfColEvals
        else:
            sumOfColEvals = sumOfColEvals + consec * 2

    # LOOK AT ALL THE ROWS...
    sumOfRowEvals = 0

    # OR SHOULD BE (range(1,8) because i is repping VERTICAL len)
    for i in range(1,
                   8):  # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
        # look at all the row evaluation:
        # consec = count_in_line((i,1), (1,0))# quick check if found winning horizontals

        # consec = count_in_line((i,1), (1,0)) # quick check if found winning verticals # THIS IS THE DEFAULT ITERATION IM SUS ABOUT...
        consec = count_in_line((i, 1),
                               (0, 1))  # quick check if found winning verticals # MY FIX BY SWAPPING (1,0) with (0,1)
        if consec == 4:
            sumOfRowEvals = 1
            print("FOUND WINNING HORIZONTALL!!!!!!!!!")
            return sumOfRowEvals
        else:
            sumOfRowEvals = sumOfRowEvals + consec * 2

    # scale from -1 to 1
    # NORMALIZE THE COL & ROW EVALS
    a = sumOfColEvals / 48

    b = sumOfRowEvals / 48

    print(a, "___", b)

    # RISKY DECISION HERE: ONLY RETURNING THE LARGER OF THE TWO RATINGS -- so if the COL score is higher, I'll return that, and same goes for
    # scale from -1 to 1
    # print(ev/48)
    # return ev / 48
    return max(a, b)


# board state judged by tot num X's in a col AND tot num X's in rows [HOWEVER, DOESNT factor in consecutive X's, only TOTAL NUM]
# same as default, but now looks at BOTH Columns AND rows (instead of only columns)
def c4_evalMyVersionTHREE(state):
    '''Example of a bad evaluation function: It gives a high
    score to any state whose board has a lot of Xs in the same
    column. Doesn't account for 'O', doesn't check other things
    that really would make sense.
    '''

    # The Count_in_Line() iterates through 1 col and gives it a val.
    # It is then called on every column of the game board, and summed together, to get a final eval of this state
    def count_in_line(start, dxy):  # THIS LOOP ASSESSES 1 COLUMN
        count = 0

        while start in state.board:  # THIS
            if state.board.get(start) == 'X':
                count = count + 1

            # increment start(x,y),
            start = (start[0] + dxy[0], start[1] + dxy[
                1])  # THIS NOTATION IS AWKWARD BUT IT ALLOWS YOU TO BE ABLE TO SEARCH VERTICALLY OR HORIZONTALLY WITHOUT CHANGING ANY OF THE BODYS CODE, SIMPLY BY PASSING A DIFF VAL FOR THE dxy(a,b) tuple
            # start = (start[0], start[1]+1)
        return count

    # LOOK AT ALL THE COLUMNS...
    sumOfColEvals = 0
    for i in range(1,
                   8):  # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
        # look at all the column evaluation:
        sumOfColEvals = sumOfColEvals + count_in_line((1, i), (0, 1)) * 2

    # LOOK AT ALL THE ROWS...
    sumOfRowEvals = 0
    for i in range(1,
                   7):  # CALL OUR FUNCTION ON EVERY COL OF STATE, then SUM val of each col and that is the boards state rating
        # look at all the column evaluation:
        sumOfRowEvals = sumOfRowEvals + count_in_line((i, 1), (1, 0)) * 2

    # row evaluation

    # scale from -1 to 1
    # print(ev/48)
    return ev / 48


def c4_evalMyVersionONE(state):
    '''Example of a bad evaluation function: It gives a high
    score to any state whose board has a lot of Xs in the same
    column. Doesn't account for 'O', doesn't check other things
    that really would make sense.
    '''

    # The Count_in_Line() iterates through 1 col and gives it a val.
    # It is then called on every column of the game board, and summed together, to get a final eval of this state
    def count_in_line(start, dxy):  # THIS LOOP ASSESSES 1 COLUMN
        count = 0
        print(len(start[0]))
        while start in state.board:  # THIS
            if state.board.get(start) == 'X':
                count += 1
            start = (start[0] + dxy[0], start[1] + dxy[1])
            # INSERT CODE HERE TO SEARCH FOR A 3-in a row OPPONENT state, and return very high value so automatically chooses to block it
        return count

    ev = 0
    for i in range(1, 8):  #
        ev = ev + count_in_line((1, i), (0, 1)) * 2
        # INSERT CODE HERE TO SEARCH FOR A 3-in a row OPPONENT state, and return very high value so automatically chooses to block it

    # scale from -1 to 1
    print(ev / 48)
    return ev / 48


def c4_eval(state):
    '''Example of a bad evaluation function: It gives a high
    score to any state whose board has a lot of Xs in the same
    column. Doesn't account for 'O', doesn't check other things
    that really would make sense.
    '''

    def count_in_line(start, dxy):
        count = 0
        print(len(state.board))
        print("ABOUT TO LOOK AT STATE-BOARD")
        # print("ENTERING count-in-line FUNCTION...")
        # r = len(start[0])
        # c = len(start)

        # print(start)
        # print("r reads as: ", r)
        print(state.board)
        while start in state.board:
            if state.board.get(start) == 'X':
                count += 1

            start = (start[0] + dxy[0], start[1] + dxy[1])
            print("start reads as:")
            print(start)

        return count

    ev = 0
    for i in range(1, 8):
        ev += count_in_line((1, i), (0, 1)) * 2

    # scale from -1 to 1
    # print(ev/48)
    return ev / 48


# DIFFERENT PLAYERS (aka diff eval functions)
# DEFAULT
def ab_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state, game, eval_fn=c4_eval)


# PRIME
def ab_cutoff_playerPRIME(game, state):
    return alpha_beta_cutoff_search(state, game, eval_fn=c4_evalMyVersionPRIME)


# PRIME WITH CUTOFF OF 4 (1c)
def ab_cutoff_playerPRIME_cutoff(game, state):
    return alpha_beta_cutoff_search(state, game, 2, eval_fn=c4_evalMyVersionPRIME)


# PRIME (WHITE-PLAYER) WITH CUTOFF OF 4 (1c)
def ab_cutoff_playerPRIME_cutoff_white(game, state):
    return alpha_beta_cutoff_search(state, game, 4, eval_fn=c4_evalMyVersionPRIMEwhite)


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
        # print("10 GAMES FOR X")
        c4 = ConnectFour()
        c4.play_game(ab_cutoff_playerPRIME_cutoff, random_player)
        c5 = ConnectFour()
        c5.play_game(ab_cutoff_playerPRIME_cutoff_white, random_player)
        # for i in range(10):
        #     print("___starting new game___")
        #     c4 = ConnectFour()
        #     c4.play_game(ab_cutoff_playerPRIME_cutoff, random_player)
        #
        # print("____________________________________________________________________________")
        # print("10 GAMES FOR O......")
        #
        # for i in range(10):
        #     print("___starting new game___")
        #     c4 = ConnectFour()
        #     c4.play_game(ab_cutoff_playerPRIME_cutoff_white, random_player)

    # 2-B
    def problem_2b(self):
        goku = Gomoku()
        goku.play_game(ab_cutoff_playerPRIME_cutoff, random_player)
        # write your code for problem 2d here


def main():
    hw3 = HW3()
    # An example for you to follow to get you started on Games
    print('Example Problem result:')
    print('=======================')
    print(hw3.example_problem()) #PLAYS 1a) TIC-TAC TOE
    # print(hw3.example_problem2()) #PLAYS 1b) CONNECT-4
    # print(hw3.problem_1d())
    print(hw3.problem_2b())


if __name__ == '__main__':
    main()
