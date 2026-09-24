#! /usr/bin/env python3
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import DataTable, Footer, Header, Input

from player import Player
# from roll_dice import roll_dice


def main():
    initiative_order = []
    # name = input("Character name: ")
    # player_name = input("Player name: ")
    # init_roll = int(input("Initiative roll: "))
    # hp = int(input("Hit points: "))
    # ac = int(input("Armour class: "))

    # initiative_order.append(Player(name, player_name, init_roll, hp, ac))

    name = "Aragorn"
    player_name = "Viggo"
    init_roll = 15
    hp = 30
    ac = 15

    initiative_order.append(Player(name, player_name, init_roll, hp, ac))

    name = "Frodo"
    player_name = "Elijah"
    init_roll = 18
    hp = 30
    ac = 15

    initiative_order.append(Player(name, player_name, init_roll, hp, ac))

    name = "Gimli"
    player_name = "John"
    init_roll = 5
    hp = 30
    ac = 15

    initiative_order.append(Player(name, player_name, init_roll, hp, ac))
    init_list = [
        ("Initiative", "Name", "Player", "Hit Points", "Armour Class")
    ]

    for a in initiative_order:
        init_list.append((a.init_roll, a.name, a.player_name, a.hp, a.ac))

    return init_list


class InitiativeApp(App):
    """A Textual app to manage initiative."""
    # ansi_color=True
    ENABLE_COMMAND_PALETTE = False
    BINDINGS = [
        ("n", "next_actor", "Next turn"),
        ("a", "add_actor", "Add"),
        ("^q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield DataTable()
        with Horizontal(id="input-bar"):
            yield Input(id="name", placeholder="Actor name")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        for col in init_list[0]:
            table.add_column(col, key=col)
        # table.add_columns(*init_list[0])
        table.add_rows(init_list[1:])
        table.fixed_rows = 0
        table.cursor_type = "row"
        table.sort("Initiative", "Name", reverse=True)

    def action_add_actor(self) -> None:
        table = self.query_one(DataTable)
        name_input = self.query_one("#name", Input)
        name = name_input.value.strip()
        if not name:
            return

        key = f"{name}_{table.row_count}"
        table.add_row(name, "?", "?", key=key)

        name_input.value = ""

if __name__ == "__main__":
    init_list = main()
    app = InitiativeApp()
    app.run()
