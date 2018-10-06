# input loc_A, 'Clean'

location_lists = ["loc_A","loc_A","loc_B"]
enviroment_state_lists = ["Clean","Clean","Dirty"]


def action(location,enviroment_state):
    location_lists = location
    enviroment_state_lists = enviroment_state

def rule():
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
    #print(action)

rule()
