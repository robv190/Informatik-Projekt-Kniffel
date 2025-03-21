# Autoren : Hüseyin Sahin, Tom Holst, Paulo Ramos Weik, Robin Vogt, Nick Daub
# Datum : 21.03.2025

# Import: Das Modul "random" wird verwendet, um Zufallszahlen für die Würfelwürfe zu generieren.
import random

# Globale Variablen zur Verfolgung des Spielstands
total_score = 0  #  Gesamtpunkte des Spielers
oberer_teil = 0  #  Summe der Punkte im oberen Teil (Einser bis Sechser)

#######################################################################################################
# calculate_total_score berechnet die Gesamtpunkte
# bonus überprüft ob ein Bonus ensteht und addiert ihn auf die Gesamtpunkte
# calculate_score berechnet die Punkte für die einzelnen Kategorien


def calculate_total_score(score): 
    global total_score
    total_score += score
    return total_score

def bonus(): 
    global oberer_teil
    global total_score 
    if oberer_teil >= 63:
        total_score += 35
        print("Sie haben den Bonus erreicht!")

def calculate_score(category,dice): 
  global oberer_teil
  counts = {i: dice.count(i) for i in range (1, 7)}                                                   # Zählt die Anzahl der Würfel mit den Zahlen 1-6
  if category in ["einser","zweier","dreier","vierer","fuenfer","sechser"]:                           # Überprüft ob die Kategorie in der Liste ist
    num = ["einser","zweier","dreier","vierer","fuenfer","sechser"].index(category) + 1
    oberer_teil += num * counts.get(num, 0)                                                           # Addiert die Punkte zum oberen Teil (relevant für den Bonus) 
    return num * counts.get(num, 0)                                                                   # Gibt die Punkte für die Kategorie zurück                
  elif category == "dreierpasch":
    return sum(dice) if any(count >= 3 for count in counts.values()) else 0                           # Gibt die Summe der Würfel zurück wenn mindestens 3 Würfel die gleiche Zahl haben (Dreierpasch), sonst 0
  elif category == "viererpasch":
    return sum(dice) if any(count >= 4 for count in counts.values()) else 0                           # Gibt die Summe der Würfel zurück wenn mindestens 4 Würfel die gleiche Zahl haben (Viererpasch), sonst 0
  elif category == "fullhouse":
    return 25 if 2 in counts.values() and 3 in counts.values() else 0                                 # Gibt 25 Punkte zurück wenn 2 und 3 gleiche Würfel existieren, sonst 0
  elif category == "kleinestrasse":
    sorted_dice = sorted(sorted(dice))                                                                # Sortiert die Würfel und entfernt doppelte Würfel
    if len(sorted_dice) >= 4 and (                                                                    # Überprüft ob die Anzahl der Würfel ohne der Duplikate mindestens 4 ist 
      max(sorted_dice) - min(sorted_dice) == 3 or                                                     # Überprüft ob die Differenz zwischen dem höchsten und niedrigsten Würfel 3 ist --> Kleine Straße
      max(sorted_dice) - min(sorted_dice) == 4 or                                                     # Überprüft ob die Differenz zwischen dem höchsten und niedrigsten Würfel 4 ist --> Große Straße ist auch eine kleine Straße                                                  
      set(sorted_dice) in [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]):                                # Überprüft ob die Würfel die Zahlen 1-4, 2-5 oder 3-6 enthalten --> Fehlerabsicherung
      return 30                                                                                       # Gibt 30 Punkte zurück wenn die Bedingungen erfüllt sind, sonst 0
    else: return 0
  elif category == "grossestrasse":
    sorted_dice = sorted(set(dice))                                                                   # Sortiert die Würfel 
    return 40 if len(sorted_dice) == 5 and max(sorted_dice) - min(sorted_dice) == 4 else 0            # Gibt 40 Punkte zurück wenn die Anzahl der Würfel 5 ist und die Differenz zwischen dem höchsten und niedrigsten Würfel 4 ist (Große Straße), sonst 0
  elif category == "chance":
    return sum(dice)                                                                                  # Gibt die Summe der Würfel zurück                       
  elif category == "kniffel":
    return 50 if any(count == 5 for count in counts.values()) else 0                                  # Gibt 50 Punkte zurück wenn mindestens 5 Würfel die gleiche Zahl haben (Kniffel), sonst 0
  return 0

