import random


def roll_dice(num_dice: int = 1, num_faces: int = 20, bonus: int = 0) -> tuple[list[int], int]:
    rolls = []
    for d in range(num_dice):
        rolls.append(random.randint(1, num_faces))
    return rolls, bonus

    # Use the following to get the resultant rolls and sum
    # result = roll_dice(3,6)
    # print(f"{" + ".join(str(r) for r in result)} = {sum(result)}")

# def roll_dice_with_bonus(num_dice: int = 1, num_faces: int = 20) -> tuple[list[int], int]:
#     rolls = roll_dice(num_dice, num_faces)
#     result = sum(rolls) + bonus

#     return rolls, result

#     # Use the following to get the resultant rolls and sum
#     # rolls, result, bonus = roll_dice_with_bonus(2,3,6)
#     # print(f"{" + ".join(str(r) for r in rolls)} ++ {bonus} = {sum(result)}")
