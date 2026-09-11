class Actor:
    def __init__(self, name: str, init_roll: int, hp: int, ac:int) -> None:
        self.name = name
        self.hp = hp
        self.ac = ac
        self.condition = ""
