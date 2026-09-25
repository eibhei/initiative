#! /usr/bin/env python3
from textual.app import App, ComposeResult
from textual.screen import Screen, ModalScreen
from textual.widget import Widget
from textual.widgets import (
    DataTable,
    Footer,
    Input,
    Label,
)

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

    name, player_name, init_roll, hp, ac = "Aragorn", "Viggo", 15, 30, 15
    initiative_order.append(Player(name, player_name, init_roll, hp, ac))

    name, player_name, init_roll, hp, ac = "Frodo", "Elijah", 18, 30, 15
    initiative_order.append(Player(name, player_name, init_roll, hp, ac))

    name, player_name, init_roll, hp, ac = "Gimli", "John", 5, 30, 15
    initiative_order.append(Player(name, player_name, init_roll, hp, ac))

    init_list = [
        (
            "Initiative",
            "Name",
            "Player",
            "Hit Points",
            "Armour Class",
            "Condition",
            "Notes",
        )
    ]
    for a in initiative_order:
        init_list.append((a.init_roll, a.name, a.player_name, a.hp, a.ac))

    return init_list

class LabelledInput(Widget):
    """The screen for adding a new actor to the initiative order"""
    DEFAULT_CSS = """
    LabelledInput {
        layout: horizontal;
        height: auto;
    }
    LabelledInput Label {
        padding: 1;
        width: 12;
        text-align: right;
    }
    LabelledInput Input {
        width: 1fr;
    }
    """

    def __init__(self, label: str, placeholder: str | None = None) -> None:
        super().__init__()
        self.label = label
        self.placeholder = placeholder if placeholder is not None else ""

    def compose(self) -> ComposeResult:
        yield Label(self.label)
        yield Input(placeholder=self.placeholder)

class AddActor(ModalScreen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield LabelledInput("Character")
        yield LabelledInput("Player name", "Leave blank for NPC")
        yield LabelledInput("Hit Points")
        yield LabelledInput("Armour Class")
        yield LabelledInput("Initiative", "Ctrl+R to roll")
        yield LabelledInput("Conditions")
        yield LabelledInput("Notes")

class InitiativeApp(App):
    """A Textual app to manage initiative."""
    CSS = """
    """
    ansi_color = True
    ENABLE_COMMAND_PALETTE = False
    BINDINGS = [
        ("n", "next_actor", "Next"),
        ("a", "add_actor", "Add"),
        ("^q", "quit", "Quit"),
    ]
    SCREENS = {"add_actor": AddActor}

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        for col in init_list[0]:
            table.add_column(col, key=col)
        table.add_rows(init_list[1:])
        table.fixed_rows = 0
        table.cursor_type = "row"
        table.sort("Initiative", "Name", reverse=True)

    def action_add_actor(self) -> None:
        self.push_screen(AddActor())

if __name__ == "__main__":
    init_list = main()
    app = InitiativeApp()
    app.run()
