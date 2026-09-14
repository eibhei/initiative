#! /usr/bin/env python3
from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer, Header

from player import Player
from roll_dice import roll_dice

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

    sorted_initiative = sorted(initiative_order, key=lambda x: x.init_roll, reverse=True)

    init_list = [
        ("Initiative Roll", "Name", "Player Name", "Hit Points", "Armour Class")
    ]

    for a in sorted_initiative:
        init_list.append((a.init_roll, a.name, a.player_name, a.hp, a.ac))

    return init_list

class InitiativeApp(App):
    """A Textual app to manage initiative."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit the app")
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*init_list[0])
        table.add_rows(init_list[1:])

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    init_list = main()
    app = InitiativeApp()
    app.run()
