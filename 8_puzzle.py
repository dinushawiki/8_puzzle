import numpy as np
import copy

class EightPuzzle:
    
    def __init__(self, problem):
        #initial puzzle
        self.current = np.matrix(problem)
        #goal
        self.goal = np.matrix(_goal_state)
        self.moves = []

    def legalMoves(self):
        #locate the 0 entry
        row,col = np.where(self.current == 0)
        #number of rows and columns
        size = self.current.shape
        numRows, numCols = size

        free = []
        # find indices of pieces that can move to empty space
        if row > 0:
            free.append((row - 1, col))
        if col > 0:
            free.append((row, col - 1))
        if row < numRows-1:
            free.append((row + 1, col))
        if col < numRows-1:
            free.append((row, col + 1))
        return free
    
    def getBestMove(self,puzzles):
        #locate zero (empty space)
        row,col = np.where(self.current == 0)
        best_move = []
        h_misplaced = 0
        i = 0
        #go through each legal move to evaluate
        for puzzle in puzzles:
            #get the misplaced tiles heuristic afte the given puzzle config
            move_h_misplaced = EightPuzzle.manhatten(self,puzzle)
            #check for the minimum misplaced tiles heuristic to get the best move
            if i == 0:
                h_misplaced = move_h_misplaced
                best_move = copy.deepcopy(puzzle)
            else:
                if move_h_misplaced < h_misplaced:
                    h_misplaced = move_h_misplaced
                    best_move = copy.deepcopy(puzzle)
            i += 1
        return best_move

    def puzzlesToCheck(self,legalMoves):
        puzzleToCheck = []
        #locate zero (empty space)
        row,col = np.where(self.current == 0)
        #go through each legal move to check if they are repeating
        for move in legalMoves:
            adj_matrix = copy.deepcopy(self.current)
            numToMoveRow,numToMoveCol = int(move[0]),int(move[1])
            #matrix after the move
            adj_matrix[row,col] = adj_matrix[numToMoveRow,numToMoveCol]
            adj_matrix[numToMoveRow,numToMoveCol] = 0
            exist = False
            for movesDone in self.moves:
                diff = movesDone - adj_matrix
                diffIndicator = len(np.nonzero(diff)[0])
                if diffIndicator == 0:
                    exist = True
            if exist == False:
                puzzleToCheck.append(adj_matrix)
        return puzzleToCheck
    
    def misplaced(self,adj_matrix):
        diff = self.goal-adj_matrix
        misplaced_tiles = len(np.nonzero(diff)[0])
        return misplaced_tiles

    def manhatten(self,adj_matrix):
        manhatten = 0
        size = adj_matrix.shape
        numRows, numCols = size
        for x in range(0, numRows):
            for y in range(0, numCols):
                #where is this element in goal?
                xCurrent = x
                yCurrent = y
                goalRow,goalCol = np.where(self.goal == adj_matrix[x,y])
                xGoal = goalRow[0]
                yGoal = goalCol[0]
                manhatten += abs(xCurrent - xGoal) + abs(yCurrent - yGoal)
        return manhatten


    def goalReached(self):
        diff = self.goal-self.current
        misplaced_tiles = len(np.nonzero(diff)[0])
        if misplaced_tiles == 0:
            return False
        else:
            return True
    
    def solve(self):

        goalReached = EightPuzzle.goalReached(self)
        i = 1
        while goalReached:
            #get legal moves
            legalMoves = EightPuzzle.legalMoves(self)
            #build the puzzlesToCheck elimating reapeated ones
            puzzlesToCheck = EightPuzzle.puzzlesToCheck(self,legalMoves)
            if not puzzlesToCheck:
                print("unsolvable")
                break
            afterBestMove = EightPuzzle.getBestMove(self,puzzlesToCheck)
            self.current = copy.deepcopy(afterBestMove)
            print('Move' + str(i))
            print(self.current)
            self.moves.append(self.current)
            goalReached = EightPuzzle.goalReached(self)
            i += 1



if __name__ == "__main__":
    _goal_state = [[1,2,3],
                   [8,0,4],
                   [7,6,5]]
    problem  =    [[2,8,3],
                   [1,6,4],
                   [7,5,0]]

    out = EightPuzzle(problem)
    out.solve()
