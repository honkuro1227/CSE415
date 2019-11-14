# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:36:10 2019

@author: fghjk
"""

'''Rubik2Cube.py
'''
#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Rubik2Cube"
PROBLEM_VERSION = "0.2"
PROBLEM_AUTHORS = ['Hung Lo']
PROBLEM_CREATION_DATE = "18-OCT-2019"
PROBLEM_DESC=\
'''This formulation of the Rubik2Cube uses generic
Python 3 constructs and has been tested with Python 3.6.
'''
#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
class State:
  def __init__(self, b):
      list_of_lists = b
      self.b = list_of_lists

  def __eq__(self,s2):
    for i in range(6):
      for j in range(4):
        if self.b[i][j] != s2.b[i][j]: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    txt = "\n["
    for i in range(6):
      txt += str(self.b[i])+"\n "
    return txt[:-2]+"]"

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    news.b = [row[:] for row in self.b]
    return news

  def can_move(self,dir):
    '''Tests whether it's legal to move a tile that is next
       to the void in the direction given.'''
    return True
    raise Exception("Illegal direction in can_move: "+str(dir))

  def move(self,dir):
    '''Assuming it's legal to make the move, this computes
       the new state resulting from moving a tile in the
       given direction, into the void.'''
    news = self.copy() # start with a deep copy.
    #(vi, vj) = self.find_void_location()
    b = news.b
   
    #'F','B','U','D','L','R
    if dir=='F': 
      c=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
      c[0][0]= b[0][2]
      c[0][1]= b[0][0]
      c[0][2]= b[0][3]
      c[0][3]= b[0][1]
      c[4][0]= b[1][0]
      c[4][2]= b[1][2]
      c[3][0]=b[4][0]
      c[3][2]=b[4][2]
      c[5][0]=b[3][0]
      c[5][2]=b[3][2]
      c[1][0]=b[5][0]
      c[1][2]=b[5][2]
      for i in range(len(b)):
          for j in range(len(b[i])):
              if c[i][j]==-1:
                  c[i][j]=b[i][j]
      news.b=c
      
    if dir=='B':
      c=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
      c[2][0]= b[2][2]
      c[2][1]= b[2][0]
      c[2][2]= b[2][3]
      c[2][3]= b[2][1]
      c[1][1]= b[5][1]
      c[1][3]= b[5][3]
      c[4][1]=b[1][1]
      c[4][3]=b[1][3]
      c[3][1]=b[4][1]
      c[3][3]=b[4][3]
      c[5][1]=b[3][1]
      c[5][3]=b[3][3]
      for i in range(len(b)):
          for j in range(len(b[i])):
              if c[i][j]==-1:
                  c[i][j]=b[i][j]
      news.b=c
    if dir=='U':
      c=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
      c[5][0]= b[5][2]
      c[5][1]= b[5][0]
      c[5][2]= b[5][3]
      c[5][3]= b[5][1]
      c[0][0]= b[1][0]
      c[0][1]= b[1][1]
      c[3][0]=b[0][0]
      c[3][1]=b[0][1]
      c[2][0]=b[3][0]
      c[2][1]=b[3][1]
      c[1][0]=b[2][0]
      c[1][1]=b[2][1]
      for i in range(len(b)):
          for j in range(len(b[i])):
              if c[i][j]==-1:
                  c[i][j]=b[i][j]
      news.b=c
    if dir=='D':
      c=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]  
      c[4][0]= b[4][2]
      c[4][1]= b[4][0]
      c[4][2]= b[4][3]
      c[4][3]= b[4][1]
      c[0][2]= b[1][2]
      c[0][3]= b[1][3]
      c[3][2]=b[0][2]
      c[3][3]=b[0][3]
      c[2][2]=b[3][2]
      c[2][3]=b[3][3]
      c[1][2]=b[2][2]
      c[1][3]=b[2][3]
      for i in range(len(b)):
          for j in range(len(b[i])):
              if c[i][j]==-1:
                  c[i][j]=b[i][j]
      news.b=c
    if dir=='R':
      c=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
      c[1][0]= b[1][2]
      c[1][1]= b[1][0]
      c[1][2]= b[1][3]
      c[1][3]= b[1][1]
      c[5][3]= b[0][1]
      c[5][2]= b[0][3]
      c[2][1]=b[5][3]
      c[2][3]=b[5][2]
      c[4][3]=b[2][1]
      c[4][2]=b[2][3]
      c[0][1]=b[4][3]
      c[0][3]=b[4][2]
      for i in range(len(b)):
          for j in range(len(b[i])):
              if c[i][j]==-1:
                  c[i][j]=b[i][j]
      news.b=c
    if dir=='L':
      c=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
      c[3][0]= b[3][2]
      c[3][1]= b[3][0]
      c[3][2]= b[3][3]
      c[3][3]= b[3][1]
      c[0][0]= b[4][1]
      c[0][2]= b[4][0]
      c[5][1]=b[0][0]
      c[5][0]=b[0][2]
      c[2][0]=b[5][1]
      c[2][2]=b[5][0]
      c[4][1]=b[2][0]
      c[4][0]=b[2][2]
      for i in range(len(b)):
          for j in range(len(b[i])):
              if c[i][j]==-1:
                  c[i][j]=b[i][j]
      news.b=c
    return news # return new state

  def edge_distance(self, s2):
    return 1.0  # Warning, this is only correct when
    # self and s2 are neighboring states.
    # We assume that is the case.  This method is
    # provided so that problems having all move costs equal to
    # don't have to be handled as a special case in the algorithms.
  
def goal_test(s):
  '''If all the b values are in order, then s is a goal state.'''
  return s == State([[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5]])

def goal_message(s):
  return "You've got all Cubics. Great!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
  # Use default, but override if new value supplied
             # by the user on the command line.
try:
  import sys
  init_state_string = sys.argv[2]
  print("Initial state as given on the command line: "+init_state_string)
  init_state_list = eval(init_state_string)
except:
  
  init_state_list = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5]]
  print("Using default initial state list: "+str(init_state_list))


CREATE_INITIAL_STATE = lambda: State(init_state_list)
#</INITIAL_STATE>

#<OPERATORS>
 #F (front), B (back), U (upper), D (down-side), L (left), R (right)
directions = ['F','B','U','D','L','R']
OPERATORS = [Operator("Move a tile "+str(dir)+" into the void",
                      lambda s,dir1=dir: s.can_move(dir1),
                      # The default value construct is needed
                      # here to capture the value of dir
                      # in each iteration of the list comp. iteration.
                      lambda s,dir1=dir: s.move(dir1) )
             for dir in directions]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)


    
