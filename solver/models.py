from abc import ABC, abstractmethod

cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
rows = [1, 2, 3, 4, 5, 6, 7, 8]


class Figure(ABC):
    def __init__(self, current_field: str):
        self.current_field = current_field

    @abstractmethod
    def list_available_moves(self) -> list:
        pass

    @abstractmethod
    def validate_move(self, dest_field: str) -> bool:
        pass


class Pawn(Figure):
    def list_available_moves(self) -> list:
        col: str = self.current_field[0]
        row: int = int(self.current_field[1])
        if row == 8:
            return []
        else:
            return [f"{col}{row+1}"]

    def validate_move(self, dest_field: str) -> bool:
        avaliable_moves = self.list_available_moves()
        if dest_field in avaliable_moves:
            return True
        else:
            return False
