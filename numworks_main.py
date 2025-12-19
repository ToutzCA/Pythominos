import kandinsky
import ion
import time
from random import randint

# --- Constants ---
BLOCK_SIZE = 20
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
GRID_WIDTH = 12
GRID_HEIGHT = 10

# Center the grid
GRID_OFFSET_X = (SCREEN_WIDTH - (GRID_WIDTH * BLOCK_SIZE)) // 2
GRID_OFFSET_Y = (SCREEN_HEIGHT - (GRID_HEIGHT * BLOCK_SIZE)) // 2

# Colors (RGB)
COLORS = {
    0: (255, 255, 255),  # Background (White for better visibility on calc?) Or Black? Let's stick to Black background.
    1: (29, 43, 83),
    2: (126, 37, 83),
    3: (0, 135, 81),
    4: (171, 82, 54),
    5: (95, 87, 79),
    6: (194, 195, 199),
    7: (200, 200, 255), # Modified 7 to be visible against white if needed, but here against black
    8: (255, 0, 77),
    9: (255, 163, 0),
    10: (255, 236, 39),
    11: (0, 228, 54),
    12: (41, 173, 255),
    13: (100, 100, 100), # Grid lines
    14: (0, 0, 0)        # Background
}

GRAND_CHELEM = [
    [2, 3, 6, 11, 8, 4, 5, 10, 9, 1, 7, 12],
    [2, 3, 7, 9, 8, 5, 6, 4, 10, 1, 12, 11],
    [2, 4, 6, 7, 8, 1, 3, 9, 11, 5, 12, 10],
    [3, 4, 6, 7, 8, 1, 5, 2, 11, 10, 12, 9],
    [3, 6, 7, 9, 10, 2, 12, 11, 4, 1, 5, 8],
    [2, 3, 5, 6, 4, 9, 11, 10, 8, 12, 1, 7],
    [2, 3, 5, 7, 8, 1, 9, 10, 12, 4, 11, 6],
    [2, 3, 6, 10, 11, 8, 9, 12, 4, 1, 7, 5],
    [2, 3, 6, 8, 5, 11, 9, 7, 12, 10, 1, 4],
    [2, 4, 5, 8, 7, 10, 6, 1, 12, 9, 11, 3],
    [3, 4, 5, 10, 9, 1, 6, 11, 8, 12, 7, 2],
    [2, 6, 7, 9, 11, 3, 8, 4, 5, 10, 12, 1]
]

# --- Graphics Helpers ---
def draw_rect(x, y, w, h, color):
    kandinsky.fill_rect(x, y, w, h, color)

def draw_grid_background():
    # Clear screen
    draw_rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, COLORS[14])
    
    # Draw grid area
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            px = GRID_OFFSET_X + x * BLOCK_SIZE
            py = GRID_OFFSET_Y + y * BLOCK_SIZE
            # Draw cell border
            draw_rect(px, py, BLOCK_SIZE, BLOCK_SIZE, COLORS[13])
            # Draw cell interior (slightly smaller to show border)
            draw_rect(px + 1, py + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2, COLORS[14])

def draw_piece_block(grid_x, grid_y, color_idx):
    px = GRID_OFFSET_X + grid_x * BLOCK_SIZE
    py = GRID_OFFSET_Y + grid_y * BLOCK_SIZE
    draw_rect(px + 1, py + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2, COLORS[color_idx])

def clear_piece_block(grid_x, grid_y):
    px = GRID_OFFSET_X + grid_x * BLOCK_SIZE
    py = GRID_OFFSET_Y + grid_y * BLOCK_SIZE
    draw_rect(px + 1, py + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2, COLORS[14])

# --- Game Logic ---

