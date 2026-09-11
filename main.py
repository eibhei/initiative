#! /usr/bin/env python3
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

    name = "Aragorn"
    player_name = "Viggo"
    init_roll = 15
    hp = 30
    ac = 15

    initiative_order.append(Player(name, player_name, init_roll, hp, ac))


    name = "Frodo"
    player_name = "Elijah"
    init_roll = 18
    hp = 30
    ac = 15

    initiative_order.append(Player(name, player_name, init_roll, hp, ac))

    sorted_initiative = sorted(initiative_order, key=lambda x: x.init_roll, reverse=True)

    print(f"The order of initiative is as follows:")
    for a in sorted_initiative:
        print(f"{a.name} ({a.init_roll})")


if __name__ == "__main__":
    main()
