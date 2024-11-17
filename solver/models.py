from abc import ABC, abstractmethod


class Figure(ABC):
    _cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
    _rows = [1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, current_field: str):
        self.current_field: str = current_field
        self.col: str = self.current_field[0]
        self.row: int = int(self.current_field[1])

    @abstractmethod
    def list_available_moves(self) -> set:
        pass

    def validate_move(self, dest_field: str) -> bool:
        avaliable_moves: set = self.list_available_moves()
        if dest_field in avaliable_moves:
            return True
        else:
            return False

    @staticmethod
    def _indexes_in_board(col_index: int, row_index: int) -> bool:
        if col_index >= 8 or col_index < 0:
            return False
        elif row_index >= 8 or row_index < 0:
            return False
        else:
            return True

    def _list_straight_moves(self, jump_col: list, jump_row: list) -> set:
        moves = set()

        if len(jump_col) != len(jump_row):
            raise Exception("Provided array lenghts are not equal.")

        for turn in range(len(jump_col)):
            col_index: int = self._cols.index(self.col)
            row_index: int = self._rows.index(self.row)
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

    def _list_close_moves(self, jump_col: list, jump_row: list) -> set:
        moves = set()

        if len(jump_col) != len(jump_row):
            raise Exception("Provided array lenghts are not equal.")

        for turn in range(len(jump_col)):
            col_index: int = self._cols.index(self.col)
            row_index: int = self._rows.index(self.row)

            # Move a step
            col_index += jump_col[turn]
            row_index += jump_row[turn]

            if self._indexes_in_board(col_index, row_index) is False:
                continue

            # Append move to set
            moves.add(f"{self._cols[col_index]}{self._rows[row_index]}")
        return moves


class Pawn(Figure):
    def list_available_moves(self) -> set:
        if self.row == 8:
            return {}
        else:
            return {f"{self.col}{self.row+1}"}


class Knight(Figure):
    def list_available_moves(self) -> set:
        jump_col = [2, -2, 2, -2, 1, 1, -1, -1]
        jump_row = [1, 1, -1, -1, 2, -2, 2, -2]
        return self._list_close_moves(jump_col, jump_row)


class Bishop(Figure):
    def list_available_moves(self) -> set:
        jump_col = [1, 1, -1, -1]
        jump_row = [1, -1, 1, -1]
        return self._list_straight_moves(jump_col, jump_row)


class Rook(Figure):
    def list_available_moves(self) -> set:
        jump_col = [1, -1, 0, 0]
        jump_row = [0, 0, 1, -1]
        return self._list_straight_moves(jump_col, jump_row)


class Queen(Figure):
    def list_available_moves(self) -> set:
        jump_col = [1, 1, -1, -1, 1, -1, 0, 0]
        jump_row = [1, -1, 1, -1, 0, 0, 1, -1]
        return self._list_straight_moves(jump_col, jump_row)


class King(Figure):
    def list_available_moves(self) -> set:
        jump_col = [1, 1, -1, -1, 1, -1, 0, 0]
        jump_row = [1, -1, 1, -1, 0, 0, 1, -1]
        return self._list_close_moves(jump_col, jump_row)
