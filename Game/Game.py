#game 2022.09.21
import time
import random
class player:
    def __init__(self, fhp, hp, atk, deff, gold, exp, level, battle_def, key):
        self.fhp = fhp
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.gold = gold
        self.exp = exp
        self.level = level
        self.battle_def = battle_def
        self.key = key
    def player_atk(self, enemy):
        enemy.hp -= self.atk
        print('===================')
        time.sleep(0.1)
        print('{}의 피해를 준다?'.format(self.atk))
        time.sleep(0.1)
        print('적은 체력이 {} 남았다'.format(enemy.hp))
        time.sleep(0.1)
        print('===================')
        time.sleep(0.1)
    def player_def(self):
        self.battle_def = self.deff * 2
    def battle_gain(self, enemy):
        self.gold += enemy.gold
        self.exp += enemy.exp

class level:
    def __init__(self, level_default, level_value):
        self.level_default = level_default
        self.level_value = level_value
    def level_up(self, p):
        self.level_default = 10
        if self.level_value * self.level_default <= p.exp:
            p.level += 1
            print('레벨 업!\n플레이어 레벨: {}'.format(p.level))
            self.level_value = self.level_value * 2.5
            a = (random.randrange(1, 5) + 4)//2
            b = (random.randrange(1, 5) + 4)//2
            c = (random.randrange(1, 5) + 4)//2
            print('체력이 {}만큼 성장했습니다!'.format(c))
            print('방어력이 {}만큼 성장했습니다!'.format(b))
            print('공격력이 {}만큼 성장했습니다!'.format(a))
            p.atk += a
            p.deff += b
            p.fhp += c
            p.hp = p.fhp
            return self.level_value
