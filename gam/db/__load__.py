#__load__.py
import json

class Load:

    def _loadPlayer(self, name):
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
            return dict
        except:
            raise Error("PlayerError :: Player doesn't exist")
