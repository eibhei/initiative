class Actor:
    def __init__(self, name: str, init_roll: int, hp: int, ac:int) -> None:
        self.name = name
        self.hp = hp
        self.ac = ac
        self.init_roll = init_roll
        self.condition = ""

    def take_damage(self, total):
        pass

    def heal_damage(self, total):
        pass

    def gain_condition(self, condition):
        pass
