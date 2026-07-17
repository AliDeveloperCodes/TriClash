# TriClash 🪨📄✂️

Ein einfaches, unterhaltsames **Schere-Stein-Papier**-Spiel für die Kommandozeile, geschrieben in Python. Wähle deinen Zug, fordere den Computer heraus und finde heraus, wer gewinnt!

> In anderen Sprachen lesen: [English](README.en.md) · [فارسی](README.fa.md)

## Funktionen

- Übersichtliche, minimalistische Kommandozeilen-Oberfläche
- Spiel gegen einen zufällig agierenden Computergegner
- Eingabevalidierung (stürzt bei ungültigen Eingaben nicht ab)
- Automatische Wiederholung bei einem Unentschieden
- Möglichkeit, nach jeder Runde erneut zu spielen

## Funktionsweise

1. Ein nummeriertes Menü wird angezeigt: `1. Rock` (Stein), `2. Paper` (Papier), `3. Scissors` (Schere)
2. Gib die Nummer deiner Wahl ein
3. Der Computer wählt zufällig
4. Der Gewinner wird nach den klassischen Regeln von Schere-Stein-Papier ermittelt
5. Bei einem Unentschieden startet die Runde automatisch neu
6. Nach einem Sieg oder einer Niederlage wirst du gefragt, ob du erneut spielen möchtest

## Voraussetzungen

- Python 3.x (keine externen Abhängigkeiten)

## Installation & Nutzung

Repository klonen:

```bash
git clone https://github.com/<your-username>/TriClash.git
cd TriClash
```

Spiel starten:

```bash
python game.py
```

### Windows

Alternativ kannst du auch einfach `run.bat` doppelklicken, um das Spiel zu starten.

## Projektstruktur

```
TriClash/
├── game.py       # Haupt-Spiellogik
├── run.bat       # Startskript für Windows
├── README.md     # Sprachauswahl
├── README.en.md  # Englische Dokumentation
├── README.de.md  # Deutsche Dokumentation
├── README.fa.md  # Persische Dokumentation
└── LICENSE       # MIT-Lizenz
```

## Mitwirken

Beiträge, Fehlermeldungen und Feature-Wünsche sind herzlich willkommen! Schau gerne auf der [Issues-Seite](../../issues) vorbei oder erstelle einen Pull Request.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz — Details findest du in der Datei [LICENSE](LICENSE).
