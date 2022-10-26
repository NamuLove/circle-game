#game 2022.09.21
import time
import random
class player:
    def __init__(self, hp, atk, deff, gold, exp):
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.gd = gold
        self.exp = exp
    def player_atk(self, enemy):
        enemy.hp -= self.atk
        print('{}의 피해를 준다?'.format(self.atk))
        print('적은 체력이 {}만 남았다'.format(enemy.hp))
    def level_up(self, enemy):
        enemy

while True:
    time.sleep(0.5)
    print('당신은 길을 걷고 있었다?')
    time.sleep(0.5)
    print('당신은 떨어졌다?')
    time.sleep(0.5)
    print('"여기는 어디인가?"')
    time.sleep(0.5)
    print('나는 누구인가?')
    time.sleep(0.5)
    print('레벨을 올리고 보스를 격파하여 원래 세상으로 돌아가세요?')
    p1 = player(10, 8, 5, 0, 0)


    class quiz:
        def __init__(self, name, answer, result):
            self.name = name
            self.answer = answer
            self.result = result
        def quiz_start(self):
            self.result = False
            print(self.name)
            p1_input = input('답을 입력하시오')
            if self.answer == p1_input:
                self.result = True
            else:
                print('실패')


    class quest:
        def __init__(self, name, exp, gold):
            self.name = name
            self.exp = exp
            self.gold = gold
        def quest_start(self, quiz, player):
            print('{}-퀘스트 시작'.format(self.name))
            print('.')
            print('.')
            quiz.quiz_start()
            if quiz.result == True:
                print('맞았어요!')
                player.exp += self.exp
                player.exp += self.gold

            else:
                print('틀렸어!')


    class boss:
        def __init__(self, hp, atk):
            self.hp = hp
            self.atk = atk
        def boss_atk(self, p):
            boss_default_hp = self.hp
            if 0 >= self.atk - p.deff:
                print('막다?')
                while True:
                    p.player_atk(self)
                    if self.hp <= 0:
                        print('승리')
                        self.hp = boss_default_hp
                        break
            else:
                while True:
                    p.hp -= self.atk - p.deff
                    print('{}의 피해를 봤다?'.format(self.atk - p.deff))
                    p.player_atk(self)
                    if self.hp == 0:
                        print('보스 죽음')
                        print('승리!')
                        break
                    if p.hp == 0:
                        print('플레이어 죽음')
                        print('패배')
                        break


    quiz1 = quiz('손톱은 발톱보다 더 빨리 자란다?', '네', False)
    quiz2 = quiz('몸의 북기를 방치하면 살이 된다?', '아니오', False)
    quest1 = quest('치즈', 10, 10)
    quest2 = quest('빵', 10, 10)
    boss1 = boss(10, 2)
    while True:
        move = input('어떤 행동을 하실 건가요?\n(이동)-()-()\n>>>')
        if move == '이동':
            while True:
                reply = input('어디로 이동하실건가요?\n(던전 퀘스트)-(보스방)-(뒤로가기)\n>>>')
                if reply == '던전 퀘스트':
                    while True:
                        reply_quest = input('퀘스트를 선택하세요?\n(치즈 퀘스트)-(빵집 퀘스트)-(뒤로가기)\n>>>')
                        if reply_quest == '치즈 퀘스트':
                            quest1.quest_start(quiz1, p1)
                            break
                        if reply_quest == '빵집 퀘스트':
                            quest2.quest_start(quiz2, p1)
                            break
                        if reply_quest == '뒤로가기':
                            break
                elif reply == '보스방':
                    while True:
                        reply_boss = input('보스를 선택하세요?\n(보스1)-(뒤로가기)\n>>>')
                        if reply_boss == '보스1':
                            boss1.boss_atk(p1)
                            break
                        if reply_boss == '뒤로가기':
                            break
                elif reply == '뒤로가기':
                    break
                else:
                    print('다시 입력해주시겠어요?')


