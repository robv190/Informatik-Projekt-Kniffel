import random

def calculate_total_score(score):
    global total_score
    total_score += score
    return total_score

def roll_dice(num_dice=5):
    return [random.randint(1, 6) for _ in range(num_dice)]

def print_dice(dice):
    print("Sie haben gewürfelt: ", *dice)


def initialize_categories():
    return {
        "einser": False,
        "zweier": False,
        "dreier": False,
        "vierer": False,
        "fuenfer": False,
        "sechser": False,
        "dreierpasch": False,
        "viererpasch": False,
        "fullhouse": False,
        "kleinestrasse": False,
        "grossestrasse": False,
        "chance": False,
        "kniffel": False
    }

def all_categories_used(categories):
    return all(categories.values())

def main():
    categories = initialize_categories()
    while not all_categories_used(categories):
        player_turn(categories)
    print("Spiel beendet! Alle Kategorien sind ausgefüllt.Sie haben insgesamt", total_score, "Punkte erzielt.")

if __name__ == "__main__":
    main()