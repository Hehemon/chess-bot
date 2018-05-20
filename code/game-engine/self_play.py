import chess
import random
import timeit
from datetime import datetime

def self_play():

    board = chess.Board()
    #print("--- initial: begin ---")
    #print(board)
    #print("--- initial: end ---")
    i = 0
    while True:

        if board.is_checkmate():
            #print("Checkmate !!! ")
            res = not board.turn
            #del board
            return res

        if board.is_stalemate():
            #print("Stalemate !!!" + str(board.turn))
            res = not board.turn
            #del board
            return res

        if board.is_insufficient_material():
            #print("Draw !!!" + str(board.turn))
            #del board
            break


        lm = list(board.legal_moves)
        next_move = lm[random.randrange(0, len(lm))]

        #print("Move: " + str(i))
        #print(board)
        board.push(next_move)
        i += 1

def learn(N):
    white = 0
    black = 0
    draw = 0
    for i in range(N):
        if 0 == i%100:
            print(str(i) + " of " + str(N))
        j = self_play()
        if j is None:
            draw += 1
        if j is True:
            white += 1
        if j is False:
            black += 1

    print("Total: white=" + str(white) + ", black=" + str(black) + ", draw" + str(draw))

if __name__ == "__main__":

    now = datetime.utcnow()
    learn(100000)
    now2 = datetime.utcnow()
    print("Total spent " + str(now2 - now))

#    print(timeit.timeit(
#        stmt="play_immortal_game()",
#        setup="from __main__ import play_immortal_game",
#       number=100))