#######################################################################################################
# Die Funktionen roll_dice, print_dice, print_image_dice und handle_reroll sind Funktionen um die Würfel zu würfeln und auszugeben

dice_faces = { 1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}                                      # Bilder für die Würfel

def roll_dice(num_dice=5): 
    return [random.randint(1, 6) for _ in range(num_dice)]

def print_dice(dice): 
    print("Sie haben gewürfelt: ", *dice)
    print_image_dice(dice)

def print_image_dice(dice): 
    print(" ".join(dice_faces[die] for die in dice))

def handle_reroll(dice): 
    print("Welche Würfel möchten sie neu würfeln? Geben sie die Nummern der Würfel, die sie neu würfeln möchten, getrennt durch ein Leerzeichen ein (1-5).")
    reroll_input = input().strip()                                                                    # Entfernt Leerzeichen 
    indices = [int(i) - 1 for i in reroll_input.split() if i.isdigit() and 0 <= int(i) - 1 < 5]       # Konvertiert die Eingabe in eine Liste von Indizes
    for idx in indices:                                                                               # Würfelt die ausgewählten Würfel neu
        dice[idx] = random.randint(1,6)
    print_dice(dice)

#######################################################################################################
# initialize_categories initialisiert die Kategorien
# all_categories_used überprüft ob alle Kategorien verwendet wurden
# choose_category lässt den Spieler eine Kategorie auswählen 
# print_open_categories gibt die noch offenen Kategorien aus

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

def choose_category(categories, dice): 
    while True:
        print("Geben sie die gewünschte Kategorie ein, wenn sie wissen wollen welche Kategorien noch frei sind, schreiben sie 'Übersicht'.")
        eingabe = input().strip().lower()                                                             # Konvertiert die Eingabe in Kleinbuchstaben und entfernt Leerzeichen
        if eingabe in categories and not categories[eingabe]:
            score = calculate_score(eingabe, dice)
            print(f"Sie haben {score} Punkte in {eingabe} erziehlt.")
            categories[eingabe] = True
            return
        elif eingabe == "übersicht":
            print_open_categories(categories)
        else:
            print("Ungültige Kategorie oder bereits verwendet.")

def print_open_categories(categories): 
  open_cats = [cat for cat, used in categories.items() if not used]                                   # Erstellt eine Liste von Kategorien die noch offen sind
  print("folgende Kategorien haben Sie noch offen:",",".join(open_cats),", der obere Teil hat folgende Punktzahl: ",oberer_teil) 

#######################################################################################################
# player_turn verwaltet den Spielzug des Spielers

def player_turn(categories): 
    dice = roll_dice()
    print_dice(dice)
    for roll in range(3):
        if roll <2:
            while True:
                print("Wollen sie ihren Zug beenden? Wenn ja, geben sie ihre gewünschte Kategorie in Kleinbuchstaben ein. Wenn sie eine Übersicht haben wollen welche Kategorien noch frei sind, schreiben sie 'übersicht'. Wenn nicht schreiben sie 'würfel'.")
                eingabe = input().strip().lower()                                                       # Konvertiert die Eingabe in Kleinbuchstaben und entfernt Leerzeichen
                if eingabe == "übersicht":
                    print_open_categories(categories)
                elif eingabe == "würfel":
                    handle_reroll(dice)
                    break 
                elif eingabe in categories and not categories[eingabe]:
                    score = calculate_score(eingabe, dice)
                    calculate_total_score(score)
                    print(f"Sie haben {score} Punkte in {eingabe} erzielt.")
                    categories[eingabe] = True
                    return
                else: 
                    print("Ungültige Eingabe oder Kategorie bereits verwendet")
    else:
            choose_category(categories, dice)

#######################################################################################################
# main ist die Hauptfunktion des Programms

def main(): 
    global total_score
    categories = initialize_categories()
    while not all_categories_used(categories):
        player_turn(categories)
    print("Spiel beendet! Alle Kategorien sind ausgefüllt.Sie haben insgesamt", total_score, "Punkte erzielt.")

if __name__ == "__main__": 
    main()
  
