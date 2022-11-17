from typing import Optional
from dataclasses import dataclass


@dataclass
class DobotPosition:
    x: Optional[int] = None
    y: Optional[int] = None
    z: Optional[int] = None
    r: Optional[int] = None
