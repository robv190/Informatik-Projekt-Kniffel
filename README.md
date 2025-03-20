# Informatik-Projekt-Kniffel

Ersteller : Robin Vogt, Nick Daub, Tom Holst, Paulo Ramos Weik, Hüseyin Sahin
***

## Inhaltsverzeichnis
### 1. Einleitung
### 2. Features
### 3. Installation
### 4. Technologien
### 5. Erklärung des Spiels
### 6. Spielanleitung
### 7. Offizielle Spielregeln


## Einleitung
Dieses Projekt ist eine digitale Umsetzung des Würfelspiels Kniffel (auch bekannt als Yahtzee). 
Das Spiel kann alleine oder mit mehreren Spielern gespielt werden und bietet eine interaktive Benutzeroberfläche.


## Features
- Spieleranzahl wählbar
- Zufallsbasierte Würflewürfe
- Punkteberechnung nach offiziellen Kniffel-Regeln
- Möglichkeit, Würfe strategisch zu behalten oder erneut zu würfeln


## Technologien

### Programmiersprache
- Python

### Bibliotheken
- tkinter
- random


## Erklärung des Spiels
Kniffel ist ein beliebtes Würfelspiel, bei dem es darum geht, in 13 Runden möglichst viele Punkte zu sammeln.
Jeder Spieler hat pro Runde bis zu drei Würfe, um eine optimale Kombination zu erreichen.

Die gewürfelten Werte werden in einer Wertungstabelle eingetragen, entweder in den **oberen Block** (wo die Summe von gleichen Zahlen gezählt wird)
oder in den **unteren Block** (mit speziellen Kombinationen wie z.B. "Full House" oder "Große Straße").

Das Ziel ist es, strategisch zu entscheiden, wann welche Kategorien genutzt werden und ob man riskiert, noch einmal zu würfeln oder sich mit dem aktuellen Wurf zufrieden gibt.
Ein Kniffel (5 gleiche Würfel) bringt die meisten Punkte und kann im Laufe des Spiels Bonuspunkte einbringen.
Am Ende gewinnt der Spieler mit der höchsten Gesamtpunktzahl.



## Spielanleitung
1. Starten Sie das Programm
2. Wählen Sie die Anzahl der Spieler
3. Würfen Sie bis zu drei Mal pro Runde und entscheiden Sie, welche Würfeln Sie behalten möchten
4. Wählen Sie eine Kategorie für den Wurf (z.B. Dreierpasch, Große Straße, etc.)
5. Das Spiel endet nach 13 Runden und der Spieler mit der höchsten Punktzahl gewinnt


## Offizielle Spielregeln

### 1. Spielmaterial
- 5 sechseitige Würfel
- 1 Kniffelwertungstabelle

### 2. Spielablauf
- Jeder Spieler hat 13 Runden
- Pro Runde darf ein Spieler bis zu drei Mal würfeln
- Nach jedem Wurf kann der Spieler beliebige Würfel zurücklegen und mit den restlichen neu würfeln
- Nach den drei Würfen muss der Spieler eine Punktekästchen in der Wertungstabelle ausfüllen

### 3. Wertungstabelle 
- Jeder Spieler muss jede Kategorie genau einmal ausfüllen
- Falls keine passende Kategorie gewählt werden kann, muss eine mit 0 Punkten gestrichen werden

| Kategorie           | Punktevergabe |
|---------------------|--------------|
| **Oberer Block**    |              |
| Einser             | Summe aller Einser |
| Zweier             | Summe aller Zweier |
| Dreier             | Summe aller Dreier |
| Vierer             | Summe aller Vierer |
| Fünfer             | Summe aller Fünfer |
| Sechser            | Summe aller Sechser |
| **Bonus (35 Punkte)** | Wenn Summe oben ≥ 63 |
| **Unterer Block**  |              |
| Dreierpasch       | Summe aller Würfel (mind. 3 gleiche) |
| Viererpasch       | Summe aller Würfel (mind. 4 gleiche) |
| Full House        | **25 Punkte** (Drilling + Paar) |
| Kleine Straße     | **30 Punkte** (z. B. 1-2-3-4) |
| Große Straße      | **40 Punkte** (z. B. 2-3-4-5-6) |
| Kniffel           | **50 Punkte** (5 gleiche Würfel) |
| Chance           | Summe aller Würfel |
