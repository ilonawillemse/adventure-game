# Adventure.py 🗺️

[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/downloads/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Adventure.py** is een interactieve, tekstgebaseerde avonturengame geschreven in Python. Spelers verkennen kamers, verzamelen items en lossen puzzels op om verder te komen. Het project demonstreert objectgeoriënteerd programmeren, dynamische data loading en interactieve command handling.

---

## Over dit project

Dit project is in **2022 ontwikkeld** als onderdeel van de **Minor Programmeren** aan de **Universiteit van Amsterdam**.  
Het spel `Adventure.py` is gemaakt als opdracht om **objectgeoriënteerd programmeren, datastructuren en interactieve command handling** te oefenen.

---

## Doelen van het spel
- **Verkennen van kamers:** Beweeg met commando's zoals `NORTH`, `EAST`, `IN`, en `OUT`.
- **Items verzamelen:** Gebruik `TAKE` om items op te pakken en `DROP` om ze neer te leggen.
- **Probleemoplossing:** Verzamel de juiste items om toegang te krijgen tot bepaalde kamers.
- **Interactie en feedback:** Gebruik `LOOK`, `INVENTORY` en `HELP` om de omgeving en je inventaris te bekijken.

---

## Technische aspecten
- Objectgeoriënteerd ontwerp met kamers en items als objecten.
- Dynamische room graph loading via `.dat` bestanden.
- Synoniemen en commando-afhandeling voor vloeiende gebruikerservaring.
- Robuuste foutafhandeling voor ontbrekende of onjuiste input.

---

## Installatie en gebruik
1. Zorg dat [Python 3](https://www.python.org/downloads/) is geïnstalleerd.
2. Clone of download dit project:
   ```bash
   git clone https://github.com/ilonawillemse/adventure.git
   ```

3. Navigeer naar de projectmap:
   ```bash
   cd adventure
   ```

4. (Optioneel) Maak en activeer een virtual environment:
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Mac/Linux
   source venv/bin/activate
   ```

5. Installeer dependencies (geen extra packages nodig voor dit project):
   ```bash
   pip install -r requirements.txt
   ```

6. Run het spel:
   ```bash
   python adventure.py
   ```
---

Optioneel kun je een specifieke game laden:
   ```bash
   python adventure.py Tiny
   ```

   Commando's
   | Commando                     | Beschrijving                               |
   |-------------------------------|-------------------------------------------|
   | NORTH/SOUTH/EAST/WEST/IN/OUT | Beweeg tussen kamers                       |
   | TAKE <item>                   | Pak een item op                            |
   | DROP <item>                   | Leg een item neer                          |
   | LOOK                          | Toon lange omschrijving van kamer en items|
   | INVENTORY                     | Toon items in je hand                      |
   | HELP                          | Toon beschikbare commando’s                |
   | QUIT                          | Stop het spel                              |

## Voorbeeld gameplay
   ```text
   > LOOK
   You are in a dimly lit room. There is a KEY on the floor.

   > TAKE KEY
   KEY taken

   > INVENTORY
   KEY

   > EAST
   You enter a bright hallway. There is a MAP on a table.

   > TAKE MAP
   MAP taken
```

## Projectstructuur
   ``` text
   adventure.py           # Hoofdscript dat het spel runt
   loader.py              # Module voor het inladen van kamers en synoniemen
   room.py                # Klasse voor kamers (optioneel, afhankelijk van loader)
   item.py                # Klasse voor items (optioneel, afhankelijk van loader)
   data/                  # Map met game data bestanden
   │   └─ TinyAdv.dat     # Voorbeeldspeldata
   README.md              # Dit bestand, met uitleg en instructies
   LICENSE                # Licentie (bijv. MIT)
   images/                # Optioneel: screenshots of GIF van het spel
   .gitignore             # Git negeer regels
   requirements.txt       # Lijst met Python dependencies (in dit geval leeg)
   ```

## Minimale bestanden om het spel te runnen:
   adventure.py

   loader.py

   data/<game_name>Adv.dat

   room.py en item.py (indien niet geïntegreerd in loader.py)

## Licentie

   MIT License

## Auteur

   Ilona Willemse – Universiteit van Amsterdam
