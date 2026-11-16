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
)
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


class InitiativeApp(App):
    """A Textual app to manage initiative."""
    # ansi_color = True
    CSS_PATH = "new_app.tcss"
    ENABLE_COMMAND_PALETTE = False
    TITLE = "Initiative Tracker"

    BINDINGS = [
        ("n", "next_actor", "Next"),
        ("a", "add_actor", "Add"),
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

    @on(Button.Pressed, '#next-button')
    def next_turn(self):
        # Move up the turn order
        initiative.next()

        # Grab the necessary information
        round_number = initiative.get_current_round()
        current_turn = initiative.get_current_turn()
        current_actor = initiative.actors[current_turn]

        # Update the round number
        round_number_display = self.query_one("#round_number")
        round_number_display.update(content=f'Round {round_number}')

        # Update the current actor
        current_actor_display = self.query_one("#current_actor")
        current_actor_display.update(content=f'{current_actor.name}\n{current_actor.player_name}')

        # Update the progress bar
        round_progress = initiative.current_turn_index + 1
        progress_bar_display = self.query_one('#progress_bar')
        progress_bar_display.advance(round_progress)

    @on(Button.Pressed, '#prev-button')
    def prev_turn(self):
        # Move up the turn order
        initiative.previous()

        # Grab the necessary information
        round_number = initiative.get_current_round()
        current_turn = initiative.get_current_turn()
        current_actor = initiative.actors[current_turn]

        # Update the round number
        round_number_display = self.query_one("#round_number")
        round_number_display.update(content=f'Round {round_number}')

        # Update the current actor
        current_actor_display = self.query_one("#current_actor")
        current_actor_display.update(content=f'{current_actor.name}\n{current_actor.player_name}')

        # Update the progress bar
        round_progress = initiative.current_turn_index + 1
        progress_bar_display = self.query_one('#progress_bar')
        progress_bar_display.update(progress=round_progress)

if __name__ == "__main__":
    fighter = Actor("Aragorn", 18, 30, 16, "Viggo")
    goblin = Actor("Gollum", 12, 7, 15, "DM")
    wizard = Actor("Gandalf", 5, 18, 12, "Ian")
    initiative = InitiativeList([fighter, goblin, wizard])
    app = InitiativeApp()
    app.run()
