def handle_reroll(dice):
    print("Welche Würfel möchten sie neu würfeln? Geben sie die Nummern der Würfel, die sie neu würfeln möchten, getrennt durch ein Leerzeichen ein (1-5).")
    reroll_input = input().strip()
    indices = [int(i) - 1 for i in reroll_input.split() if i.isdigit() and 0 <= int(i) - 1 < 5]
    for idx in indices:
        dice[idx] = random.randint(1,6)
        print_dice(dice)

def choose_category(categoreis, dice):
    while True:
        print("Geben sie die gewünschte Kategorie ein, wenn sie wissen wollen welche Kategorien noch frei sind, schreiben sie 'Übersicht'.")
        eingabe = input().strip().lower()
        if eingabe in categories and not categories[eingabe]:
            score = calculate_score(eingabe, dice)
            print(f"Sie haben {score} Punkte in {eingabe} erziehlt.")
            categories[eingabe] = True
            return
        elif eingabe == "übersicht":
            print_open_categories(categories)
        else:
            print("Ungültige Kategorie oder bereits verwendet.")

def player_turn(categories):
    dice = roll_dice()
    print_dice(dice)
    for roll in range(3):
        if roll <2:
            while True:
                print("Wollen sie ihren Zug beenden? Wenn ja, geben sie ihre gewünschte Kategorie in Kleinbuchstaben ein. Wenn sie eine Übersicht haben wollen welche Kategorien noch frei sind, schreiben sie 'übersicht'. Wenn nicht schreiben sie 'würfel'.")
                eingabe = input().strip().lower()
                if eingabe == "übersicht":
                    print_open_categories(categories)
                elif eingabe == "würfel":
                    handle_reroll(dice)
                    break
                elif eingabe in categories and not categories[eingabe]:
                    score = calculate_score(eingabe, dice)
                    calculate_total_score(score)
                    print(f"Sie haben {score} Punkte in {eingabe} erziehlt.")
                    categories[eingabe] = True
                    return
                else:
                    print("Ungültige Eingabe oder Kategorie bereits verwendet.")
        else:
            choose_category(categories, dice)