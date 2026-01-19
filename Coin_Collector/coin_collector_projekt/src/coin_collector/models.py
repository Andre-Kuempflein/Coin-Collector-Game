from pydantic import BaseModel, Field
from typing import List, Tuple

class Coin(BaseModel):
    x: float
    y: float
    r: float

class Wall(BaseModel):
    x: float
    y: float
    w: float
    h: float

class LevelConfig(BaseModel):
    width: int = Field(gt=0)
    height: int = Field(gt=0)
    player_start: Tuple[float, float]
    coins: List[Coin]
    walls: List[Wall]