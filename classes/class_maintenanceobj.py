from dataclasses import dataclass
from datetime import datetime

@dataclass
class MaintenanceObj:
    start_day: int
    end_day: int
    start_time: str
    end_time: str

    def validate(self):
        now = datetime.now()
        if now.day >= self.start_day and now.day <= self.end_day:
            if now.strftime("%H:%M") >= self.start_time and now.strftime("%H:%M") <= self.end_time:
                return True
            else:
                return False
        else:
            return False