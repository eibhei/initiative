import unittest

from actor import Actor
from initiative import InitiativeList


class TestInitiativeList(unittest.TestCase):
    def setUp(self):
        self.fighter = Actor("Fighter", 18, 30, 16)
        self.goblin = Actor("Goblin", 12, 7, 15)
        self.wizard = Actor("Wizard", 5, 18, 12)

        # Deliberately out of order, to prove the sort works
        self.list = InitiativeList([self.wizard, self.fighter, self.goblin])

        # For adding later
        self.rogue = Actor("Rogue", 2, 22, 14)
        self.cleric = Actor("Cleric", 20, 29, 17)

    def test_sorted_on_init(self):
        self.assertIs(self.list.actors[0], self.fighter)

    def test_next(self):
        self.list.next()
        self.assertIs(self.list.actors[1], self.goblin)

    def test_next_at_end(self):
        self.list.current_turn_index = -1
        self.list.next()
        self.assertIs(self.list.actors[0], self.fighter)

    def test_previous(self):
        self.list.next()
        self.list.next()
        self.list.previous()
        self.assertIs(self.list.actors[1], self.goblin)

    def test_previous_at_start(self):
        self.list.previous()
        self.assertIs(self.list.actors[-1], self.wizard)

    def test_add_at_end(self):
        self.list.add_actor(self.rogue)
        self.assertIs(self.list.actors[-1], self.rogue)

    def test_add_at_start(self):
        self.list.add_actor(self.cleric)
        self.assertIs(self.list.actors[0], self.cleric)

    def test_remove(self):
        self.list.remove_actor(self.goblin)
        self.assertIs(self.list.actors[1], self.wizard)

    def test_remove_current_actor(self):
        self.list.next()
        self.list.remove_actor(self.goblin)
        self.assertIs(self.list.actors[1], self.wizard)

if __name__ == "__main__":
    unittest.main()
