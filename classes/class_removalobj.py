from dataclasses import dataclass
from datetime import datetime

@dataclass
class RemovalObj:
    name: str
    type: str
    group: str
    removed: bool = False
    log: str = ""
    exitcode: int = -1
    date: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")