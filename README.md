# EX1
In this project we are giving (hopfully) the best solution for an offline algorithm,
in this project we had to deal with a new language and a little bit different problem   
in according to the first task. 
The algorithm has been implemented in python 3 using 3 main classes: Elevator, Elevators
and Calls classes.

# Our task's goal
The main goal of our task was to minimize the total waiting time in a givven list of calls
and building.

# Literature review

https://www.researchgate.net/publication/220590321_Optimization_of_Group_Elevator_Scheduling_With_Advance_Information

https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/

https://ls11-www.cs.tu-dortmund.de/people/preuss/pages/publications/BPM05.pdf

# Algorithm Explain
In our algorithm we are using 3 main classes, Elevator, Elevators and Calls and the code in implemented in the main class.
 -Elevator class: 
 df2dt: get the amount of floors that elevator need to tracel and the returns the time it will take to finish. 
 update: this function updates the elevator status, current floor is changed to the last elevator call destination, and
        the next time it will be free according to it's current state and expected travel time.
        
 Elevators: 
 read the building json file which inheritance from Elevator class.
 
 Calls:
 reads the csv file, and adds another columns which represents the time which take to the elevator to fulfill the call request
 from it current floor.
 
 Main:
 for each call we check for each elevator the time it will take to fulfill the call from the current floor and we take the fastest elevator's index and aloocate the choosen elevator to this call and than we update the next time for the elevator and the currnt floor.
 
 # Examples for allocations

Here we would like to represent some of the calls allocation in a graph.
for example, here we have of calls_A and B4 building.

![B4callsA](https://user-images.githubusercontent.com/87694635/142169228-e1d677fe-37e8-461b-980c-0a25fcaa018b.png)
 

