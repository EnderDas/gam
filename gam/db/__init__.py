#db.__init__.py
from .__save__ import Save
from .__load__ import Load


class _player:

    def _give_coins(self, player, amount):
        p = Load()._loadPlayer(player.name)
        p['CREDITS']['COINS'] += amount
        Save()._savePlayer(player.name, p)
        new = player.__class__.__init__(player, player.name)
        del player
        return new

    def _give_bills(self, player, amount):
        p = Load()._loadPlayer(player.name)
        p['CREDITS']['BILLS'] += amount
        Save()._savePlayer(player.name, p)
        new = player.__class__.__init__(player, player.name)
        del player
        return new

    def _give_chips(self, player, amount):
        p = Load()._loadPlayer(player.name)
        p['CREDITS']['CHIPS'] += amount
        Save()._savePlayer(player.name, p)
        new = player.__class__.__init__(player, player.name)
        del player
        return new

    def _give_sword(self, player, stag):
        p = Load()._loadPlayer(player.name)
        if stag in p['WEAPONS']:
            raise "DatabaseError :: Sword already in WEAPONS"
        else:
            p['WEAPONS'].append(stag)
        Save()._savePlayer(player.name, p)
        new = player.__class__.__init__(player, player.name)
        del player
        return new

    def _give_exp(self, player, amount):
        p = Load()._loadPlayer(player.name)
        p['EXP'] += amount
        Save()._savePlayer(player.name, p)
        new = player.__class__.__init__(player, player.name)
        del player
        return new

    def _take_coins(self, player, amount):
        p = Load()._loadPlayer(player.name)
        p['CREDITS']['COINS'] -= amount
        Save()._savePlayer(player.name, p)
        new = player.__class__.__init__(player, player.name)
        del player
        return new

    def _take_bills(self, player, amount):
        p = Load()._loadPlayer(player.name)
        p['CREDITS']['BILLS'] -= amount
        Save()._savePlayer(player.name, p)
        new = player.__class__.__init__(player, player.name)
        del player
        return new

    def _take_chips(self, player, amount):
        p = Load()._loadPlayer(player.name)
        p['CREDITS']['CHIPS'] -= amount
        Save()._savePlayer(player.name, p)
        new = player.__class__.__init__(player, player.name)
        del player
        return new

    def _take_sword(self, player, stag):
        p = Load()._loadPlayer(player.name)
        if stag in p['WEAPONS']:
            p['WEAPONS'].remove(stag)
        else:
            raise "DatabaseError :: Sword doesn't exist"
        Save()._savePlayer(player.name, p)
        new = player.__class__.__init__(player, player.name)
        del player
        return new

    def _current_wep_change(self, player, stag):
        p = Load()._loadPlayer(player.name)
        if stag in p['WEAPONS']:
            if stag == p['CURRENT WEAPON']:
                raise "DatabaseError :: Sword already equiped"
            else:
                p['CURRENT WEAPON'] = stag
                Save()._savePlayer(player.name, p)
        else:
            raise "DatabaseError :: Player doesn't own sword"
        new = player.__class__.__init__(player, player.name)
        del player
        return new

    def _name_chang(self, player, change):
        raise DeprecatedError

    def _card_change(self, player, change):
        p = Load()._loadPlayer(player.name)
