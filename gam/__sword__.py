#__sword__.py
import random
"""
What-It-Do:

__sword__ will handle sword hash parsing and generation of sword hashes.

"""

DICT = {
    1: {
        1: {
            "NAME": "Cheap",
            "TYPE": "Wood",
            "RP": 1,
            "PC": .70,
            "LVL": 0
        },
        2: {
            "NAME": "Heavy",
            "TYPE": "Stone",
            "RP": 3,
            "PC": .50,
            "LVL": 0
        },
        3: {
            "NAME": "Heavy",
            "TYPE": "Iron",
            "RP": 5,
            "PC": .30,
            "LVL": 0
        },
        4: {
            "NAME": "Light",
            "TYPE": "Aluminum",
            "RP": 7,
            "PC": .15,
            "LVL": 5
        },
        5: {
            "NAME": "Heavy",
            "TYPE": "Steel",
            "RP": 9,
            "PC": .10,
            "LVL": 7
        },
        6: {
            "NAME": "Quick",
            "TYPE": "Titanium",
            "RP": 10,
            "PC": .5,
            "LVL": 10
        }
    },
    2: {
        1: {
            "NAME": "Ruggid",
            "TYPE": "Cloth",
            "RP": 1,
            "PC": .70,
            "LVL": 0
        },
        2: {
            "NAME": "Rough",
            "TYPE": "Rope",
            "RP": 2,
            "PC": .50,
            "LVL": 0
        },
        3: {
            "NAME": "Gripping",
            "TYPE": "Leather",
            "RP": 3,
            "PC": .30,
            "LVL": 0
        },
        4: {
            "NAME": "Gripping",
            "TYPE": "Mold",
            "RP": 4,
            "PC": .15,
            "LVL": 5
        },
        5: {
            "NAME": "Comfortable",
            "TYPE": "Special Textile",
            "RP": 4,
            "PC": .10,
            "LVL": 10
        },
        6: {
            "NAME": "Lenient",
            "TYPE": "Carbon Fiber",
            "RP": 6,
            "PC": .5,
            "LVL": 15
        }
    },
    3: {
        1: {
            "NAME": "Unbalanced",
            "TYPE": "Wood",
            "RP": 1,
            "PC": .70,
            "LVL": 0
        },
        2: {
            "NAME": "Steadfast",
            "TYPE": "Iron",
            "RP": 2,
            "PC": .40,
            "LVL": 0
        },
        3: {
            "NAME": "Responsive",
            "TYPE": "Carbon",
            "RP": 3,
            "PC": .10,
            "LVL": 7
        }
    },
    4: {
        1: {
            "NAME": "Scared",
            "TYPE": "Wood",
            "RP": 1,
            "PC": .70,
            "LVL": 0
        },
        2: {
            "NAME": "Guarded",
            "TYPE": "Iron",
            "RP": 2,
            "PC": .50,
            "LVL": 0
        },
        3: {
            "NAME": "Guarded",
            "TYPE": "Gold",
            "RP": 3,
            "PC": .30,
            "LVL": 0
        },
        4: {
            "NAME": "Protective",
            "TYPE": "Steel",
            "RP": 4,
            "PC": .15,
            "LVL": 5
        },
        5: {
            "NAME": "Protective",
            "TYPE": "Titanium",
            "RP": 5,
            "PC": .10,
            "LVL": 10
        }
    },
    5: {
        1: {
            "NAME": "Weak",
            "TYPE": "Wood",
            "RP": 1,
            "PC": .70,
            "LVL": 0
        },
        2: {
            "NAME": "Weak",
            "TYPE": "Bamboo",
            "RP": 2,
            "PC": .65,
            "LVL": 0
        },
        3: {
            "NAME": "Weak",
            "TYPE": "Stone",
            "RP": 3,
            "PC": .60,
            "LVL": 0
        },
        4: {
            "NAME": "Sturdy",
            "TYPE": "Ceramic",
            "RP": 4,
            "PC": .55,
            "LVL": 0
        },
        5: {
            "NAME": "Sturdy",
            "TYPE": "Iron",
            "RP": 5,
            "PC": .55,
            "LVL": 0
        },
        6: {
            "NAME": "Decorative",
            "TYPE": "Gold",
            "RP": 5,
            "PC": .40,
            "LVL": 0
        },
        7: {
            "NAME": "Skillful",
            "TYPE": "Aluminum",
            "RP": 6,
            "PC": .50,
            "LVL": 5
        },
        8: {
            "NAME": "Durable",
            "TYPE": "Steel",
            "RP": 7,
            "PC": .45,
            "LVL": 5
        },
        9: {
            "NAME": "Durable",
            "TYPE": "Titanium",
            "RP": 8,
            "PC": .40,
            "LVL": 7
        },
        10: {
            "NAME": "Mastered",
            "TYPE": "Carbon Fiber",
            "RP": 9,
            "PC": .35,
            "LVL": 10
        },
        11: {
            "NAME": "Explosive",
            "TYPE": "Depleted Uranium",
            "RP": 10,
            "PC": .30,
            "LVL": 15
        },
        12: {
            "NAME": "Curious",
            "TYPE": "Odd Metal",
            "RP": 11,
            "PC": .25,
            "LVL": 15
        }
    },
    6: {
        1: {
            "NAME": "Small",
            "TYPE": "Short",
            "RP": 1,
            "PC": .70,
            "LVL": 0
        },
        2: {
            "NAME": "Standard",
            "TYPE": "Medium",
            "RP": 3,
            "PC": .45,
            "LVL": 7
        },
        3: {
            "NAME": "Tall",
            "TYPE": "Long",
            "RP": 5,
            "PC": .20,
            "LVL": 10
        }
    }
}

