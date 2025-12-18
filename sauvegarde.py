import json
from pathlib import Path
from typing import Any, Dict, List, Optional

# HOTFIX: add metadata, robust path handling, UTF-8 encoding and pretty JSON
_SAVE_VERSION = 1

def save_game_file(
    mode_grand_chelem: bool,
    niveau_grand_chelem: int,
    pieces_selectionnees: List[int],
    plateau: List[List[int]],
    etape: int,
    filename: str = "katamino_save.json",
) -> bool:
    """Persist current game state to a JSON file.

    - Ensures parent folder exists when a path is provided.
    - Adds a small metadata block for future compatibility.
    """
    payload: Dict[str, Any] = {
        "_meta": {"version": _SAVE_VERSION},
        "mode_grand_chelem": mode_grand_chelem,
        "niveau_grand_chelem": niveau_grand_chelem,
        "pieces_selectionnees": pieces_selectionnees,
        "plateau": plateau,
        "etape": etape,
    }
    path = Path(filename)
    try:
        if path.parent and str(path.parent) not in ("", "."):
            path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Game saved to {path}")
        return True
    except Exception as e:
        print(f"Failed to save game to {path}: {e}")
        return False


def load_game_file(filename: str = "katamino_save.json") -> Optional[Dict[str, Any]]:
    """Load a game state from JSON if it exists; returns None otherwise."""
    path = Path(filename)
    try:
        if not path.exists():
            print(f"Save file not found: {path}")
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
        print(f"Game loaded from {path}")
        return data
    except Exception as e:
        print(f"Failed to load game from {path}: {e}")
        return None