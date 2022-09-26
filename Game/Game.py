#game 2022.09.21
class player:
    def __init__(self, hp, atk, deff, gold, exp):
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.gd = gold
        self.exp = exp
    def level_up(self, enemy):
        enemy
class boss:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk
    def boss_atk(self, p):
        p.hp -= self.atk

class quest:
    def __init__(self, name, exp, gold):
        self.name = name
        self.exp = exp
        self.gold = gold
    def quest_
