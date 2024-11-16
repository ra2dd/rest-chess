from abc import ABC, abstractmethod

cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
rows = [1, 2, 3, 4, 5, 6, 7, 8]


class Figure(ABC):
    def __init__(self, current_field: str):
        self.current_field: str = current_field
        self.col: str = self.current_field[0]
        self.row: int = int(self.current_field[1])

    @abstractmethod
    def list_available_moves(self) -> list | set:
        pass

    def validate_move(self, dest_field: str) -> bool:
        avaliable_moves: list | set = self.list_available_moves()
        if dest_field in avaliable_moves:
            return True
        else:
            return False


class Pawn(Figure):
    def list_available_moves(self) -> list:
        if self.row == 8:
            return []
        else:
            return [f"{self.col}{self.row+1}"]


class Knight(Figure):
    def list_available_moves(self) -> set:
        moves = set()
        jump_col = [2, -2, 0, 0]
        jump_row = [0, 0, 2, -2]
        jump_dir = [1, -1]

        for turn in range(4):
            for direction in range(2):
                # Make a two tile jump in certain direction
                col_index = cols.index(self.col) + jump_col[turn]
                row_index = rows.index(self.row) + jump_row[turn]

                # Make a one tile jump left or right
                if jump_col[turn] == 0:
                    col_index += jump_dir[direction]
                else:
                    row_index += jump_dir[direction]

                # Check if after a move a figure is out of board
                if col_index >= len(cols) or col_index < 0:
                    continue
                if row_index >= len(rows) or row_index < 0:
                    continue

                # Append move to set
                moves.add(f"{cols[col_index]}{rows[row_index]}")
        return moves
