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
        