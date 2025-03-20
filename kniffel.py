import random

total_score = 0
oberer_teil = 0

def calculate_total_score(score, category):
    global total_score, oberer_teil
    total_score += score
    if category in ["einser", "zweier", "dreier", "vierer", "fuenfer", "sechser"]:
        oberer_teil += score

def bonus():
    global total_score
    if oberer_teil >= 63:
        total_score += 35

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

def print_open_categories(categories):
    open_cats = [cat for cat, used in categories.items() if not used]
    print("Folgende Kategorien haben Sie noch offen:", ", ".join(open_cats))

def calculate_score(category, dice):
    counts = {i: dice.count(i) for i in range(1, 7)}
    if category in ["einser", "zweier", "dreier", "vierer", "fuenfer", "sechser"]:
        num = ["einser", "zweier", "dreier", "vierer", "fuenfer", "sechser"].index(category) + 1
        return num * counts.get(num, 0)
    elif category == "dreierpasch":
        return sum(dice) if any(count >= 3 for count in counts.values()) else 0
    elif category == "viererpasch":
        return sum(dice) if any(count >= 4 for count in counts.values()) else 0
    elif category == "fullhouse":
        return 25 if 2 in counts.values() and 3 in counts.values() else 0
    elif category == "kleinestrasse":
        if any(set([i, i+1, i+2, i+3]).issubset(set(dice)) for i in range(1, 4)):
            return 30
        return 0
    elif category == "grossestrasse":
        sorted_dice = sorted(set(dice))
        return 40 if len(sorted_dice) == 5 and max(sorted_dice) - min(sorted_dice) == 4 else 0
    elif category == "chance":
        return sum(dice)
    elif category == "kniffel":
        return 50 if any(count == 5 for count in counts.values()) else 0

def handle_reroll(dice):
    print("Welche Würfel möchten Sie neu würfeln? Geben Sie die Nummern der Würfel, die Sie neu würfeln möchten, getrennt durch ein Leerzeichen ein (1-5).")
    reroll_input = input().strip()
    indices = [int(i) - 1 for i in reroll_input.split() if i.isdigit() and 0 <= int(i) - 1 < 5]
    for idx in indices:
        dice[idx] = random.randint(1, 6)
    print_dice(dice)

def choose_category(categories, dice):
    while True:
        print("Geben Sie die gewünschte Kategorie ein. Wenn Sie wissen wollen, welche Kategorien noch frei sind, schreiben Sie 'Übersicht'.")
        eingabe = input().strip().lower()
        if eingabe in categories and not categories[eingabe]:
            score = calculate_score(eingabe, dice)
            print(f"Sie haben {score} Punkte in {eingabe} erzielt.")
            categories[eingabe] = True
            return score, eingabe
        elif eingabe == "übersicht":
            print_open_categories(categories)
        else:
            print("Ungültige Kategorie oder bereits verwendet.")

def player_turn(categories):
    dice = roll_dice()
    print_dice(dice)
    for roll in range(3):
        if roll < 2:
            while True:
                print("Wollen Sie Ihren Zug beenden? Wenn ja, geben Sie Ihre gewünschte Kategorie in Kleinbuchstaben ein. Wenn Sie eine Übersicht haben wollen, welche Kategorien noch frei sind, schreiben Sie 'Übersicht'. Wenn nicht, schreiben Sie 'würfel'.")
                eingabe = input().strip().lower()
                if eingabe == "übersicht":
                    print_open_categories(categories)
                elif eingabe == "würfel":
                    handle_reroll(dice)
                    break
                elif eingabe in categories and not categories[eingabe]:
                    score = calculate_score(eingabe, dice)
                    calculate_total_score(score, eingabe)
                    print(f"Sie haben {score} Punkte in {eingabe} erzielt.")
                    categories[eingabe] = True
                    return
                else:
                    print("Ungültige Eingabe oder Kategorie bereits verwendet")
        else:
            score, category = choose_category(categories, dice)
            calculate_total_score(score, category)

def main():
    categories = initialize_categories()
    while not all_categories_used(categories):
        player_turn(categories)
    bonus()
    print("Spiel beendet! Alle Kategorien sind ausgefüllt. Sie haben insgesamt", total_score, "Punkte erzielt.")

if __name__ == "__main__":
    main()