print('#     #    #    #     # #     # ####### #       ####### #     #    #    #     #     #####  \n##   ##   # #   ##    # #     # #     # #       #       ##   ##   # #   ##    #    #     # \n# # # #  #   #  # #   # #     # #     # #       #       # # # #  #   #  # #   #          # \n#  #  # #     # #  #  # ####### #     # #       #####   #  #  # #     # #  #  #     #####  \n#     # ####### #   # # #     # #     # #       #       #     # ####### #   # #    #       \n#     # #     # #    ## #     # #     # #       #       #     # #     # #    ##    #       \n#     # #     # #     # #     # ####### ####### ####### #     # #     # #     #    ####### ')
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

    p1 = player(30, 30, 5, 5, 0, 0, 1, 0, 0)
    level1 = level(10, 1)


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
                player.exp += self.gold
                level1.level_up(player)

            else:
                print('틀렸어!')


    class boss:
        def __init__(self, fhp, hp, atk, exp, gold, name):
            self.fhp =fhp
            self.hp = hp
            self.atk = atk
            self.exp = exp
            self.gold = gold
            self.name = name
        def boss_atk(self, p):
            print('==========보스 차례==========')
            time.sleep(0.1)
            p.hp -= self.atk + p.battle_def
            print('{}의 피해를 받았다.?'.format(self.atk))
            time.sleep(0.1)
            print('나의 체력은 {}만 남았다?'.format(p.hp))
            time.sleep(0.1)
            print('====================')
            time.sleep(0.1)

    def battle(enemy, player):
        while True:
            print('\n====================\n플레이어\n체력: {}-공격력: {}-방어력: {}\n===================='.format(player.hp, player.atk, player.deff))
            player_battle_decision = input('\n(공격-1)-(방어-2)-(탐색-3)\n숫자를 입력하세요>>>')
            time.sleep(0.5)
            if player_battle_decision == '1':
                player.player_atk(enemy)
            elif player_battle_decision == '2':
                player.player_def()
            elif player_battle_decision == '3':
                print('\n====================\n보스\n체력: {}-공격력: {}\n===================='.format(enemy.hp, enemy.atk))
            time.sleep(0.5)
            if enemy.hp <= 0:
                time.sleep(0.5)
                print('승리')
                player.battle_gain(enemy)
                level1.level_up(player)
                enemy.hp = enemy.fhp
                break
            enemy.boss_atk(player)
            if player.hp <= 0:
                print('너의 패배')
                break
    quiz1 = quiz('손톱은 발톱보다 더 빨리 자란다?', '네', False)
    quiz2 = quiz('몸의 북기를 방치하면 살이 된다?', '아니오', False)
    quest1 = quest('치즈', 2, 5)
    quest2 = quest('빵', 2, 5)

    boss1 = boss(20, 20, 8, 5, 20, '오물킹')
    boss2 = boss(30, 30, 6, 30, 30, '옥상황제')
    ene1 = boss(10, 10, 5, 2, 10, '쥐돌이')
    ene2 = boss(12, 12, 4, 2, 10, '멸치 시체')
    ene3 = boss(12, 12, 4, 2, 10, '기이과인')
    while True:
        move = input('===================\n어떤 행동을 하실 건가요?\n(이동-1)-(상태 확인-2)-(의료실-3)\n숫자를 입력하세요>>>')
        time.sleep(0.5)

        if move == '1':
            travel = True
            while travel:
                reply = input('===================\n어디로 이동하실건가요?\n(던전 퀘스트-1)-(보스방-2)-(던전-3)(뒤로가기-0)\n숫자를 입력하세요>>>')
                time.sleep(0.5)

                if reply == '1':
                    while True:
                        reply_quest = input('===================\n퀘스트를 선택하세요?\n(치즈 퀘스트-1)-(빵집 퀘스트-2)-(뒤로가기-0)\n숫자를 입력하세요>>>')
                        if reply_quest == '1':
                            quest1.quest_start(quiz1, p1)
                            travel = False
                            break
                        if reply_quest == '2':
                            quest2.quest_start(quiz2, p1)
                            travel = False
                            break
                        if reply_quest == '0':
                            break
                        else:
                            print('다시 입력해주세요')
                            time.sleep(0.5)

                elif reply == '2':
                    while True:
                        reply_boss = input('===================\n보스를 선택하세요?\n(중간 보스방<1>-1)-(최종 보스<2>-2)(뒤로가기-0)\n숫자를 입력하세요>>>')
                        time.sleep(0.5)
                        if reply_boss == '1':
                            battle(boss1, p1)
                            travel = False
                            break
                        if reply_boss == '2':
                            battle(boss2, p1)
                            travel = False
                            break
                        elif reply_boss == '0':
                            break
                        else:
                            print('다시 입력해주세요')
                            time.sleep(0.5)
                elif reply == '3':
                    while True:
                        reply_dungeon = input('===================\n던전를 선택하세요?\n(던전1-1)-(던전2-2)-(뒤로가기-0)\n숫자를 입력하세요>>>')
                        time.sleep(0.5)
                        if reply_dungeon == '1':
                            print('=========첫번째 적=========')
                            time.sleep(1)
                            battle(ene1, p1)
                            print('=========두번째 적=========')
                            time.sleep(1)
                            battle(ene1, p1)
                            print('=========세번째 적=========')
                            time.sleep(1)
                            battle(ene1, p1)
                            travel = False
                            break
                        elif reply_dungeon == '2':
                            print()

                        elif reply_dungeon == '0':
                            break
                elif reply == '0':
                    travel = False
                else:
                    print('===================\n다시 입력해주시겠어요?')


        elif move == '2':

            print('9999999999999999999999\n플레이어\n체력: {}\n공격력: {}\n방어력: {}\n금: {}\n경험치: {}\n6666666666666666666666'.format(p1.hp, p1.atk, p1.deff, p1.gold, p1.exp))
            while True:
                self_check = input('(뒤로가기-1)\n숫자를 입력하세요>>>')
                time.sleep(0.5)
                if self_check == '1':
                    break
                else:
                    print('다시 입력해주세요')
                    time.sleep(0.5)
        elif move == '3':
            print('===================\n치료하시겠습니까?(골드 15소비)(예-1/뒤로가기-0)\n===================')
            while True:
                t_reply = input('숫자를 입력하세요>>>')
                time.sleep(0.5)
                if t_reply == '1':
                    if p1.gold >= 15:
                        p1.gold = p1.gold - 15
                        p1.hp = p1.fhp
                        print('치료했습니다.(현재 체력:{}'.format(p1.hp))
                        break
                    else:
                        print('돈이 부족합니다.')
                if t_reply == '0':
                    break



        if p1.hp <= 0:
            print('플레이어: 깨꼬닭!\n======================\n당신은 사망했습니다\n======================')
            break