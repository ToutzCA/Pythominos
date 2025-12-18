"""
Pythominos - NumWorks Calculator Adaptation
A simplified version of the Pythominos puzzle game designed for the NumWorks calculator.

Features:
- Uses kandinsky module for graphics (NumWorks screen: 320x222 pixels)
- Uses ion module for keyboard input
- Simplified UI optimized for calculator screen
- No audio support (NumWorks limitation)
- No file save system (uses in-memory state only)
- Focus on core puzzle gameplay

Controls:
- Arrow keys: Move piece
- OK: Place piece / Select
- Back: Remove piece / Go back
- EXE: Rotate piece
- Shift: Mirror piece
- Toolbox: Quick menu
"""

try:
    from kandinsky import fill_rect, draw_string, get_pixel, set_pixel
    from ion import keydown, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
    from ion import KEY_OK, KEY_BACK, KEY_EXE, KEY_SHIFT
    NUMWORKS_MODE = True
except ImportError:
    # Fallback for testing on PC - simulate NumWorks modules
    NUMWORKS_MODE = False
    print("Warning: NumWorks modules not available. Running in simulation mode.")
    
    class SimKandinsky:
        @staticmethod
        def fill_rect(x, y, w, h, color):
            pass
        
        @staticmethod
        def draw_string(text, x, y, color=(0, 0, 0), bg=(255, 255, 255)):
            print(f"Draw: {text} at ({x}, {y})")
    
    class SimIon:
        KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 0, 1, 2, 3
        KEY_OK, KEY_BACK, KEY_EXE, KEY_SHIFT = 4, 5, 6, 7
        
        @staticmethod
        def keydown(key):
            return False
    
    kandinsky = SimKandinsky()
    ion = SimIon()
    fill_rect = kandinsky.fill_rect
    draw_string = kandinsky.draw_string
    keydown = ion.keydown
    KEY_LEFT = ion.KEY_LEFT
    KEY_RIGHT = ion.KEY_RIGHT
    KEY_UP = ion.KEY_UP
    KEY_DOWN = ion.KEY_DOWN
    KEY_OK = ion.KEY_OK
    KEY_BACK = ion.KEY_BACK
    KEY_EXE = ion.KEY_EXE
    KEY_SHIFT = ion.KEY_SHIFT

# Screen dimensions for NumWorks calculator
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 222

# Game constants
CELL_SIZE = 20  # Smaller cells for calculator screen
BOARD_WIDTH = 12
BOARD_HEIGHT = 5
BOARD_X = 10
BOARD_Y = 40

# Colors (RGB tuples)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GRAY = (127, 127, 127)
COLOR_LIGHT_GRAY = (195, 195, 195)
COLOR_BLUE = (100, 188, 237)
COLOR_DARK_BLUE = (32, 12, 255)
COLOR_RED = (255, 30, 39)
COLOR_DARK_RED = (136, 0, 21)
COLOR_YELLOW = (255, 255, 0)
COLOR_ORANGE = (245, 139, 26)
COLOR_GREEN = (32, 189, 15)
COLOR_DARK_GREEN = (16, 79, 18)
COLOR_PINK = (245, 133, 177)
COLOR_PURPLE = (202, 66, 209)
COLOR_DARK_PURPLE = (99, 37, 212)
COLOR_BROWN = (128, 118, 37)

# Piece colors (12 different colors for 12 pieces)
PIECE_COLORS = [
    COLOR_BLUE, COLOR_DARK_BLUE, COLOR_RED, COLOR_DARK_RED,
    COLOR_YELLOW, COLOR_ORANGE, COLOR_GREEN, COLOR_DARK_GREEN,
    COLOR_PINK, COLOR_PURPLE, COLOR_DARK_PURPLE, COLOR_BROWN
]

# Piece patterns (12 pentomino-like pieces) - matching original Pythominos.py
PIECE_PATTERNS = [
    # Piece 1: I pentomino (5 cells in a vertical line)
    [[1], [1], [1], [1], [1]],
    
    # Piece 2: L pentomino
    [[2, 2], [2], [2], [2]],
    
    # Piece 3: T pentomino
    [[3], [3, 3], [3], [3]],
    
    # Piece 4: N pentomino
    [[4], [4, 4], [0, 4], [0, 4]],
    
    # Piece 5: Y pentomino
    [[5], [5], [5, 5, 5]],
    
    # Piece 6: P pentomino
    [[6], [6, 6], [6, 6]],
    
    # Piece 7: Z pentomino
    [[7, 7], [0, 7], [7, 7]],
    
    # Piece 8: W pentomino
    [[8, 8], [0, 8], [0, 8, 8]],
    
    # Piece 9: U pentomino
    [[9], [9, 9, 9], [0, 9]],
    
    # Piece 10: F pentomino
    [[10, 10, 10], [0, 10], [0, 10]],
    
    # Piece 11: X pentomino
    [[11], [11, 11], [0, 11, 11]],
    
    # Piece 12: V pentomino (cross shape)
    [[0, 12], [12, 12, 12], [0, 12]]
]


