
import json
from calls import *
class Elevator:
    calls = []
    curr_floor = 0
    _type = []
    _src = []
    _dest = []
    _time = 0
    _in_motion = 0
    def __init__(self, dct):
        for k, v in dct.items():
            setattr(self, k, v)

    def __add__(self, call: Calls):
        self.calls.append(call)
        self._src.append(call.src)
        self._dest.append(call.dest)

#t=d/s
    def time_call(self):
        time = 0
        temp_floor = self.curr_floor
        for call in self.calls:
            time += abs(call.src - temp_floor)/self._speed
            time += self._openTime + self._startTime + self._stopTime + self._closeTime
            temp_floor = call.src
            time += abs(call.dest - temp_floor)/self._speed
            time += self._openTime + self._startTime + self._stopTime + self._closeTime
            temp_floor = call.dest
        return time

#calculate the time it will take for the elevator to complete the given call with the the rest of the calls
    def time(self, call):
        if len(self.calls) > 0:
            total_time = self.time_call()
            temp_floor = self.calls[len(self.calls)-1].dest #calculatin from the last destenation
            call_time = abs(call.src - temp_floor) / self._speed
            call_time += self._openTime + self._startTime + self._stopTime + self._closeTime
            call_time += abs(call.dest - call.src) / self._speed
            call_time += self._openTime + self._startTime + self._stopTime + self._closeTime
            return total_time+call_time
        else:
            return 0