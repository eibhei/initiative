# initiative.py
A terminal-based initiative tracker for Dungeons and Dragons

## Project Scope
Be able to track an arbitrary number of players and enemies in initiative order, roll for initiative, track health, AC, and any other applied conditions.

## Project Plan
- [x] Write basic logic for holding player/enemy information and order
- [x] Set up dice rolls for initiative calculation in-app
- [ ] Make combat conditions do things
  - https://roll20.net/compendium/dnd5e/Conditions#content
- [ ] Track death saves
- [ ] Add bonus hit points if need be
- [ ] Add optional notes for each actor

### Bonus features
- [ ] Save and restore sessions

### To-do
- [ ] Move through the turn order with 'n'
  - See https://textual.textualize.io/widgets/data_table/
  - Probably worth having some way to undo or travel back in case of accidental keypresses
- [ ] Add a round tracker in header
  - See https://textual.textualize.io/widgets/header/
- [ ] Create a new line in the table from AddActor()
  - See https://textual.textualize.io/guide/screens/#returning-data-from-screens
- [ ] Style the table, highlight the current player
