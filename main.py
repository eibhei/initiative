#! /usr/bin/env python3
from player import Player
from roll_dice import roll_dice


def main():
    initiative_order = []
    name = input("Character name: ")
    player_name = input("Player name: ")
    init_roll = int(input("Initiative roll: "))
    hp = int(input("Hit points: "))
    ac = int(input("Armour class: "))

    initiative_order.append(Player(name, player_name, init_roll, hp, ac))

    name = "Alfred"
    player_name = "Molly"
    init_roll = 16
    hp = 30
    ac = 15

    initiative_order.append(Player(name, player_name, init_roll, hp, ac))

    print(initiative_order[0].name, initiative_order[1].name)

    # def __init__(self, name, player_name, init_roll, hp, ac):


if __name__ == "__main__":
    main()
