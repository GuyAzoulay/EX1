import json
from Calls import Calls
class Elevator:
    call = []
    _floor = 0
    _type = []
    _src = []
    _dest = []
    def __init__(self, dct):
        for k, v in dct.items():
            setattr(self, k, v)

    def __add__(self, call: Calls):
        self.call.append(call)
        self._src.append(call.src)
        self._dest.append(call.dest)

#calculate the time it will take for the elevator to complete the given call with the the rest of the calls
    def time(self, call):
        time = self._openTime + self._startTime + self._stopTime + self._closeTime
        if len(self.call) == 0:
            return 0



