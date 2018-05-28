# 8_puzzle
# Overview
Solving 8 puzzle game using A* seacrh. Two different heuristics are implemeted here.

1. Number of misplaced tiles
2. Manhatten distance

Sample input 

    _goal_state = [[1,2,3],
                   [8,0,4],
                   [7,6,5]]
    problem  =    [[2,8,3],
                   [1,6,4],
                   [7,5,0]]
                   
Change the \_goal_state and problem accrodingly.

Sample output

```
Move1 
[[2 8 3]
 [1 6 4]
 [7 0 5]]
Move2
[[2 8 3]
 [1 0 4]
 [7 6 5]]
Move3
[[2 0 3]
 [1 8 4]
 [7 6 5]]
Move4
[[0 2 3]
 [1 8 4]
 [7 6 5]]
Move5
[[1 2 3]
 [0 8 4]
 [7 6 5]]
Move6
[[1 2 3]
 [8 0 4]
 [7 6 5]]

```

# Installing

```
git clone https://github.com/tomherren/pnl-service 
cd 8_puzzle 
pip install numpy
pip install copy
```
# Running Locally
```
python 8_puzzle.py
```