class Hash:

    def Gen(self, level):
        """1234-5-6"""

        self.level = level

        NUM_1 = self.get_one()
        NUM_2 = self.get_two()
        NUM_3 = self.get_three()
        NUM_4 = self.get_four()
        NUM_5 = self.get_five()
        NUM_6 = self.get_six()

        Hash = "{0}{1}{2}{3}-{4}-{5}".format(NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6)

        return Hash

    def get_one(self):
        num = random.randint(0, 5)
        if num is 0:
            if self.level < DICT[1][1]['LVL']:
                return self.get_one()
            else:
                if random.random() <= DICT[1][1]['PC']:
                    return 1
                else:
                    return self.get_one()
        elif num is 1:
            if self.level < DICT[1][2]['LVL']:
                return self.get_one()
            else:
                if random.random() <= DICT[1][2]['PC']:
                    return 2
                else:
                    return self.get_one()
        elif num is 2:
            if self.level < DICT[1][3]['LVL']:
                return self.get_one()
            else:
                if random.random() <= DICT[1][3]['PC']:
                    return 3
                else:
                    return self.get_one()
        elif num is 3:
            if self.level < DICT[1][4]['LVL']:
                return self.get_one()
            else:
                if random.random() <= DICT[1][4]['PC']:
                    return 4
                else:
                    return self.get_one()
        elif num is 4:
            if self.level < DICT[1][5]['LVL']:
                return self.get_one()
            else:
                if random.random() <= DICT[1][5]['PC']:
                    return 5
                else:
                    return self.get_one()
        elif num is 5:
            if self.level < DICT[1][6]['LVL']:
                return self.get_one()
            else:
                if random.random() <= DICT[1][6]['PC']:
                    return 6
                else:
                    return self.get_one()

    def get_two(self):
        num = random.randint(0, 5)
        if num is 0:
            if self.level < DICT[2][1]['LVL']:
                return self.get_two()
            else:
                if random.random() <= DICT[2][1]['PC']:
                    return 1
                else:
                    return self.get_two()
        elif num is 1:
            if self.level < DICT[2][2]['LVL']:
                return self.get_two()
            else:
                if random.random() <= DICT[2][2]['PC']:
                    return 2
                else:
                    return self.get_two()
        elif num is 2:
            if self.level < DICT[2][3]['LVL']:
                return self.get_two()
            else:
                if random.random() <= DICT[2][3]['PC']:
                    return 3
                else:
                    return self.get_two()
        elif num is 3:
            if self.level < DICT[2][4]['LVL']:
                return self.get_two()
            else:
                if random.random() <= DICT[2][4]['PC']:
                    return 4
                else:
                    return self.get_two()
        elif num is 4:
            if self.level < DICT[2][5]['LVL']:
                return self.get_two()
            else:
                if random.random() <= DICT[2][5]['PC']:
                    return 5
                else:
                    return self.get_two()
        elif num is 5:
            if self.level < DICT[2][6]['LVL']:
                return self.get_two()
            else:
                if random.random() <= DICT[2][6]['PC']:
                    return 6
                else:
                    return self.get_two()

    def get_three(self):
        num = random.randint(0, 2)
        if num is 0:
            if self.level < DICT[3][1]['LVL']:
                return self.get_three()
            else:
                if random.random() <= DICT[3][1]['PC']:
                    return 1
                else:
                    return self.get_three()
        elif num is 1:
            if self.level < DICT[3][2]['LVL']:
                return self.get_three()
            else:
                if random.random() <= DICT[3][2]['PC']:
                    return 2
                else:
                    return self.get_three()
        elif num is 2:
            if self.level < DICT[3][3]['LVL']:
                return self.get_three()
            else:
                if random.random() <= DICT[3][3]['PC']:
                    return 3
                else:
                    return self.get_three()

    def get_four(self):
        num = random.randint(0, 4)
        if num is 0:
            if self.level < DICT[4][1]['LVL']:
                return self.get_four()
            else:
                if random.random() <= DICT[4][1]['PC']:
                    return 1
                else:
                    return self.get_four()
        elif num is 1:
            if self.level < DICT[4][2]['LVL']:
                return self.get_four()
            else:
                if random.random() <= DICT[4][2]['PC']:
                    return 2
                else:
                    return self.get_four()
        elif num is 2:
            if self.level < DICT[4][3]['LVL']:
                return self.get_four()
            else:
                if random.random() <= DICT[4][3]['PC']:
                    return 3
                else:
                    return self.get_four()
        elif num is 3:
            if self.level < DICT[4][4]['LVL']:
                return self.get_four()
            else:
                if random.random() <= DICT[4][4]['PC']:
                    return 4
                else:
                    return self.get_four()
        elif num is 4:
            if self.level < DICT[4][5]['LVL']:
                return self.get_four()
            else:
                if random.random() <= DICT[4][5]['PC']:
                    return 5
                else:
                    return self.get_four()

    def get_five(self):
        num = random.randint(0, 11)
        if num is 0:
            if self.level < DICT[5][1]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][1]['PC']:
                    return 1
                else:
                    return self.get_five()
        elif num is 1:
            if self.level < DICT[5][2]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][2]['PC']:
                    return 2
                else:
                    return self.get_five()
        elif num is 2:
            if self.level < DICT[5][3]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][3]['PC']:
                    return 3
                else:
                    return self.get_five()
        elif num is 3:
            if self.level < DICT[5][4]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][4]['PC']:
                    return 4
                else:
                    return self.get_five()
        elif num is 4:
            if self.level < DICT[5][5]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][5]['PC']:
                    return 5
                else:
                    return self.get_five()
        elif num is 5:
            if self.level < DICT[5][6]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][6]['PC']:
                    return 6
                else:
                    return self.get_five()
        elif num is 6:
            if self.level < DICT[5][7]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][7]['PC']:
                    return 7
                else:
                    return self.get_five()
        elif num is 7:
            if self.level < DICT[5][8]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][8]['PC']:
                    return 8
                else:
                    return self.get_five()
        elif num is 8:
            if self.level < DICT[5][9]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][9]['PC']:
                    return 9
                else:
                    return self.get_five()
        elif num is 9:
            if self.level < DICT[5][10]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][10]['PC']:
                    return 10
                else:
                    return self.get_five()
        elif num is 10:
            if self.level < DICT[5][11]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][11]['PC']:
                    return 11
                else:
                    return self.get_five()
        elif num is 11:
            if self.level < DICT[5][12]['LVL']:
                return self.get_five()
            else:
                if random.random() <= DICT[5][12]['PC']:
                    return 12
                else:
                    return self.get_five()

    def get_six(self):
        num = random.randint(0, 2)
        if num is 0:
            if self.level < DICT[6][1]['LVL']:
                return self.get_six()
            else:
                if random.random() <= DICT[6][1]['PC']:
                    return 1
                else:
                    return self.get_six()
        elif num is 1:
            if self.level < DICT[6][2]['LVL']:
                return self.get_six()
            else:
                if random.random() <= DICT[6][2]['PC']:
                    return 2
                else:
                    return self.get_six()
        elif num is 2:
            if self.level < DICT[6][3]['LVL']:
                return self.get_six()
            else:
                if random.random() <= DICT[6][3]['PC']:
                    return 3
                else:
                    return self.get_six()

