from Elevators import *

import pandas as pd


class Calls:
    def __init__(self, file_name) -> object:
        self.calls = pd.read_csv(file_name, header=None, usecols=[1, 2, 3, 5],
                                 names=['t0', 'source', 'destination', 'elevator_index'])
        self.calls['df'] = abs(self.calls['source'] - self.calls['destination'])

    def get_elevators_time(self, elevators: Elevators):
        for elev in elevators.Elevators_List:
            self.calls[f'dt_elev_{elev.id}'] = elev.df2dt(self.calls['df'])

