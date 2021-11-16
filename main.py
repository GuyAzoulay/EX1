from Calls import *
from Elevators import *

import numpy as np
import matplotlib.pyplot as plt

from calls_output import *


if __name__ == '__main__':
    c = Calls('./Calls_c.csv')
    e = Elevators('B2.json')
    c.get_elevators_time(e)
    output = calls_output('./Calls_c.csv')
    # print(c.calls)

    for i, call in c.calls.iterrows():
        # index is needed for updating the original c.calls dataframe
        elev_times = []
        # this loop calculates the times each elevator will take to complete the current call
        for elevator in e.Elevators_List:
            elev_time = elevator.next_time_free # if elevator.next_time_free > call['t0'] else call['t0']

            # this part checks weather the elevator is in the source floor. if not, it adds the time to source to the
            # total time
            df_arrival = abs(elevator.current_floor - call['source'])
            if not df_arrival: elev_time += elevator.df2dt(df_arrival)

            # this adds the call execution time for each elevator
            elev_time += call[f'dt_elev_{elevator.id}']
            elev_times.append(elev_time)

        # here we find the best elevator index
        best_elevator_index = np.argmin(elev_times)

        call['elevator_index'] = best_elevator_index
        c.calls.iloc[i] = call
        output.file[i][5] = best_elevator_index

        # here we update the best elevator status
        best_elevator = e.Elevators_List[best_elevator_index]
        best_elevator.update(elev_times[best_elevator_index], call)

        # print()
    output.save_csv(fileName='out.csv', calls=output.file)
    # print(c.calls['elevator_index'])
    plt.figure()
    c.calls['elevator_index'].hist()
    plt.show()

