from actor import Actor


class InitiativeList:
    def __init__(self, actors: list[Actor]) -> None:
        self.actors: list[Actor] = actors
        self.current_turn_index: int = 0
        self.current_round: int = 0

        # Ensure list is sorted on init
        self.sort_list()

    def sort_list(self) -> None:
        self.actors = sorted(self.actors, key=lambda a: a.init_roll, reverse=True)

    def get_current_turn(self) -> int:
        return self.current_turn_index

    def get_current_round(self) -> int:
        return self.current_round

    def next(self):
        current_index = int(self.get_current_turn())

        # Loop back around to the start if necessary
        if current_index == 0 and self.current_round == 0:
            self.current_round = 1
        elif current_index + 1 == len(self.actors):
            self.current_turn_index = 0
            self.current_round += 1
        else:
            self.current_turn_index += 1

    def previous(self):
        current_index = int(self.get_current_turn())

        # Loop back around to the end if necessary
        if current_index > 0:
            self.current_turn_index = current_index - 1
            self.current_round -= 1
        else:
            self.current_turn_index -= 1

    def add_actor(self, actor: Actor):
        current_index = int(self.get_current_turn())
        current_actor = self.actors[current_index]

        self.actors.append(actor)
        self.sort_list()

        if self.actors.index(current_actor) != current_index:
            self.current_turn_index = self.actors.index(current_actor)

    def remove_actor(self, actor: Actor):
        current_index = int(self.get_current_turn())
        current_actor = self.actors[current_index]

        if self.actors.index(current_actor) != current_index:
            self.current_turn_index = self.actors.index(current_actor)
            self.actors.remove(actor)
        else:
            self.actors.remove(actor)
