import comp140_module5_tictactoe as tictactoe

# Board Dimension
DIMENSION = 3

# Square contents
SQ_EMPTY = 0
SQ_X = 1
SQ_O = 2

# Game state
WIN_NONE = 0
WIN_TIE = 1
WIN_X = 2
WIN_O = 3

class TicTacToeBoard:
    """
    Representation of an n dimensional Tic-Tac-Toe board.

    Squares can be empty (SQ_EMPTY) or have an X (SQ_X) or an O (SQ_O)
    in them.
    """

    def __init__(self, dimension):
        self._size = dimension
        self._grid = []
        for dummy in range(dimension):
            self._grid.append([SQ_EMPTY] * dimension)

    def get_square(self, xpos, ypos):
        """
        Get the state of a square on the board

    Inputs:
          xpos - integer x board position
          ypos - integer t board position

    Returns:
          state (SQ_EMPTY, SQ_X, or SQ_O) of square (xpos, ypos)
        """
        return self._grid[xpos][ypos]

    def mark_square(self, xpos, ypos, symbol):
        """
        Make the state of a square on the board.

    Inputs:
          xpos - integer x board position
          ypos - integer t board position
          symbol - one of SQ_EMPTY, SQ_X, or SQ_O
        """
        self._grid[xpos][ypos] = symbol

    def _get_rows(self):
        """
        Return a list of rows in the board.

        For efficiency, this returns the internal representation
        of the board, so should only be used internally!
        """
        return self._grid

    def _get_cols(self):
        """
        Return a list of columns in the board.
        """
        cols = []
        for ypos in range(self._size):
            cols.append([self._grid[xpos][ypos] for xpos in range(self._size)])
        return cols

    def _get_diags(self):
        """
        Return a list of diagonals in the board.
        """
        diags = []
        diags.append([self._grid[pos][pos] for pos in range(self._size)])
        diags.append([self._grid[pos][self._size-pos-1]
                      for pos in range(self._size)])
        return diags

    def _check_win(self, straight, symbol):
        """
    Check if symbol has won on this straight.

        Inputs:
          straight - a list of board symbols
          symbol - one of SQ_EMPTY, SQ_X, or SQ_O

        Returns:
          True if all elements of the straight are symbol,
          False, otherwise.       
        """
        return all(item == symbol for item in straight)

    def _board_full(self):
        """
        Returns True if the board is full, False otherwise.
        """
        for row in self._grid:
            if SQ_EMPTY in row:
                return False
        return True

    def win_state(self):
        """
        Returns the state of the board (WIN_NONE, WIN_TIE, WIN_X,
        WIN_O).
        """
        straights = []
        straights.extend(self._get_rows())
        straights.extend(self._get_cols())
        straights.extend(self._get_diags())

        # Check if winner in any of the straights
        for straight in straights:
            if self._check_win(straight, SQ_X):
                return WIN_X
            if self._check_win(straight, SQ_O):
                return WIN_O

        # Check if tie
        if self._board_full():
            return WIN_TIE

        return WIN_NONE

class TicTacToeGame:
    """
    Implements the logic to play a game of Tic-Tac-Toe one
    move at a time. Specifically, implements a method

        (symbol, winner) = game.play_next_move(self, x, y)

    that, given a valid coordinate on a Tic-Tac-Toe board,
    returns the symbol to placed on that grid coordinate,
    and either the winner of the game (if there is one) or
    None.
    """

    def __init__(self, dimension):
        self._board = TicTacToeBoard(dimension)
        self._player = SQ_X
        self._winner = WIN_NONE

        # Mappings from internal representations to what the GUI
        # wants.
        self._player_map = {SQ_X: 'X',
                            SQ_O: 'O'}

        self._state_map = {WIN_NONE: None,
                           WIN_TIE: 'Tie',
                           WIN_X: 'X',
                           WIN_O: 'O'}

    def _switch_player(self):
        """
        Switches the player back-and-forth between X and O.
        """
        if self._player == SQ_X:
            self._player = SQ_O
        else:
            self._player = SQ_X

    def play_next_move(self, xpos, ypos):
        """
        Given a valid (row, col) grid position on the
        Tic-Tac-Toe board, returns the symbol that should be
        placed in that position, and the winner of the game.
        
        The winner of the game should be the name of the 
        winning player ('X' or 'O'), 'Tie' if the game 
        ends in a tie, and None if the game is still in 
        progress.

        Inputs:
         row - row number on the board
         col - column number on the board

        Returns:
         A tuple of the symbol to be place on the board
         and the winner, as described above.
        """
        player = self._board.get_square(xpos, ypos)
        if (player == SQ_EMPTY) and (self._winner == WIN_NONE):
            # Square is empty, mark square
            player = self._player
            self._board.mark_square(xpos, ypos, player)
            self._switch_player()

        # Check winner
        self._winner = self._board.win_state()

        return (self._player_map[player],
                self._state_map[self._winner])

# Create the game controller and start the GUI
tictactoe.start(TicTacToeGame(DIMENSION), DIMENSION)
