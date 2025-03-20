# Header: Dieses Programm implementiert ein einfaches Kniffel-Spiel für einen einzelnen Spieler.
# Der Spieler würfelt in jedem Zug bis zu drei Mal mit fünf Würfeln und wählt anschließend eine Kategorie aus,
# um Punkte zu sammeln. Das Spiel endet, wenn alle verfügbaren Kategorien verwendet wurden.
# Der Gesamtscore wird am Ende ausgegeben, inklusive eines möglichen Bonus für den oberen Teil.

# Import: Das Modul 'random' wird verwendet, um Zufallszahlen für die Würfelwürfe zu generieren.
import random

# Globale Variablen zur Verfolgung des Spielstands
total_score = 0  # Gesamtpunkte des Spielers
oberer_teil = 0  # Summe der Punkte im oberen Teil (Einser bis Sechser)

dice_faces = { 1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"} #Bilder für die Würfel

def calculate_total_score(score): #Funktion um die Gesamtpunkte zu berechnen
    global total_score
    total_score += score
    return total_score

def bonus(): #Funktion um den Bonus zu berechnen
    global oberer_teil
    global total_score 
    if oberer_teil >= 63:
        total_score += 35

def roll_dice(num_dice=5): #Funktion um die Würfel zu würfeln
    return [random.randint(1, 6) for _ in range(num_dice)]

def print_dice(dice): #Funktion um die Würfel auszugeben
    print("Sie haben gewürfelt: ", *dice)
    print(" ".join(dice_faces[die] for die in dice))


def initialize_categories(): #Funktion um die Kategorien am Start des Spiels zu initialisieren
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

def all_categories_used(categories): #Funktion um zu überprüfen ob alle Kategorien verwendet wurden
    return all(categories.values())

def print_image_dice(dice): #Funktion um die Würfel als Bilder auszugeben
    print(" ".join(dice_faces[die] for die in dice))

def handle_reroll(dice): #Funktion um die Würfel neu zu würfeln
    print("Welche Würfel möchten sie neu würfeln? Geben sie die Nummern der Würfel, die sie neu würfeln möchten, getrennt durch ein Leerzeichen ein (1-5).")
    reroll_input = input().strip()
    indices = [int(i) - 1 for i in reroll_input.split() if i.isdigit() and 0 <= int(i) - 1 < 5]
    for idx in indices:
        dice[idx] = random.randint(1,6)
    print_dice(dice)

def choose_category(categories, dice): #Funktion um die Kategorie auszuwählen
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

def player_turn(categories): #Funktion um den Zug des Spielers zu verwalten
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
                    break #verlässt die while-schleife
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
            
def print_open_categories(categories): #Funktion um die noch offenen Kategorien auszugeben
  open_cats = [cat for cat, used in categories.items() if not used]
  print("folgende Kategorien haben Sie noch offen:",",".join(open_cats)) 

def calculate_score(category,dice): #Funktion um die Punkte zu berechnen
  global oberer_teil
  counts = {i: dice.count(i) for i in range (1, 7)}
  if category in ["einser","zweier","dreier","vierer","fuenfer","sechser"]:
    num = ["einser","zweier","dreier","vierer","fuenfer","sechser"].index(category) + 1
    oberer_teil += num * counts.get(num, 0)
    return num * counts.get(num, 0)
  
  elif category == "dreierpasch":
    return sum(dice) if any(count >= 3 for count in counts.values()) else 0
  elif category == "viererpasch":
    return sum(dice) if any(count >= 4 for count in counts.values()) else 0
  elif category == "fullhouse":
    return 25 if 2 in counts.values() and 3 in counts.values() else 0
  elif category == "kleinestrasse":
    sorted_dice = sorted(sorted(dice))
    if len(sorted_dice) >= 4 and (
      max(sorted_dice) - min(sorted_dice) == 3 or 
      set(sorted_dice) in [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]):
      return 30
    else: return 0
  elif category == "grossestrasse":
    sorted_dice = sorted(set(dice))
    return 40 if len(sorted_dice) == 5 and max(sorted_dice) - min(sorted_dice) == 4 else 0
  elif category == "chance":
    return sum(dice)
  elif category == "kniffel":
    return 50 if any(count == 5 for count in counts.values()) else 0
  return 0


def main(): #Funktion um das Spiel zu starten
    global total_score
    categories = initialize_categories()
    while not all_categories_used(categories):
        player_turn(categories)
    print("Spiel beendet! Alle Kategorien sind ausgefüllt.Sie haben insgesamt", total_score, "Punkte erzielt.")

if __name__ == "__main__": #Funktion um das eigentliche Programm zu starten
    main()
  
