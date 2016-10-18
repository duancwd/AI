import gamePlay
from gamePlay import gameOver
from copy import deepcopy


INFINITY = float("inf")



def value(board):
    value = 0
    for row in board:
           for elem in row:
                  if elem == "W":
                         value = value + 1
                  elif elem == "B":
                         value = value - 1





def Search(board, color, depth, alpha, beta, maximizingPlayer):
        moves = []
        for i in range(8):
                for j in range(8):
                        if gamePlay.validMove(board, color, (i,j)):
                                moves.append((i,j))
        if depth == 0 or gameOver(board) or len(moves) == 0:
                return "pass", value(board)
        if maximizingPlayer:
            for i in range (len(moves)):
                        move = moves[i]
                        newBoard = deepcopy(board)
                        gamePlay.doMove(newBoard,color,move)
                        alpha = max(alpha, Search(newBoard, color, depth - 1, alpha, beta, False)[1])
                        if beta <= alpha:
                                break
            return move, alpha 
        else:
                for j in range (len(moves)):
                        move = moves[j]
                        newBoard = deepcopy(board)
                        gamePlay.doMove(newBoard,color,move)
                        beta = min(beta, Search(newBoard, color, depth - 1, alpha, beta, True)[1])
                        if beta <= alpha:
                                break
                return move, beta

def nextMove(board, color):
        maximizingPlayer = color == "W"
        bestMove = Search(board, color, 3, -INFINITY, INFINITY, maximizingPlayer)[0]
        return bestMove
