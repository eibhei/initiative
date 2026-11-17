#!/usr/bin/env python3
from mimetypes import init

from textual import on
from textual.app import App, ComposeResult
from textual.containers import (
    Container,
    Horizontal,
    HorizontalGroup,
    Vertical,
    VerticalGroup,
    VerticalScroll,
)
from textual.reactive import reactive
from textual.screen import ModalScreen
from textual.widget import Widget
from textual.widgets import (
    Button,
    ContentSwitcher,
    DataTable,
    Footer,
    Header,
    Input,
    Label,
    ProgressBar,
    Select,
    Static,
)

from actor import Actor
from constants import HEADINGS
from initiative import InitiativeList
from roll_dice import roll_dice


class LabelledInput(Widget):
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

class AddActor(ModalScreen):
    """Screen for entering new actors into initiative order"""

    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            # Add typing to this section where appropriate
            #   https://textual.textualize.io/widgets/input/#input-types
            LabelledInput("Character name", id="input_name"),
            LabelledInput("Player name", "Leave blank for NPC", id="input_player"),
            LabelledInput("Hit Points", id="input_hp"),
            LabelledInput("Armour Class", id="input_ac"),
            LabelledInput("Initiative", "Ctrl+R to roll", id="input_init"),       # Need to code this in
            LabelledInput("Conditions", id="input_status"),
            LabelledInput("Notes", id="input_notes"),
            Button("Submit", variant="primary", id="input_submit"),
            id="overlay"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Validate inputs
        # Conditions must be member of the conditions list
        #   A few ways to do this:
        #       https://textual.textualize.io/widgets/checkbox/     <- I think this is the way to do it
        #       https://textual.textualize.io/widgets/list_view/
        #       https://textual.textualize.io/widgets/option_list/
        #       https://textual.textualize.io/widgets/radiobutton/
        #       https://textual.textualize.io/widgets/select/       <- Or this might be good actually

        # Parse inputs
        input_name = self.query_one("#input_name", LabelledInput).value
        input_player = self.query_one("#input_player", LabelledInput).value
        input_hp = self.query_one("#input_hp", LabelledInput).value
        input_ac = self.query_one("#input_ac", LabelledInput).value
        input_init = self.query_one("#input_init", LabelledInput).value
        input_cond = self.query_one("#input_status", LabelledInput).value
        input_notes = self.query_one("#input_notes", LabelledInput).value

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

class InitiativeApp(App):
    """A Textual app to manage initiative."""
    # ansi_color = True
    CSS_PATH = "new_app.tcss"
    ENABLE_COMMAND_PALETTE = False
    TITLE = "Initiative Tracker"

    BINDINGS = [
        ("^q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Container(
                VerticalGroup(
                    Static("Press Next to start", id="round_number"),
                    ProgressBar(total=len(initiative.actors) + 1, show_eta=False, show_percentage=False, id="progress_bar"),
                    id="roundinfo"
                ),
                Static("Character name,\nand player", id="current_actor"),
                Static("Status: \n", id="conditions"),
                id="top"
            ),
            Container(
                # Need to figure out how to put in a content switcher
                DataTable(id="initiative-table"),
                id="middle"
            ),
            Horizontal(
                Button("Add", classes="buttons", id="add-button"),
                Button("Edit", classes="buttons", id="edit-button"),
                Container(id="gap"),
                Button("Prev", classes="buttons", id="prev-button"),
                Button("Next", classes="buttons", id="next-button"),
                id="bottom"
            ),
        )
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*HEADINGS)
        for actor in initiative.actors:
            table.add_row(actor.init_roll, actor.name, actor.player_name, actor.hp, actor.ac)
        table.show_cursor = False
        table.cursor_type = "row"

    # Method for updating everything, without using reactives
    def update_widgets(self):
        # Grab the necessary information
        round_number = initiative.get_current_round()
        current_turn = initiative.get_current_turn()
        current_actor = initiative.actors[current_turn]
        round_progress = initiative.current_turn_index + 1

        # Get the widgets to update
        round_number_display = self.query_one("#round_number")
        current_actor_display = self.query_one("#current_actor")
        progress_bar_display = self.query_one('#progress_bar')
        table = self.query_one("#initiative-table")

        # Update the widgets
        round_number_display.update(content=f'Round {round_number}')
        current_actor_display.update(content=f'{current_actor.name}\n{current_actor.player_name}')
        progress_bar_display.update(total=len(initiative.actors), progress=round_progress)
        table.show_cursor = True
        table.move_cursor(row=initiative.current_turn_index)


    # Move around the turn order with next and previous buttons
    @on(Button.Pressed, '#next-button, #prev-button')
    def move_turn(self, event: Button.Pressed) -> None:
        # Identify the direction of travel and run the matching function
        direction = event.button.id.partition("-")[0]
        if direction == "next":
            initiative.next()
        if direction == "prev":
            initiative.previous()

        self.update_widgets()

    # Add an actor to the initiative order
    @on(Button.Pressed, '#add-button')
    def action_add_actor(self) -> None:
        self.push_screen(AddActor(), callback=self.on_actor_added)

    def on_actor_added(self, new_actor: Actor | None):
        if new_actor is None:
            return

        initiative.add_actor(new_actor)

        table = self.query_one(DataTable)
        table.clear()
        for actor in initiative.actors:
            table.add_row(actor.init_roll, actor.name, actor.player_name, actor.hp, actor.ac)

        self.update_widgets()

    # Update information about an actor
    @on(Button.Pressed, '#edit-button')
    def edit_mode():
        pass

if __name__ == "__main__":
    fighter = Actor("Aragorn", 18, 30, 16, "Viggo")
    goblin = Actor("Gollum", 12, 7, 15, "DM")
    wizard = Actor("Gandalf", 5, 18, 12, "Ian")
    initiative = InitiativeList([fighter, goblin, wizard])
    app = InitiativeApp()
    app.run()