class Piece:
    """Represents a game piece with rotation and movement capabilities."""
    
    def __init__(self, numero, pattern):
        self.numero = numero
        self.pattern = pattern
        self.coords = self._pattern_to_coords()
        self.placed = False
    
    def _pattern_to_coords(self):
        """Convert pattern matrix to list of relative coordinates."""
        coords = []
        for i, row in enumerate(self.pattern):
            for j, val in enumerate(row):
                if val != 0:
                    coords.append([i, j])
        return coords
    
    def rotate(self):
        """Rotate piece 90 degrees clockwise."""
        if not self.coords:
            return
        
        # Normalize to origin
        min_x = min(x for x, _ in self.coords)
        min_y = min(y for _, y in self.coords)
        norm = [[x - min_x, y - min_y] for x, y in self.coords]
        
        # Rotate 90° CW: (x, y) -> (y, -x)
        rot = [[y, -x] for x, y in norm]
        
        # Normalize again
        min_x2 = min(x for x, _ in rot)
        min_y2 = min(y for _, y in rot)
        self.coords = [[x - min_x2, y - min_y2] for x, y in rot]
    
    def mirror(self):
        """Mirror piece horizontally."""
        if not self.coords:
            return
        
        max_y = max(y for _, y in self.coords)
        mirrored = [[x, max_y - y] for x, y in self.coords]
        
        # Normalize
        min_y = min(y for _, y in mirrored)
        self.coords = [[x, y - min_y] for x, y in mirrored]


