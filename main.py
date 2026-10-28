#! /usr/bin/env python3
from textual.app import App, ComposeResult
from textual.containers import Center, VerticalScroll
from textual.screen import ModalScreen
from textual.widget import Widget
from textual.widgets import (
    Button,
    DataTable,
    Footer,
    Header,
    Input,
    Label,
    ProgressBar,
    Rule
)

from actor import Actor

# from roll_dice import roll_dice


def main():
    init_headings = [
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

    return init_headings

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

    @property
    def value(self) -> str:
        return self.query_one(Input).value

class RoundTracker(Widget):
    """The round tracker heading for the main screen"""

    def __init__(self, round_number: int | 0 = 0) -> None:
        super().__init__()
        self.round_number = round_number

    def compose(self) -> ComposeResult:
        yield Label(f"Round number: {self.round_number}")
        yield ProgressBar(total=100, show_eta=False, show_percentage=False)
        yield Button("Next", variant="primary", id="next")


class AddActor(ModalScreen):
    """Screen for entering new actors into initiative order"""

    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            # Add typing to this section where appropriate
            #   https://textual.textualize.io/widgets/input/#input-types
            LabelledInput("Character name", id="name"),
            LabelledInput("Player name", "Leave blank for NPC", id="player"),
            LabelledInput("Hit Points", id="hp"),
            LabelledInput("Armour Class", id="ac"),
            LabelledInput("Initiative", "Ctrl+R to roll", id="init"),       # Need to code this in
            LabelledInput("Conditions", id="status"),
            LabelledInput("Notes", id="notes"),
            Button("Submit", variant="primary", id="submit"),
            id="overlay"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Validate inputs

            # Character must be a string
            # Player name must be a string or empty
            # Hit points must be an integar
            # AC must be an integar
            # Initiative must be an integar
            # Conditions must be member of the conditions list
            #   A few ways to do this:
            #       https://textual.textualize.io/widgets/checkbox/     <- I think this is the way to do it
            #       https://textual.textualize.io/widgets/list_view/
            #       https://textual.textualize.io/widgets/option_list/
            #       https://textual.textualize.io/widgets/radiobutton/

        # Parse inputs
        input_name = self.query_one("#name", LabelledInput).value
        input_player = self.query_one("#player", LabelledInput).value
        input_hp = self.query_one("#hp", LabelledInput).value
        input_ac = self.query_one("#ac", LabelledInput).value
        input_init = self.query_one("#init", LabelledInput).value
        input_cond = self.query_one("#status", LabelledInput).value
        input_notes = self.query_one("#notes", LabelledInput).value

        new_actor = Actor(
            input_name,
            int(input_init),
            int(input_hp),
            int(input_ac),
            player_name = input_player if input_player != "" else "DM",
            condition = input_cond,
            notes = input_notes
        )

        self.dismiss(new_actor)

    def roll_for_initiative(self) -> None:
        pass
        # Confirm focused input has id "init"
        # Do the roll (how do we specify the bonus?)

class InitiativeApp(App):
    """A Textual app to manage initiative."""

    ansi_color = True
    CSS_PATH = "app.tcss"
    ENABLE_COMMAND_PALETTE = False
    TITLE = "Initiative Tracker"

    BINDINGS = [
        ("n", "next_actor", "Next"),
        ("a", "add_actor", "Add"),
        ("^q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield DataTable(id="initiative_table")
        yield Rule(line_style="dashed")
        yield RoundTracker()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        for col in init_list[0]:
            table.add_column(col, key=col)
        table.add_rows(init_list[1:])
        table.fixed_rows = 0
        table.cursor_type = "row"
        table.sort("Initiative", "Name", reverse=True)

        current_round = 0

    def action_add_actor(self) -> None:
        self.push_screen(AddActor(), callback=self.on_actor_added)

        character_input = self.screen.query_one(Input)
        self.set_focus(character_input) #FIXME: This works, but it's not a robust solution
                                        #       And should maybe just be added in the screen constructor?

    def on_actor_added(self, new_actor: Actor | None) -> None:
        if new_actor is None:
            return

        table = self.query_one(DataTable)
        table.add_row((new_actor.init_roll), (new_actor.name), (new_actor.player_name), (new_actor.hp), (new_actor.ac), (new_actor.condition), (new_actor.notes))

    def next_turn(self) -> None:
        pass

if __name__ == "__main__":
    init_list = main()
    app = InitiativeApp()
    app.run()
