import sys
from Elevator import Elevator
import json
class Building:
    Elevator_List=[]
    def __init__(self, dict):
        with open(dict) as f:
            building = json.load(f)
        self.minfloor = building["_minFloor"]
        self.maxfloor = building["_maxFloor"]
        for elev in building["_elevators"]:
            temp_elev = Elevator(elev)
            self.Elevator_List.append(temp_elev)

    def __str__(self):
        return f"minFloor:{self.minfloor}, maxFloor:{self.maxfloor}, Elevators: {self.Elevator_List}"

    def __add__(self, call):
        total_time = []
        min_time = sys.maxint
        min_index = 0
        for elev in self.Elevator_List:
            temp_elev = Elevator(elev)
            temp_time = temp_elev.time(call)
            total_time.append(temp_time)
            if temp_time < min_time:
                min_index = elev._id
                min_time = temp_time

        chosen_elev = self.Elevator_List[min_index]
        chosen_elev.__add__(call)
