from abc import ABC, abstractmethod


class Figure(ABC):
    _cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
    _rows = [1, 2, 3, 4, 5, 6, 7, 8]

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

    @staticmethod
    def _indexes_in_board(col_index, row_index):
        if col_index >= 8 or col_index < 0:
            return False
        elif row_index >= 8 or row_index < 0:
            return False
        else:
            return True


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
                col_index = self._cols.index(self.col) + jump_col[turn]
                row_index = self._rows.index(self.row) + jump_row[turn]

                # Make a one tile jump left or right
                if jump_col[turn] == 0:
                    col_index += jump_dir[direction]
                else:
                    row_index += jump_dir[direction]

                # Check if after a move a figure is in the board
                if self._indexes_in_board(col_index, row_index) is False:
                    continue

                # Append move to set
                moves.add(f"{self._cols[col_index]}{self._rows[row_index]}")
        return moves


class Bishop(Figure):
    def list_available_moves(self) -> set:
        moves = set()
        jump_col = [1, 1, -1, -1]
        jump_row = [1, -1, 1, -1]

        for turn in range(4):
            col_index = self._cols.index(self.col)
            row_index = self._rows.index(self.row)
            limit = 0
            while limit < 9:
                # Move a step
                col_index += jump_col[turn]
                row_index += jump_row[turn]

                if self._indexes_in_board(col_index, row_index) is False:
                    break

                # Append move to set
                moves.add(f"{self._cols[col_index]}{self._rows[row_index]}")
                limit += 1

            if limit >= 8:
                raise Exception("Chess board was iterated out of bounds")
        return moves
