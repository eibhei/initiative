from conditions import Condition


class Actor:
    def __init__(self, name: str, init_roll: int, hp: int, ac:int) -> None:
        self.name = name
        self.hp = hp
        self.ac = ac
        self.init_roll = init_roll
        self.condition = ""

    def take_damage(self, total: int):
        pass

    def heal_damage(self, total: int):
        pass

    def gain_condition(self, condition: Condition):
        pass

    def add_note(self):
        pass
