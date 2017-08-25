#__player__.py
from .db import _player, Load, Save
from .__sword__ import Sword, Hash

class Players:
    """
    *Players*

    What-It-Is
    *Players* is a class that lets you create players and get players
    in the form of *User* a class object.
    """
    def __init__(self):
        pass

    def get_player(self, name):
        """
        Returns a *User* object from a player file.
        """
        return User(name)

    def create_player(self, name):
        """
        Creates a player save file.
        """
        Save()._createPlayer(name)

class User:
    """
    User:object:
    
    User can be called without Players, but i suggest i shouldnt be just for
    clean code, if used with Players it will create a player if the player loaded
    doesnt exist (wont raise an error and fixes the problem)
    
    """
    def __init__(self, name):
        self.name = name
        self._unloadPlayer()
        self.give = self.Give(self)
        self.take = self.Take(self)
        self.change = self.Change(self)

    def _unloadPlayer(self):
        self.dict = Load()._loadPlayer(self.name)
        self.cred = self.Credits(self.dict['CREDITS'])
        self.weapons = self.dict['WEAPONS']
        self.rank = self.dict['RANK']
        self.exp = self.dict['EXP']
        self.weapon = self.Weapon(Sword().__parseHash__(self.dict['CURRENT WEAPON']))

    class Weapon:

        def __init__(self, sword):
            self.name = sword['Name']
            self.rank = sword['Rank']
            self.tier = sword['Tier']
            self.hash = sword['Hash_ID']

    class Credits:

        def __init__(self, dict):
            self.coins = dict['COINS']
            self.bills = dict['BILLS']
            self.chips = dict['CHIPS']
            if dict['CARD'] is False:
                self.card = False
            else:
                self.card = sum((self.coins * 0.01, self.bills, self.chips * 10))

    class Give:
        """
        coins - give the player coins
            ~ amount:int:

        bills - give the player bills
            ~ amount:int:

        chips - give the player chips
            ~ amount:int:

        exp - give the player exp
            ~ amount:int:

        sword - give the player a sword
            ~ stag:str:
        """
        def __init__(self, user):
            self.user = user

        def coins(self, amount):
            _player()._give_coins(self.user, amount)

        def bills(self, amount):
            _player()._give_bills(self.user, amount)

        def chips(self, amount):
            _player()._give_chips(self.user, amount)

        def exp(self, amount):
            _player()._give_exp(self.user, amount)

        def sword(self, stag):
            _player()._give_sword(self.user, stag)

    class Take:
        """
        +-functions----------------
        | coins | Take 
        """
        def __init__(self, user):
            self.user = user

        def coins(self, amount):
            _player()._take_coins(self.user, amount)

        def bills(self, amount):
            _player()._take_bills(self.user, amount)

        def chips(self, amount):
            _player()._take_chips(self.user, amount)

        def sword(self, stag):
            _player()._take_sword(self.user, stag)

    class Change:

        def __init__(self, user):
            self.user = user

        def current_wep(self, change):
            _player()._current_wep_change(self.user, change)

        def name(self, change):
            _player()._name_change(self.user, change)

        def card_status(self, stag):
            _player()._card_change(self.user, stag)

def _test(amount):
    p = Players()
    try:
        w = p.get_player("TestPlayer")
    except:
        p.create_player("TestPlayer")
        w = p.get_player("TestPlayer")
        w.give.coins(1)
    Exotics = []
    inter = 0
    import time
    for i in range(amount):
        wep = Hash().Gen(100)
        sword = Sword().__parseHash__(wep)
        if sword['Rank'] > 37:
            Exotics.append(sword)
            print(inter, "SE")
            time.sleep(3)
        else:
            print(inter)
        inter += 1
    import pprint
    pprint.pprint(Exotics)
