# A-Search-Algorithm
A* Search Algorithm implemented to print out a sequence of hex coordinates that form the lowest cost path from the start cell to the goal cell. More specifically, the cost of the solution sequence, and then the sequence itself, is printed to standard output. The first line is an integer denoting the cost, and subsequent
lines are of the form (r,q), denoting the ordered solution sequence of coordinates. If there is no valid solution, 0 is outputted with no subsequent lines. Reads in an input JSON file (see sample_input.json) for size "n" of board space, possible "blocks" on the board, a start and goal coordinates. 

To run program download and type: ```python -m search sample_input.json``` in command line. 

Example of JSON file(a), visual diagram of board (b) and output of this solution (c) below:

![image](https://user-images.githubusercontent.com/70874436/210516130-5215b1a6-a45a-4b2d-984e-f44b3c2fe68e.png)

