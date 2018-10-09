import random

'''初始化環境'''
def dirt_placing():
    loc_A = random.choice(['Clean', 'Dirty'])
    loc_B = random.choice(['Clean', 'Dirty'])
    return loc_A,loc_B
'''agent初始位置'''
def init_loc():
    vacuum_init_loc = random.choice(['loc_A','loc_B'])
    return vacuum_init_loc
'''計算分數，agent往左往右扣一分，吸則得十分(參考Github Repo上提供的計算範例)''''
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
    location_lists = []
    enviroment_state_lists = []
    location_lists.append(location)
    action = ""
    if location_lists == ['loc_A']:
        enviroment_state_lists.append(loc_A)
    elif location_lists == ['loc_B']:
        enviroment_state_lists.append(loc_B)
    for location_list in location_lists:
        if location_list is "loc_A":
            for enviroment_state_list in enviroment_state_lists:
                if enviroment_state_list is "Clean":
                    action = "Right"
                else:
                    action = "Suck"
        elif location_list is "loc_B":
            for enviroment_state_list in enviroment_state_lists:
                if enviroment_state_list is "Clean":
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
enviroment(5)
