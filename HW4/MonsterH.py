# -*- coding: utf-8 -*-
'''EightPuzzleWithHamming.py
by Hung Lo
UWNetID: honkuro
Student number: 1926128

Assignment 3, in CSE 415, Autumn 2019.
 
This file contains my problem formulation for the problem of
EightPuzzleWithHamming.py
'''
from Monster import *
def h(s):
  '''We return an estimate of mistake tilts
  between s and the goal state.'''

  current_state = s  #  current state
  different=min([abs(current_state.b[0]-3), 
                 abs(current_state.b[1]+3),
                 abs(current_state.b[2]-0)]
    )
  return different

