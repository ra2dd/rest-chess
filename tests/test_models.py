from solver.models import Pawn, Knight


def test_initialization():
    pawn = Pawn("A2")
    assert pawn.current_field == "A2", "Pawn should be initialized at A2"
    assert pawn.col == "A"
    assert pawn.row == 2


def test_pawn_list_available_moves():
    pawn = Pawn("A2")
    assert pawn.list_available_moves() == ["A3"]

    pawn = Pawn("A8")
    assert pawn.list_available_moves() == []


def test_pawn_validate_move():
    pawn = Pawn("A2")
    assert pawn.validate_move("A3") is True
    assert pawn.validate_move("B5") is False


def test_knight_list_available_moves():
    knight = Knight("D4")
    expected_moves = {"C6", "E6", "F3", "F5", "C2", "E2", "B3", "B5"}
    assert knight.list_available_moves() == expected_moves

    knight = Knight("A8")
    expected_moves = {"B6", "C7"}
    assert knight.list_available_moves() == expected_moves

    knight = Knight("H1")
    expected_moves = {"F2", "G3"}
    assert knight.list_available_moves() == expected_moves


def test_knight_validate_move():
    knight = Knight("D4")
    assert knight.validate_move("C6") is True
    assert knight.validate_move("D6") is False
