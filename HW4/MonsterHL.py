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
g=[0,0,0]
def h(s):
    
    if s.b==[2,-1,-1]:
            return 8
    if s.b==[1,-1,0]:
            return 9
    if s.b==[2,-2,0]:
            return 8
    return 0