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
    
def player_turn(categories):
    dice = roll_dice()
    print_dice(dice)
    for roll in range(3): # Zählt Würfe mit
        if roll < 2: # gibt Möglichkeit zu wählen ob man neu würfeln oder den zug beenden will
            while True:
                print("Wollen sie ihren Zug beenden? Wenn ja, geben sie ihre gewünschte Kategorie ein. Wenn sie eine Übersicht über ihre offenen Kategorien haben wollen, schreiben sie 'übersicht'. Wenn sie nochmal wüfeln möchten, schreiben sie 'würfel'")
                eingabe = input().strip().lower() # entfernt außenstehende leerzeichen und formiert die eingabe in kleinbuchstaben
                if eingabe == "übersicht":
                    print_open_categories(categories)
                elif eingabe == "würfel":
                    handle_reroll(dice)
                    break #verlässt die while-schleife
                elif eingabe in categories and not categories[eingabe]:
                    score = calculate_score(eingabe, dice)
                    calculate_total_score(score)
                    print(f"Sie haben {score} Punkte in {eingabe} erzielt.")
                    categories[eingabe] = True
                    return
                else: 
                    print("Ungültige Eingabe oder Kategorie bereits verwendet")
        else: # nach drittem wurf wird eingabe einer kategorie erzwungen
            choose_category(categories, dice)
        