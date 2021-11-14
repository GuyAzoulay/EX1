import sys
from Elevator import *
class Building:

    Elevator_List = []
    def __init__(self, dict:dict={}):
        self.minfloor = dict["_minFloor"]
        self.maxfloor = dict["_maxFloor"]
        for elev in dict["_elevators"]:
            temp_elev = Elevator(elev)
            self.Elevator_List.append(temp_elev)

    def __str__(self):
        return f"minFloor:{self.minfloor}, maxFloor:{self.maxfloor}, Elevators: {self.Elevator_List}"

    def __add__(self, call):
        new_call = Calls(call)
        min_time = 999999999
        min_index = 0
        for elev in self.Elevator_List: ####need to go to the right id
            temp_time = elev.time(new_call)
            if temp_time < min_time:
                min_index = elev._id
                min_time = temp_time

        chosen_elev = self.Elevator_List[min_index]
        chosen_elev.__add__(new_call)
        return min_index


    def get_elev(self):