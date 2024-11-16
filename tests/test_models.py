from solver.models import Figure, Pawn, Knight, Bishop, Rook, Queen


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


def test_bishop_list_available_moves():
    bishop = Bishop("C3")
    expected_moves = {"A1", "B2", "D4", "E5", "F6", "G7", "H8", "B4", "A5", "D2", "E1"}
    assert bishop.list_available_moves() == expected_moves

    bishop = Bishop("F5")
    expected_moves = {"E6", "D7", "C8", "G6", "H7", "G4", "H3", "E4", "D3", "C2", "B1"}
    assert bishop.list_available_moves() == expected_moves


def test_col_rows_are_in_the_board():
    assert Figure._indexes_in_board(0, 0) is True
    assert Figure._indexes_in_board(7, 7) is True
    assert Figure._indexes_in_board(8, 8) is False
    assert Figure._indexes_in_board(-1, -1) is False


def test_rook_list_available_moves():
    rook = Rook("E3")
    # fmt: off
    expected_moves = {
        "E1", "E2", "E4", "E5", "E6", "E7", "E8",
        "A3", "B3", "C3", "D3", "F3", "G3", "H3"
        }
    # fmt: on
    assert rook.list_available_moves() == expected_moves


def test_queen_list_available_moves():
    queen = Queen("C5")
    # fmt: off
    expected_moves = {
        "C1", "C2", "C3", "C4", "C6", "C7", "C8", "A5", "B5",
        "D5", "E5", "F5", "G5", "H5", "D6", "E7", "F8", "B6",
        "A7", "D4", "E3", "F2", "G1", "B4", "A3"
        }
    # fmt: on
    assert queen.list_available_moves() == expected_moves
