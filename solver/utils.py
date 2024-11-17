from flask import jsonify
from solver.models import Figure, Pawn, Knight, Bishop, Rook, Queen, King
from typing import Union


def validate_field(field: str) -> bool:
    cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
    rows = [1, 2, 3, 4, 5, 6, 7, 8]

    field = str(field).upper()
    if len(field) != 2:
        return False
    if field[1].isnumeric() is False:
        return False
    if field[0] not in cols or int(field[1]) not in rows:
        return False
    return True


def get_figure_object(figure: str, field: str) -> Union[Figure, bool]:
    figure = str(figure).lower()

    if figure == "pawn":
        return Pawn(field)
    elif figure == "knight":
        return Knight(field)
    elif figure == "bishop":
        return Bishop(field)
    elif figure == "rook":
        return Rook(field)
    elif figure == "queen":
        return Queen(field)
    elif figure == "king":
        return King(field)
    else:
        return False


def create_moves_res(figure, field, error=None, moves=[]):
    return jsonify(
        {
            "availableMoves": list(moves),
            "error": error,
            "figure": figure.lower(),
            "currentField": field,
        }
    )


def create_validate_res(is_valid, figure, field, dest, error=None):
    return jsonify(
        {
            "move": is_valid,
            "figure": figure,
            "error": error,
            "currentField": field,
            "destField": dest,
        }
    )
