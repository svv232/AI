class Board:
    def __init__(self):
        self._board = [[" "  for i in range(3)] for x in range(3)]
        self._grid = {}
        self._turn = False;
        equate = lambda x,y,z: self._grid.__setitem__((x,y),z)
        [equate(i,j,None) for i in range(3) for j in range(3)]
    
    def place_coordinates(self,x,y):
        equate = lambda x,y,z: self._grid.__setitem__((x,y),z)
        if -1<x<3 and -1<y<3 and self._board[x][y] == " ":
            self._board[x][y] = ('x' if not self._turn else 'o')
            equate(x,y,self._board[x][y])
            self._turn = not self._turn
    
    def victory(self):
        unique = lambda x: len(set(x)) == 1
        for i in range(3):
            if (unique(self._board[i]) or unique(zip(*self._board)[i])):
                if self._board[i][i] in 'xo': return 1
        return (unique(self._board[i][i] for i in range(3)) 
                or unique(self.board[i][i] for i in range(-1,2,-1)))

    def print_board(self):
        for i in self._board: print(i)

def main():
    B = Board()
    while not B.victory():
        try: B.place_coordinates(*map(int,raw_input().split(' ')))
        except: continue
        B.print_board()

main()
