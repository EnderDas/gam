#__save__.py
from .__load__ import Load
import json

class Save:

    def _createPlayer(self, name):
        """
        {
        "NAME": str,
        "CREDITS": int,
        "WEAPONS": [],
        "RANK": int,
        "EXP": {
            "CURRENT": int,
            "CAP": int
            },
        "CURRENT_WEAPON": str
        }
        """
        try:
            with open(f"{name}.json", 'r') as fp:
                dict = json.load(fp)
                raise Error("DatabaseError :: Player already exists")
        except:
            with open(f"{name}.json", 'w') as fp:
                player = {
                "NAME": name,
                "CREDITS": {
                    "CARD": True,
                    "COINS": 0,
                    "BILLS": 0,
                    "CHIPS": 0
                    },
                "WEAPONS": [
                    "1111-1-1",
                    "C0"
                    ],
                "RANK": 1,
                "EXP": 1000,
                "CURRENT WEAPON": "1111-1-1"
                }
                json.dump(player, fp, sort_keys=True, indent=4)
                return True

    def _savePlayer(self, name, new):
        try:
            with open(f"{name}.json", 'w') as fp:
                json.dump(new, fp, sort_keys=True, indent=4)
        except:
            raise Error("DatabaseError :: Player doesn't exist")
