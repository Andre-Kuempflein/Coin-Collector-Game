# Coin-Collector-Game
Ein 2D-Top-Down-Spiel, entwickelt mit Python, Pygame, Pydantic und Typer. Das Ziel des Spiels ist es, alle Münzen in einem Level zu sammeln, während man Hindernissen ausweicht.

Funktionen
Dynamische Level: Level werden aus JSON-Dateien geladen.

Datenvalidierung: Strikte Validierung der Level-Dateien durch Pydantic.

CLI-Schnittstelle: Komfortable Steuerung über die Kommandozeile mit Typer.

Kollisionserkennung: Präzise Rechteck-Rechteck-Kollision zwischen Spieler und Wänden.

Mehrere Level: Automatischer Wechsel zum nächsten Level, sobald alle Münzen gesammelt wurden.

Debug-Modus: Optionale Anzeige von Kollisionsboxen zur Fehlersuche.

# Voraussetzungen
Stelle sicher, dass du folgende Software installiert hast:

Python 3.11 oder neuer

uv (ein extrem schneller Python-Paket- und Projektmanager)

# Installation
Klone das Repository oder lade es herunter.

Navigiere im Terminal in das Hauptverzeichnis des Projekts:

Bash

cd coin_collector_projekt
Installiere alle Abhängigkeiten automatisch mit uv:

Bash

uv sync

 # Starten des Spiels
Um das Spiel zu starten, verwende den folgenden Befehl im Hauptverzeichnis:

PowerShell

In der PowerShell (Windows) den Pfad setzen

$env:PYTHONPATH = "src"

Das Spiel starten

uv run -m coin_collector start --level-dir src/coin_collector/levels
