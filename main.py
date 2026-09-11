#! /usr/bin/env python3
from roll_dice import roll_dice

def main():
    roll, bonus = roll_dice(3,6,5)
    print(f"{" + ".join(str(n) for n in roll)} = {sum(roll)}")

if __name__ == "__main__":
    main()
