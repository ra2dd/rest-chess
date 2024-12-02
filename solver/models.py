from abc import ABC, abstractmethod
import logging
from solver.figure_exceptions import (
    ArrayLengthsNotEqualError,
)

logger = logging.getLogger(__name__)


class Figure(ABC):
    __cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
    __rows = [1, 2, 3, 4, 5, 6, 7, 8]

    # Minimum and maximum size of the chess board
    __min_index = 0
    __max_index = 7
    _max_moves = __max_index + 1

    def __init__(self, current_field: str):
        self.current_field = current_field
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

    def __indexes_in_board(self, col_index: int, row_index: int) -> bool:
        if col_index > self.__max_index or col_index < self.__min_index:
            return False
        elif row_index > self.__max_index or row_index < self.__min_index:
            return False
        else:
            return True

    def _list_straight_moves(self, jump_col: list, jump_row: list) -> set:
        moves = set()

        self.__check_array_lengths_equal(len(jump_col), len(jump_row))

        for turn in range(len(jump_col)):
            col_index: int = self.__cols.index(self.col)
            row_index: int = self.__rows.index(self.row)

            for _ in range(self._max_moves):
                # Move a step
                col_index += jump_col[turn]
                row_index += jump_row[turn]

                if not self.__indexes_in_board(col_index, row_index):
                    break

                # Append move to set
                moves.add(f"{self.__cols[col_index]}{self.__rows[row_index]}")
        return moves

    def _list_close_moves(self, jump_col: list, jump_row: list) -> set:
        moves = set()

        self.__check_array_lengths_equal(len(jump_col), len(jump_row))

        for turn in range(len(jump_col)):
            col_index: int = self.__cols.index(self.col)
            row_index: int = self.__rows.index(self.row)

            # Move a step
            col_index += jump_col[turn]
            row_index += jump_row[turn]

            if not self.__indexes_in_board(col_index, row_index):
                continue

            # Append move to set
            moves.add(f"{self.__cols[col_index]}{self.__rows[row_index]}")
        return moves

    def __check_array_lengths_equal(self, col_len, row_len):
        if col_len != row_len:
            logger.error(
                f"Array lengths are not equal. Column: {col_len} != Row: {row_len}"
            )
            raise ArrayLengthsNotEqualError("Provided array lenghts are not equal.")


class Pawn(Figure):
    def list_available_moves(self) -> set:
        print(self._max_moves)
        if self.row == self._max_moves:
            return set()
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
