import json
from Elevator import *


class Elevators:
    Elevators_List = []
    def __init__(self,fileName):
        try:
            with open(fileName,"r") as f:
                build = json.load(f)
                self.minfloor = build['_minFloor']
                self.maxfloor = build["_maxFloor"]
                for elev in build['_elevators']:
                    self.Elevators_List.append(Elevator(elev))
        except IOError as e:
            print(e)

    def __repr__(self):
       return f"minFloor:{self.minfloor}, maxFloor:{self.maxfloor}, Elevators: {self.Elevators_List}"

    def __getitem__(self, item):
        return self.Elevators_List[item]





