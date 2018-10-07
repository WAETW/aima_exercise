import random

def dirt_placing():
    loc_A1 = random.choice(['Clean', 'Dirty'])
    loc_B1 = random.choice(['Clean', 'Dirty'])
    print ("A:"+loc_A1)
    print ("B:"+loc_B1)
    return loc_A1,loc_B1
def init_loc():
    vacuum_loc = random.choice(['loc_A','loc_B'])
    print("init:"+vacuum_loc)
    return vacuum_loc
def socre(actions,loc_1,loc_2):
    loc_A = loc_1
    loc_B = loc_2
    your_score = 0
    if actions is 'Left':
        your_score = your_score - 1
        vacuum_loc = 'loc_B'
    elif actions is 'Right':
        your_score = your_score - 1
        vacuum_loc = 'loc_B'
    elif actions is 'Suck':
        if loc_A is 'Dirty':
            your_score = your_score + 10
        elif loc_B is 'Dirty':
            your_score = your_score + 10
    return your_score
def rule(location):
    loc_A,loc_B = dirt_placing()
    location_lists = []
    enviroment_state_lists = []
    location_lists.append(location)
    print(location_lists)
    action = ""
    if location_lists == ['loc_A']:
        enviroment_state_lists.append(loc_A)
    elif location_lists == ['loc_B']:
        enviroment_state_lists.append(loc_B)
    print(enviroment_state_lists)
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
def enviroment(episodes):
    performence_score = 0
    for i in range(0,episodes):
        action,loc_A,loc_B =rule(init_loc())
        performence_score = performence_score + socre(action,loc_A,loc_B)
    print(performence_score)
enviroment(5)
