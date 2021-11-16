class Elevator:
    def __init__(self, dict_elev):
        self.id = dict_elev['_id']
        self._speed = dict_elev['_speed']
        self._minFloor = dict_elev['_minFloor']
        self._maxFloor = dict_elev['_maxFloor']
        self._closeTime = dict_elev['_closeTime']
        self._openTime = dict_elev['_openTime']
        self._startTime = dict_elev['_startTime']
        self._stopTime = dict_elev['_stopTime']

        self.current_floor = 0
        self.next_time_free = 0

    def df2dt(self, df):
        return self._closeTime + self._startTime + df / self._speed + self._stopTime + self._openTime

    def update(self, travel_time, call):
        # this function updates the elevator status, current floor is changed to the last elevator call destination, and
        # the next time it will be free according to it's current state and expected travel time
        self.current_floor = call['destination']

        if self.next_time_free < call['t0']: self.next_time_free = call['t0'] + travel_time
        else: self.next_time_free += travel_time

    def __str__(self):
        return f"_id:{self._id}, _speed:{self._speed}, _minFloor: {self._minFloor},_maxFloor:{self._maxFloor},_closeTime:{self._closeTime},_openTime:{self._openTime},_startTime:{self._startTime},_stopTime:{self._stopTime}"

    def __repr__(self):
        return f"_id:{self._id}, _speed:{self._speed}, _minFloor: {self._minFloor},_maxFloor:{self._maxFloor},_closeTime:{self._closeTime},_openTime:{self._openTime},_startTime:{self._startTime},_stopTime:{self._stopTime}"
