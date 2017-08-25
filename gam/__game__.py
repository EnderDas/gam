#__game__.py

class Game:

    def __init__(self):
        self.pages = self.Pages(self)
        self.sword_gen = self.Sword_gen(self)
        self.shop = self.Shop(self)
        self.trade = self.Trade(self)
        self.players = self.Players(self)

        class Pages:

            def __init__(self, game):
                self.game = game

            def __shop__(self):

            def __trade__(self):