class Piece:
    def __init__(self, numero, patron, plateau):
        self.numero = numero
        self.patron = patron
        self.plateau = plateau
        # Dplateau is used for the "moving" state in the original code
        # We will simplify: we just need to know where the piece is.
        
        self.cos_actuelles = self.cos_de_depart()
        self.rotation_anchor = [0, 0] # Will be set during rotation

    def cos_de_depart(self):
        coordinates = []
        for i, row in enumerate(self.patron):
            for j, val in enumerate(row):
                if val != 0:
                    coordinates.append([i, j])
        return coordinates

    def draw(self, clear=False):
        for x, y in self.cos_actuelles:
            if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT: # Safety check
                # Note: In original code, x seems to be row (y) and y seems to be col (x)?
                # Let's check: "coordinates.append([i, j])" where i is row index, j is col index.
                # So [row, col].
                # In draw_piece_block(grid_x, grid_y), we expect x, y.
                # So we should pass y, x.
                if clear:
                    clear_piece_block(y, x)
                else:
                    draw_piece_block(y, x, self.numero)

    def deplacement(self, dy, dx):
        # dx, dy are changes in row/col indices
        # dy is change in row (vertical), dx is change in col (horizontal)
        
        # Clear current position
        self.draw(clear=True)

        new_coordinates = []
        for r, c in self.cos_actuelles:
            new_r, new_c = r + dy, c + dx
            new_coordinates.append([new_r, new_c])

        # Check boundaries
        if all(0 <= r < len(self.plateau) and 0 <= c < len(self.plateau[0]) for r, c in new_coordinates):
            # Check collision with other pieces (values > 0 in plateau)
            # Note: The current piece is NOT in the plateau grid while moving in the original logic?
            # In original: "if not self.etat_deplacement: ... self.plateau[x][y] = 0"
            # We assume the piece is "picked up" so it's not in the grid.
            if all(self.plateau[r][c] == 0 for r, c in new_coordinates):
                self.cos_actuelles = new_coordinates
                self.draw(clear=False)
                return True
        
        # Re-draw at old position if move failed
        self.draw(clear=False)
        return False

    def rotate(self):
        self.draw(clear=True)
        
        # Anchor logic from original
        if self.numero in [6,8,4,5,10]:
            anchor = self.cos_actuelles[1]
        elif self.numero in [1, 2, 3, 7, 9, 11, 12]:
            anchor = self.cos_actuelles[2]
        else:
            anchor = self.cos_actuelles[0] # Fallback

        anchor_r, anchor_c = anchor[0], anchor[1]
        
        # Rotate 90 degrees: (r, c) -> (c, -r) relative to anchor
        new_coordinates = []
        for r, c in self.cos_actuelles:
            rel_r, rel_c = r - anchor_r, c - anchor_c
            # Rotate: new_rel_r = rel_c, new_rel_c = -rel_r
            rot_r, rot_c = rel_c, -rel_r
            new_r, new_c = rot_r + anchor_r, rot_c + anchor_c
            new_coordinates.append([new_r, new_c])

        if all(0 <= r < len(self.plateau) and 0 <= c < len(self.plateau[0]) for r, c in new_coordinates):
             if all(self.plateau[r][c] == 0 for r, c in new_coordinates):
                self.cos_actuelles = new_coordinates
                self.draw(clear=False)
                return True

        self.draw(clear=False)
        return False
    
    def symetrie(self):
        self.draw(clear=True)
        
        # Flip vertically relative to the piece's bounding box
        max_r = max(r for r, c in self.cos_actuelles)
        new_coordinates = []
        for r, c in self.cos_actuelles:
            new_r = max_r - r
            new_coordinates.append([new_r, c])
            
        # Re-align (simple approach: keep min_r same? Original does some shift)
        # Original: min_y = min(y...); decalage = min_y - min(y_new); y + decalage
        min_r_old = min(r for r, c in self.cos_actuelles)
        min_r_new = min(r for r, c in new_coordinates)
        diff = min_r_old - min_r_new
        
        final_coordinates = [[r + diff, c] for r, c in new_coordinates]

        if all(0 <= r < len(self.plateau) and 0 <= c < len(self.plateau[0]) for r, c in final_coordinates):
             if all(self.plateau[r][c] == 0 for r, c in final_coordinates):
                self.cos_actuelles = final_coordinates
                self.draw(clear=False)
                return True

        self.draw(clear=False)
        return False

    def place_on_plateau(self):
        for r, c in self.cos_actuelles:
            self.plateau[r][c] = self.numero

