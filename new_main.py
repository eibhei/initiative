#!/usr/bin/env python3
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
    ansi_color = True
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
                    Static("Round #", id="round_number"),
                    ProgressBar(total=100, show_eta=False, show_percentage=False, id="progressbar"),
                    id="roundinfo"
                ),
                Static("Character name,\nand player", id="current_actor"),
                Static("Character status", id="conditions"),
                id="top"
            ),
            Container(
                # Need to figure out how to put in a content switcher
                DataTable(id="initiative-table"),
                id="middle"
            ),
            Horizontal(
                Button("Add", classes="buttons"),
                Button("Edit", classes="buttons"),
                Container(id="gap"),
                Button("Prev", classes="buttons"),
                Button("Next", classes="buttons"),
                id="bottom"
            ),
        )
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*HEADINGS)

if __name__ == "__main__":
    initiative = InitiativeList([])
    app = InitiativeApp()
    app.run()
