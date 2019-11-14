# -*- coding: utf-8 -*-
'''EightPuzzleWithManhattan.py
by Hung Lo
UWNetID: honkuro
Student number: 1926128

Assignment 3, in CSE 415, Autumn 2019.
 
This file contains my problem formulation for the problem of
EightPuzzleWithManhattan.py
'''
from EightPuzzle import *

Manhattan = {'0':[0,0],'1':[0,1],'2':[0,2],
             '3':[1,0],'4':[1,1],'5':[1,2],
             '6':[2,0],'7':[2,1],'8':[2,2]}

def h(s):
  '''We return an estimate of mistake tiles
  between s and the goal state.'''

  current_state = s  #  current state
  different=0   #Manhattan: the sum of total step tiles need for goal state
  for i in range(len(current_state.b)):
      for j in range(len(current_state.b[i])):
          different=different+abs(Manhattan[str(current_state.b[i][j])][0]-i)+abs(Manhattan[str(current_state.b[i][j])][1]-j)
  return different

