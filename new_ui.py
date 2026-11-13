from textual.app import App, ComposeResult
from textual.containers import (
    Container,
    Horizontal,
    HorizontalGroup,
    Vertical,
    VerticalGroup,
)
from textual.widgets import Footer, Header, Placeholder


class PlaceholderApp(App):
    CSS_PATH = "new_ui.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Container(
                VerticalGroup(
                    Placeholder("Round #", id="round_number"),
                    Placeholder("Round Progress Bar", id="progress_bar"),
                    id="roundinfo"
                ),
                Placeholder("Current Actor", id="current_actor"),
                Placeholder("Conditions", id="conditions"),
                id="top"
            ),
            Container(
                Placeholder("DataTable", id="table"), # This will be a ContentSwitcher widget to make room for other interactive widgets
                id="middle"
            ),
            Horizontal(
                Placeholder("Add button", classes="buttons"),
                Placeholder("Edit button", classes="buttons"),
                Placeholder("Gap", id="gap"),
                Placeholder("Prev button", classes="buttons"),
                Placeholder("Next button", classes="buttons"),
                id="bottom"
            ),
        )
        yield Footer()


if __name__ == "__main__":
    app = PlaceholderApp()
    app.run()
