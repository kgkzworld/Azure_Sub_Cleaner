from dataclasses import dataclass
from az.cli import az

@dataclass
class CloudObj:
    name: str
    id: str
    tenantId: str
    hasAccess: list

    def show(self):
        return (az("account show")[1])

    def validate(self):
        if self.id == az("account show")[1]['id']:
            return True
        else:
            return False

    def validateUser(self):
        if az("account show")[1]["user"]["name"] in self.hasAccess:
            return True
        else:
            return False
