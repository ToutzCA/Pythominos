import json

def save_game_file(mode_grand_chelem, niveau_grand_chelem, pieces_selectionnees, plateau, etape, filename="katamino_save.json"):
    game_data = {
        "mode_grand_chelem": mode_grand_chelem,
        "niveau_grand_chelem": niveau_grand_chelem,
        "pieces_selectionnees": pieces_selectionnees,
        "plateau": plateau,
        "etape": etape 
    }
    with open(filename, 'w') as f:
        json.dump(game_data, f)
    print(f"Game saved to {filename}")
    return True

def load_game_file(filename="katamino_save.json"):
    try:
        with open(filename, 'r') as f:
            game_data = json.load(f)
        print(f"Game loaded from {filename}")
        return game_data
    except Exception as e:
        print(f"Failed to load game: {e}")
        return None