class Board:
    """Represents the game board."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
    
    def clear(self):
        """Clear the board."""
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
    
    def can_place(self, piece, row, col):
        """Check if piece can be placed at given position."""
        for dr, dc in piece.coords:
            r, c = row + dr, col + dc
            if r < 0 or r >= self.height or c < 0 or c >= self.width:
                return False
            if self.grid[r][c] != 0:
                return False
        return True
    
    def place_piece(self, piece, row, col):
        """Place piece on board at given position."""
        if not self.can_place(piece, row, col):
            return False
        
        for dr, dc in piece.coords:
            r, c = row + dr, col + dc
            self.grid[r][c] = piece.numero
        piece.placed = True
        return True
    
    def remove_piece(self, piece_numero):
        """Remove all cells belonging to a piece."""
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] == piece_numero:
                    self.grid[r][c] = 0
    
    def is_full(self):
        """Check if board is completely filled."""
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    return False
        return True


class Game:
    """Main game controller for Pythominos on NumWorks."""
    
    def __init__(self):
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT)
        self.pieces = [Piece(i + 1, PIECE_PATTERNS[i]) for i in range(12)]
        
        # Start with first 4 pieces available
        self.available_pieces = [0, 1, 2, 3]  # indices
        self.current_piece_idx = 0
        self.cursor_row = 0
        self.cursor_col = 0
        
        self.state = "playing"  # playing, won, menu
        self.menu_option = 0
        self.message = ""
        self.message_timer = 0
        
        # Key press timing for repeat
        self.key_timer = {}
    
    def get_current_piece(self):
        """Get currently selected piece."""
        if self.current_piece_idx < len(self.available_pieces):
            return self.pieces[self.available_pieces[self.current_piece_idx]]
        return None
    
    def next_piece(self):
        """Switch to next available piece."""
        self.current_piece_idx = (self.current_piece_idx + 1) % len(self.available_pieces)
    
    def prev_piece(self):
        """Switch to previous available piece."""
        self.current_piece_idx = (self.current_piece_idx - 1) % len(self.available_pieces)
    
    def show_message(self, text, duration=30):
        """Display a temporary message."""
        self.message = text
        self.message_timer = duration
    
    def update_message_timer(self):
        """Update message display timer."""
        if self.message_timer > 0:
            self.message_timer -= 1
            if self.message_timer == 0:
                self.message = ""
    
    def handle_input(self):
        """Process keyboard input."""
        if self.state == "playing":
            piece = self.get_current_piece()
            if piece is None:
                return
            
            # Movement
            if keydown(KEY_LEFT):
                if self.cursor_col > 0:
                    self.cursor_col -= 1
            
            if keydown(KEY_RIGHT):
                if self.cursor_col < self.board.width - 1:
                    self.cursor_col += 1
            
            if keydown(KEY_UP):
                if self.cursor_row > 0:
                    self.cursor_row -= 1
            
            if keydown(KEY_DOWN):
                if self.cursor_row < self.board.height - 1:
                    self.cursor_row += 1
            
            # Actions
            if keydown(KEY_OK):
                # Try to place piece
                if piece.placed:
                    self.board.remove_piece(piece.numero)
                    piece.placed = False
                    self.show_message("Piece removed")
                elif self.board.place_piece(piece, self.cursor_row, self.cursor_col):
                    self.show_message("Piece placed!")
                    self.check_win()
                else:
                    self.show_message("Cannot place here")
            
            if keydown(KEY_EXE):
                piece.rotate()
                self.show_message("Rotated")
            
            if keydown(KEY_SHIFT):
                piece.mirror()
                self.show_message("Mirrored")
            
            if keydown(KEY_BACK):
                if piece.placed:
                    self.board.remove_piece(piece.numero)
                    piece.placed = False
                    self.show_message("Piece removed")
        
        elif self.state == "won":
            if keydown(KEY_OK):
                self.reset_game()
    
    def check_win(self):
        """Check if player has won."""
        if self.board.is_full():
            self.state = "won"
            self.message = "Victory!"
    
    def reset_game(self):
        """Reset game to initial state."""
        self.board.clear()
        for piece in self.pieces:
            piece.placed = False
        self.cursor_row = 0
        self.cursor_col = 0
        self.state = "playing"
        self.message = ""
    
    def draw_board(self):
        """Draw the game board."""
        # Draw board cells
        for r in range(self.board.height):
            for c in range(self.board.width):
                x = BOARD_X + c * CELL_SIZE
                y = BOARD_Y + r * CELL_SIZE
                
                cell_value = self.board.grid[r][c]
                if cell_value > 0:
                    # Filled cell - use piece color
                    color = PIECE_COLORS[(cell_value - 1) % len(PIECE_COLORS)]
                    fill_rect(x, y, CELL_SIZE, CELL_SIZE, color)
                else:
                    # Empty cell
                    fill_rect(x, y, CELL_SIZE, CELL_SIZE, COLOR_WHITE)
                
                # Draw cell border
                # Top border
                fill_rect(x, y, CELL_SIZE, 1, COLOR_BLACK)
                # Left border
                fill_rect(x, y, 1, CELL_SIZE, COLOR_BLACK)
                # Bottom border
                fill_rect(x, y + CELL_SIZE - 1, CELL_SIZE, 1, COLOR_BLACK)
                # Right border
                fill_rect(x + CELL_SIZE - 1, y, 1, CELL_SIZE, COLOR_BLACK)
        
        # Draw cursor
        piece = self.get_current_piece()
        if piece and not piece.placed:
            for dr, dc in piece.coords:
                r, c = self.cursor_row + dr, self.cursor_col + dc
                if 0 <= r < self.board.height and 0 <= c < self.board.width:
                    x = BOARD_X + c * CELL_SIZE + 2
                    y = BOARD_Y + r * CELL_SIZE + 2
                    color = PIECE_COLORS[(piece.numero - 1) % len(PIECE_COLORS)]
                    # Draw preview with semi-transparency effect (smaller square)
                    fill_rect(x, y, CELL_SIZE - 4, CELL_SIZE - 4, color)
    
    def draw_ui(self):
        """Draw user interface elements."""
        # Clear screen
        fill_rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_WHITE)
        
        # Title
        draw_string("PYTHOMINOS", 10, 5, COLOR_BLACK, COLOR_WHITE)
        
        # Board
        self.draw_board()
        
        # Piece indicator
        piece = self.get_current_piece()
        if piece:
            piece_text = f"Piece: {piece.numero}"
            draw_string(piece_text, 10, BOARD_Y + self.board.height * CELL_SIZE + 10, 
                       COLOR_BLACK, COLOR_WHITE)
        
        # Controls hint (smaller text)
        y_pos = BOARD_Y + self.board.height * CELL_SIZE + 25
        draw_string("OK:Place EXE:Rot", 10, y_pos, COLOR_GRAY, COLOR_WHITE)
        draw_string("SHIFT:Mirror", 10, y_pos + 12, COLOR_GRAY, COLOR_WHITE)
        
        # Message
        if self.message:
            draw_string(self.message, 10, SCREEN_HEIGHT - 20, COLOR_RED, COLOR_WHITE)
    
    def draw_win_screen(self):
        """Draw victory screen."""
        fill_rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_YELLOW)
        draw_string("VICTORY!", 100, 100, COLOR_BLACK, COLOR_YELLOW)
        draw_string("Press OK to play again", 50, 120, COLOR_BLACK, COLOR_YELLOW)
    
    def draw(self):
        """Main draw function."""
        if self.state == "playing":
            self.draw_ui()
        elif self.state == "won":
            self.draw_win_screen()
    
    def update(self):
        """Main update function."""
        self.update_message_timer()
        self.handle_input()
    
    def run(self):
        """Main game loop (for NumWorks)."""
        while True:
            self.update()
            self.draw()
            # Small delay to prevent too fast updates
            # NumWorks handles frame timing automatically


def main():
    """Entry point for NumWorks calculator."""
    game = Game()
    
    if NUMWORKS_MODE:
        # On NumWorks, run the game loop
        game.run()
    else:
        # In simulation mode, just show initial screen
        print("Pythominos for NumWorks - Simulation Mode")
        print("This version is designed to run on NumWorks calculator.")
        print("\nFeatures:")
        print("- 12 different puzzle pieces")
        print("- Board size: 12x5 cells")
        print("- Optimized for 320x222 screen")
        print("\nControls on NumWorks:")
        print("- Arrow keys: Move cursor")
        print("- OK: Place/Remove piece")
        print("- EXE: Rotate piece")
        print("- SHIFT: Mirror piece")
        game.draw_ui()


if __name__ == "__main__":
    main()
