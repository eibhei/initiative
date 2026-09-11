from actor import Actor


class Player(Actor):
    def __init__(self, name, player_name, init_roll, hp, ac):
        super().__init__(name, init_roll, hp, ac)
        self.player_name = player_name

    def death_save(self):
        pass