class Sword:

    def __parseHash__(self, sword):
        "1111-1-1"
        sword_dict = {
        "Name": None,
        "Hash_ID": sword,
        "Tier": None,
        "Rank": None
        }

        if sword[0] == 'C':
            if sword[1] == '1':
                sword_dict['Name'] = 'Poke\'s Squirrel Rod #Custom'
                sword_dict['Tier'] = 'Super Exotic'
                sword_dict['Rank'] = 0
                return sword_dict
            else:
                raise

        rank = 0
        rank += DICT[1][int(sword[0])]['RP']
        rank += DICT[2][int(sword[1])]['RP']
        rank += DICT[3][int(sword[2])]['RP']
        rank += DICT[4][int(sword[3])]['RP']

        if len(sword) > 8:
            rank += DICT[5][int(sword[5:7])]['RP']
            rank += DICT[6][int(sword[8])]['RP']
        else:
            rank += DICT[5][int(sword[5])]['RP']
            rank += DICT[6][int(sword[7])]['RP']

        if rank == 6:
            Tier = "Very Common"
        elif rank <= 7:
            Tier = "Common"
        elif rank <= 8:
            Tier = "Somewhat Common"
        elif rank <= 10:
            Tier = "Somewhat Uncommon"
        elif rank <= 12:
            Tier = "Uncommon"
        elif rank <= 14:
            Tier = "Very Uncommon"
        elif rank <= 16:
            Tier = "Somewhat Rare"
        elif rank <= 18:
            Tier = "Rare"
        elif rank <= 20:
            Tier = "Very Rare"
        elif rank <= 22:
            Tier = "Somewhat Legendary"
        elif rank <= 24:
            Tier = "Legendary"
        elif rank <= 26:
            Tier = "Very Legendary"
        elif rank <= 28:
            Tier = "Somewhat Epic"
        elif rank <= 30:
            Tier = "Epic"
        elif rank <= 32:
            Tier = "Very Epic"
        elif rank <= 34:
            Tier = "Somewhat Exotic"
        elif rank <= 36:
            Tier = "Exotic"
        elif rank <= 38:
            Tier = "Very Exotic"
        elif rank <= 39:
            Tier = "Somewhat Godlike"
        elif rank == 40:
            Tier = "Godlike"
            
        ONE = DICT[1][int(sword[0])]['NAME']
        TWO = DICT[2][int(sword[1])]['NAME']
        THREE = sword[2]
        FOUR = sword[3]

        if len(sword) > 8:
            FIVE = DICT[5][int(sword[5:7])]['NAME']
            SIX = DICT[6][int(sword[8])]['NAME']
        else:
            FIVE = DICT[5][int(sword[5])]['NAME']
            SIX = DICT[6][int(sword[7])]['NAME']

        name = f"{ONE}, {TWO}, and {FIVE} {SIX} Sword #{THREE}{FOUR}"

        sword_dict['Name'] = name
        sword_dict['Tier'] = Tier
        sword_dict['Rank'] = rank

        return sword_dict
