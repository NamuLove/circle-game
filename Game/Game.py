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
            print(self.name)
            p1_input = input('답을 입력하시오')
            if self.answer == p1_input:
                self.result = True
            else:
                print('fail')
    class quest:
        def __init__(self, name, exp, gold):
            self.name = name
            self.exp = exp
            self.gold = gold
        def quest_start(self, quiz, player):
            print('{}-퀘스트 시작'.format(self.name))
            print('.')
            print('')
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
            p.hp -= self.atk
    quiz1 = quiz('손톱은 발톱보다 더 빨리 자란다?', 'o', False)
    quiz2 = quiz('몸의 북기를 방치하면 살이 된다?', 'x', False)
    quiz
    quest1 = quest('cheese', 10, 10)
    while True:
        print('choose your destination(quest)')
        reply = input('reply')
        if reply == 'quest':
            while True:
                reply_quest = input('choose your quest(cheese)')
                if reply_quest == 'cheese':
                    quest1.quest_start(quiz1, p1)
                    break
                else:
                    print('write right reply')
        else:
            print()






