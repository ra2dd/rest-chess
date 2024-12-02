from flask import jsonify
from solver.models import Figure, Pawn, Knight, Bishop, Rook, Queen, King


def validate_field(field: str) -> bool:
    cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    correct_field_len = 2

    field = str(field).upper()
    if len(field) != correct_field_len:
        return False
    if not field[1].isnumeric():
        return False
    if field[0] not in cols or int(field[1]) not in rows:
        return False
    return True


def validate_figure(figure: str) -> bool:
    return figure in {"pawn", "knight", "bishop", "rook", "queen", "king"}


def get_figure_object(figure: str, field: str) -> Figure:
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
