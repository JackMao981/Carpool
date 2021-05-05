# Fair Carpool Sharing Project
#### by Jack Mao, Audrey Lee, Shirin Kuppusamy

There are three files in this repository:

**generate_schedule.py** : This file creates a random schedule 


**carpool.py** : This file includes our code for BFS and for Edmonds-Karp 


**test.py** : This file contains our test cases to verify correct functionality of our algorithm 

To run our project, open a terminal and run ```python test.py``` If you would like
to try deterministic schedules not already in our test cases, then you
can add a new function in test.py. The outputs of the test file include a pretty print of the 
adjacency matrix of Network Flows - where each of the rows across the top is source,all the people, all the days, sink 
and each column is the same. The value at each (row, column) is the edge weight (network flow) between those two values. 
The second output is a pretty print of the driving schedule after it is solved, where the value is responsibility for a 
given person on a given day.
