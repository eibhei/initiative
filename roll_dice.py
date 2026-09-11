import random


def roll_dice(num_dice: int = 1, num_faces: int = 20, bonus: int = 0) -> tuple[list[int], int]:
    rolls = []
    for d in range(num_dice):
        rolls.append(random.randint(1, num_faces))
    return rolls, bonus