def create_piece(numero, plateau):
    # Definitions from original code
    patrons = {
        1: [[1], [1], [1], [1], [1]],
        2: [[2, 2], [2], [2], [2]],
        3: [[3], [3, 3], [3], [3]],
        4: [[4], [4, 4], [0, 4], [0, 4]],
        5: [[5], [5], [5, 5, 5]],
        6: [[6], [6, 6], [6, 6]],
        7: [[7, 7], [0, 7], [7, 7]],
        8: [[8, 8], [0, 8], [0, 8, 8]],
        9: [[9], [9, 9, 9], [0, 9]],
        10: [[10, 10, 10], [0, 10], [0, 10]],
        11: [[11], [11, 11], [0, 11, 11]],
        12: [[0, 12], [12, 12, 12], [0, 12]]
    }
    return Piece(numero, patrons[numero], plateau)

# --- Main Loop ---

def main():
    # Initialize Grid (12 rows, 12 cols? Original: width=12*32, height=10*32. So 12 cols, 10 rows?)
    # Wait, Pyxel init(width, height). 
    # Original: width = 12 * 32, height = 10 * 32.
    # So grid is 12 columns wide, 10 rows high?
    # Let's check Piece coordinates. "coordinates.append([i, j])" -> i is row, j is col.
    # "0 <= x < len(self.plateau) and 0 <= y < len(self.plateau[0])"
    # If plateau is [row][col], then len(plateau) is height (rows), len(plateau[0]) is width (cols).
    # So we need plateau to be 10 rows, 12 cols.
    
    plateau = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    
    draw_grid_background()
    
    # Game State
    level = 0
    pieces_indices = GRAND_CHELEM[level]
    current_piece_idx = 0
    
    # Create the first piece
    active_piece = create_piece(pieces_indices[current_piece_idx], plateau)
    active_piece.draw()
    
    kandinsky.draw_string("Level: " + str(level + 1), 5, 5)
    
    last_key_time = 0
    KEY_DELAY = 0.15

    while True:
        current_time = time.monotonic()
        
        if current_time - last_key_time > KEY_DELAY:
            if ion.keydown(ion.KEY_LEFT):
                active_piece.deplacement(0, -1) # dy=0, dx=-1
                last_key_time = current_time
            elif ion.keydown(ion.KEY_RIGHT):
                active_piece.deplacement(0, 1)
                last_key_time = current_time
            elif ion.keydown(ion.KEY_UP):
                active_piece.deplacement(-1, 0)
                last_key_time = current_time
            elif ion.keydown(ion.KEY_DOWN):
                active_piece.deplacement(1, 0)
                last_key_time = current_time
            elif ion.keydown(ion.KEY_OK) or ion.keydown(ion.KEY_EXE):
                # Place piece
                active_piece.place_on_plateau()
                current_piece_idx += 1
                if current_piece_idx < len(pieces_indices):
                    active_piece = create_piece(pieces_indices[current_piece_idx], plateau)
                    # Check if spawn is valid
                    if not active_piece.deplacement(0, 0): # Just check collision at spawn
                         kandinsky.draw_string("Game Over", 120, 100, (255,0,0))
                         break
                    active_piece.draw()
                else:
                    kandinsky.draw_string("You Win!", 120, 100, (0,255,0))
                    break
                last_key_time = current_time + 0.2 # Extra delay after placing
            elif ion.keydown(ion.KEY_BACK):
                # Rotate
                active_piece.rotate()
                last_key_time = current_time
            elif ion.keydown(ion.KEY_SHIFT):
                # Symmetry
                active_piece.symetrie()
                last_key_time = current_time

        # Small sleep to save battery/cpu
        time.sleep(0.01)

if __name__ == "__main__":
    main()
