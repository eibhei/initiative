from conditions import Condition


class Actor:
    def __init__(
        self,
        name: str,
        init_roll: int,
        hp: int,
        ac: int,
        player_name: str | None = None,
        condition: str | None = None,
        notes: str | None = None
    ) -> None:
        self.name = name
        self.player_name = player_name
        self.hp = hp
        self.ac = ac
        self.init_roll = init_roll
        self.condition = condition
        self.notes = notes

    def take_damage(self, total: int):
        pass

    def heal_damage(self, total: int):
        pass

    def gain_condition(self, condition: Condition):
        pass

    def add_note(self):
        pass
