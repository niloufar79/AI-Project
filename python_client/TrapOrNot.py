from dijkstra_level2 import dijkstrawayenemy
from dijkstraforAll import dijkstraforall
from queue import LifoQueue
from math import inf
#maybe we can check collision here
#should change value


def trapornot(gridmap, height, width, next_move_agent, next_move_enemy, maxvalue, score_agent, score_enemy, start_agent, start_enemy, leastscore, remainturn, diccolornumber_agent, diccolornumber_enemy, agent_trap, enemy_trap, character, character_enemy):

    enemyway = dijkstrawayenemy(start_enemy[0], start_enemy[1], next_move_enemy[0], next_move_enemy[1], gridmap, height, width, score_enemy, character_enemy ,character, diccolornumber_enemy, agent_trap)
    dicforall, dicfordiamond, dicforhole = dijkstraforall(gridmap, height, width, start_agent[0], start_agent[1], score_agent, enemy_trap, character, diccolornumber_agent)
    maxvaluefortrap = maxvalue
    nextmove = tuple() if next_move_agent == tuple() else next_move_agent
    while not enemyway.empty():
        place = enemyway.get()
        #print(place , "*" * 20)
        if place == ():
            continue
        if dicforall[place[0]][place[1]] == inf:
            continue
        place_togo = dicforall[place[0]][place[1]][0]
        if gridmap[place[0]][place[1]] == 'E' or gridmap[place[0]][place[1]] == 'E'+character:
            print("im in e")
            if ((place_togo + 2) < place[2]) and ((score_agent - (place_togo + 1)) >= leastscore):
                value = (40 - (place_togo + 2)) * (4//10)
                if value > maxvaluefortrap:
                    maxvaluefortrap = value
                    nextmove = (place[0], place[1])
                    print(nextmove,"nextmovetrap")
                print(value, "value for e")
        if (gridmap[place[0]][place[1]] == '1') and (diccolornumber_agent['y'] < 15):
            if ((place_togo + 2) < place[2]) and (((score_agent + 10) - (place_togo + 1)) >= leastscore):
                value = (40 - (place_togo + 2)) * (4//10) + 10
                if value > maxvaluefortrap:
                    maxvaluefortrap = value
                    nextmove = (place[0], place[1])
                    # print(nextmove,"nextmovetrap")
                print(value, "value for y")
        if (gridmap[place[0]][place[1]] == '2') and (diccolornumber_agent['g'] < 8):
            if ((place_togo + 2) < place[2]) and (((score_agent + 25) - (place_togo + 1)) >= leastscore):
                value = (40 - (place_togo + 2)) * (4 // 10) + 25
                if value > maxvaluefortrap:
                    maxvaluefortrap = value
                    nextmove = (place[0], place[1])
                    # print(nextmove, "nextmovetrap")
                print(value, "value for g")
        if (gridmap[place[0]][place[1]] == '3') and (diccolornumber_agent['r'] < 5):
            if ((place_togo + 2) < place[2]) and (
                    ((score_agent + 35) - (place_togo + 1)) >= leastscore):
                value = (40 - place_togo + 2) * (4 // 10) + 35
                if value > maxvaluefortrap:
                    maxvaluefortrap = value
                    nextmove = (place[0], place[1])
                    # print(nextmove, "nextmovetrap")
                print(value, "value for r")
        if (gridmap[place[0]][place[1]] == '4') and (diccolornumber_agent['b'] < 4):
            if ((place_togo + 2) < place[2]) and (
                    ((score_agent + 75) - (place_togo + 1)) >= leastscore):
                value = (40 - (place_togo + 2)) * (4 // 10) + 75
                if value > maxvaluefortrap:
                    maxvaluefortrap = value
                    nextmove = (place[0], place[1])
                    # print(nextmove, "nextmovetrap")
                print(value, "value for b")

    return nextmove, maxvaluefortrap
