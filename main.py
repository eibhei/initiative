#! /usr/bin/env python3
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.screen import ModalScreen
from textual.widget import Widget
from textual.widgets import (
    Button,
    DataTable,
    Footer,
    Header,
    Input,
    Label,
)

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

    def __init__(self, label: str, placeholder: str | None = None, id: str | None = None) -> None:
        super().__init__()
        self.label = label
        self.placeholder = placeholder if placeholder is not None else ""
        self.id = id if id is not None else ""

    def compose(self) -> ComposeResult:
        yield Label(self.label)
        yield Input(placeholder=self.placeholder, id=self.id)

class AddActor(ModalScreen):
    """Screen for entering new actors into initiative order"""

    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            # Add typing to this section where appropriate
            #   https://textual.textualize.io/widgets/input/#input-types
            LabelledInput("Character", id="char"),
            LabelledInput("Player name", "Leave blank for NPC", id="player"),
            LabelledInput("Hit Points", id="hp"),
            LabelledInput("Armour Class", id="ac"),
            LabelledInput("Initiative", "Ctrl+R to roll", id="init"),       # Need to code this in
            LabelledInput("Conditions", id="status"),
            LabelledInput("Notes", id="notes"),
            Button("Submit", variant="primary", id="submit"),
            id="overlay"
        )

    def on_submit(self, event: Button.Pressed) -> None:
        if event.button.id == "submit":
            # Validate inputs 
                # Character must be a string
                # Player name must be a string or None 
                # Hit points must be an integar
                # AC must be an integar
                # Initiative must be an integar
                # Conditions must be None or member of the conditions list 
                # Notes must be None or string
            # Make sure everything is in order
            # Return data in the format that add_row() requires
                # https://textual.textualize.io/widgets/data_table/#textual.widgets._data_table.DataTable.add_row
            # Query the input here; have a look at the latest conversation with Boots
            pass
        
    def roll_for_initiative() -> None:
        pass
        # Confirm focused input has id "init"
        # Do the roll (how do we specify the bonus?)

class InitiativeApp(App):
    """A Textual app to manage initiative."""

    ansi_color = True
    CSS_PATH = "app.tcss"
    ENABLE_COMMAND_PALETTE = False

    BINDINGS = [
        ("n", "next_actor", "Next"),
        ("a", "add_actor", "Add"),
        ("^q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield DataTable(id="initiative_table")
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

        character_input = self.screen.query_one(Input)
        self.set_focus(character_input) #FIXME: This works, but it's not a robust solution

if __name__ == "__main__":
    init_list = main()
    app = InitiativeApp()
    app.run()
