# -*- coding: utf-8 -*-
'''EightPuzzleWithHamming.py
by Hung Lo
UWNetID: honkuro
Student number: 1926128

Assignment 3, in CSE 415, Autumn 2019.
 
This file contains my problem formulation for the problem of
EightPuzzleWithHamming.py
'''
from Rubik2Cube import *

Hamming =[[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5]]

def h(s):
  '''We return an estimate of mistake tilts
  between s and the goal state.'''

  current_state = s  #  current state
  different=24   #hamming: how many tilt to goal state
  for i in range(len(current_state.b)):
      for j in range(len(current_state.b[i])):
          if current_state.b[i][j]==Hamming[i][j]:
              different=different-1
  return different
