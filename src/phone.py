from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if number_of_sim == 0 or not isinstance(number_of_sim, int):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

        self.number_of_sim = number_of_sim

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(self, Phone):
            return self.quantity + other.quantity

    @property
    def number_of_sim(self) -> int:
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        if value == 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = value