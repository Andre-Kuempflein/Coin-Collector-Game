import typer
import json
from pathlib import Path
from pydantic import ValidationError
from .models import LevelConfig
from .game import CoinCollectorGame

app = typer.Typer()

@app.command()
def start(
    level: Path = typer.Option(..., help="Pfad zur Level-JSON-Datei"),
    fps: int = typer.Option(60, help="Bilder pro Sekunde"),
    debug: bool = typer.Option(False, help="Debug-Modus zeigt Kollisionsboxen")
):
    try:
        # JSON-Datei laden
        with open(level, "r") as f:
            data = json.load(f)
        
        # Validierung mit Pydantic
        config = LevelConfig(**data)
        
        # Spiel starten
        game = CoinCollectorGame(config, fps, debug)
        game.run()
        
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{level}' wurde nicht gefunden.")
        raise typer.Exit(code=1)
    except ValidationError as e:
        print("Fehler in der Level-Datei:")
        print(e)
        raise typer.Exit(code=1)
    except json.JSONDecodeError:
        print(f"Fehler: '{level}' ist kein gueltiges JSON.")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()