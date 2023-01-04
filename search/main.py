"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""
from collections import defaultdict
from cgitb import small
import sys
import json
from tarfile import BLOCKSIZE
from tkinter import N
from turtle import right
from dataclasses import dataclass
# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.util import print_board, print_coordinate

# heuristic function
def man_distance(node, goal):
    return (abs(goal[0] - node[0]) +
           abs(goal[1] - node[1]))
 

# find neighbours that aren't blocked by blocks
def neighbours(pos, blocks, n):

    neighbours_list = []

    left_up = (pos[0]+ 1,pos[1] -1)
    if pos[0] < n and pos[1] > 0:
        if blocks[left_up] != "b":
            neighbours_list.append(left_up)

    right_up = (pos[0] +1, pos[1])
    if pos[0] < n:
        if blocks[right_up] != "b":
            neighbours_list.append(right_up)

    left = (pos[0], pos[1] -1)
    if pos[1] > 0:
        if blocks[left] != "b":
            neighbours_list.append(left)

    right = (pos[0], pos[1] +1)
    if pos[1] < n:
        if blocks[right] != "b":
            neighbours_list.append(right)

    left_btm = (pos[0]-1, pos[1])
    if pos[0] > 0:
        if blocks[left_btm] != "b":
            neighbours_list.append(left_btm)


    right_btm = (pos[0] -1, pos[1] +1)
    if pos[0] > 0 and pos[1] < n:
        if blocks[right_btm] != "b":
            neighbours_list.append(right_btm)

    return neighbours_list


'''# Implementing A* search # 

    begin with start node
        --> calculate the neighbours of the start node
        --> find the f cost using the manhattan distance heuristic
        --> add the lowest current to processed and remove from to_search
        --> remove neighbour duplicates from to_search
        --> if 2 nodes have the same f cost:
                        take the lowest h cost
                        
    return explored nodes: location and connected
    append start node to path:
        for each connected node in explored nodes:
                append to path
    
    return path'''

def a_star_search(start, goal, blocks, n):
    
    @dataclass
    class Node:
        location: tuple
        g: int
        h: int
        f: int
        connected: tuple
        
        def __init__(self, location, g, h, f, connected):
            self.location = location
            self.g = g
            self.h = h
            self.f = f
            self.connected = connected

    node = Node(start, 0, man_distance(start, goal), 0, None)
    to_search = [node]
    processed = []
    goal_state = False
    current = Node(node.location, node.g, node.h, node.f, node.connected)
    count = 0
    while(len(to_search) != 0 and not goal_state):
        neighbours_list = []
        neighbours_list = neighbours(current.location, blocks, n - 1)

        for neighbour in neighbours_list:
            
            location = neighbour
            g = current.g + 1
            h = man_distance(neighbour, goal)
            f = g + h
            connected = current.location
            tmp = Node(location, g, h, f, connected)
            duplicate = True
            for searched in to_search:
                if tmp.location == searched.location:
                    duplicate = False
                    if tmp.g < searched.g:
                        searched.g = tmp.g
                        searched.connected = tmp.connected
            if duplicate and tmp.location not in processed:
                to_search.append(tmp)
        processed.append(current)
        to_search.remove(current)
        min_f = sys.maxsize
        h_value = sys.maxsize
        for searched in to_search:
            if searched.f < min_f:
                min_f = searched.f
                h_value = searched.h
                current = searched
            elif searched.f == min_f:
                if searched.h < h_value:
                    h_value = searched.h
                    current = searched
            else:
                continue

        count += 1
        if current.location == goal:
            goal_state = True

    processed.append(current)
    path = []
    path.append(current.location)
    while current.connected != None:
        for node in processed:
            if node.location == current.connected:
                path.append(node.location)
                current = node
                break
    if len(to_search) == 0:
        return 0
    return path

def main():

    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)
    
    path = []
    start = tuple(data['start'])
    goal = tuple(data['goal'])
    n = data['n']
    blocks_dict = defaultdict(str)

    for b in data['board']:
        blocks_dict[tuple([b[1], b[2]])] = b[0]

    path = a_star_search(start, goal, blocks_dict, n)
    path.reverse()
    count = 0
    
    for p in path:
        count += 1
    print(count)
    for p in path:
        print(p)
    

    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).
