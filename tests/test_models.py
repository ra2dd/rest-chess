from solver.models import Pawn


def test_initialization():
    pawn = Pawn("A2")
    assert pawn.current_field == "A2", "Pawn should be initialized at A2"


def test_pawn_list_available_moves():
    pawn = Pawn("A2")
    assert pawn.list_available_moves() == ["A3"]

    pawn = Pawn("A8")
    assert pawn.list_available_moves() == []


def test_pawn_validate_move():
    pawn = Pawn("A2")
    assert pawn.validate_move("A3") is True
    assert pawn.validate_move("B5") is False
