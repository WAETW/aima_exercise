import random
import sys
'''初始化環境'''
def dirt_placing():
    loc_A = random.choice(['Clean', 'Dirty'])
    loc_B = random.choice(['Clean', 'Dirty'])
    return loc_A,loc_B
'''agent初始位置'''
def init_loc():
    vacuum_init_loc = random.choice(['loc_A','loc_B'])
    return vacuum_init_loc
'''計算分數，agent往左往右扣一分，吸則得十分(參考Github Repo上提供的計算範例)'''
def socre(actions,loc_A,loc_B):
    your_score = 0
    vacuum_loc = ''
    if actions is 'Left':
        your_score = your_score - 1
        vacuum_loc = 'loc_A'
    elif actions is 'Right':
        your_score = your_score - 1
        vacuum_loc = 'loc_B'
    elif actions is 'Suck':
        if loc_A is 'Dirty':
            your_score = your_score + 10
            vacuum_loc = 'loc_A'
        elif loc_B is 'Dirty':
            your_score = your_score + 10
            vacuum_loc ='loc_B'
    return your_score,vacuum_loc
'''定義規則'''
def rule(location):
    loc_A,loc_B = dirt_placing()
    action = ''
    enviroment_state = ''
    if location is 'loc_A':
        enviroment_state = loc_A
    elif location is 'loc_B':
        enviroment_state = loc_B
    if location is "loc_A":
        if enviroment_state is "Clean":
            action = "Right"
        else:
            action = "Suck"
    elif location is "loc_B":
        if enviroment_state is "Clean":
            action = "Left"
        else:
            action = "Suck"
    print(action)
    return action,loc_A,loc_B
'''建立環境，episodes為執行次數'''
def enviroment(episodes):
    performence_score = 0
    vacuum_init_loc = init_loc()
    vacuum_loc = ''
    for i in range(0,episodes):
        if i is 0:
            action,loc_A,loc_B =rule(vacuum_init_loc)
            temp_score,vacuum_loc = socre(action,loc_A,loc_B)
            performence_score = performence_score + temp_score
        else:
            action,loc_A,loc_B =rule(vacuum_loc)
            temp_score,vacuum_loc = socre(action,loc_A,loc_B)
            performence_score = performence_score + temp_score
    print(performence_score)
def main():
    input = sys.argv[1]
    episodes = int(input[0])
    enviroment(episodes)
if __name__ == "__main__":
    main()
'''執行方法 python3 2-9.py 5，5為要執行的次數可自行更改 '''
