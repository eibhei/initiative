# See https://roll20.net/compendium/dnd5e/Conditions for all the information we need
# Determine the ideal way to store the condition name and effects, especially when there are multiple
# This is probably the place to add death saves



class Condition:
    def __init__(self, name: str, glyph: str) -> None:
        self.name = name
        self.glyph = glyph
