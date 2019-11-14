'''EightPuzzle.py
'''
#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Eight Puzzle"
PROBLEM_VERSION = "0.2"
PROBLEM_AUTHORS = ['S. Tanimoto']
PROBLEM_CREATION_DATE = "18-OCT-2019"
PROBLEM_DESC=\
'''This formulation of the Eight Puzzle uses generic
Python 3 constructs and has been tested with Python 3.6.
It is designed to work according to the QUIET2 tools interface.
'''
#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
class State:
  def __init__(self, b=None):
      if b==None: 
          b=[0,0,0]
      self.b = b
      
  def __eq__(self,s2):
    for i in range(3):
        if self.b != s2.b: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    txt = "\n["
    for i in range(3):
      txt += str(self.b[i])+","
    return txt[:-1]+"]"

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    news.b = [row for row in self.b]
    return news

  def find_void_location(self):
    '''Return the (vi, vj) coordinates of the void.
    vi is the row index of the void, and vj is its column index.'''


  def can_move(self,dir):
    '''Tests whether it's legal to move a tile that is next
       to the void in the direction given.'''
       
    if (any(x>3 for x in self.move(dir).b) or any(x<-3 for x in self.move(dir).b)   ):
        return False
    if self.b==[2,-1,-1]:
        if (self.move(dir).b==[3,-1,-2] or self.move(dir).b==[3,-2,-1] ):
            return False
    if self.b==[1,-1,0]:
        if (self.move(dir).b==[2,-2,0] or self.move(dir).b==[1,-2,1] ):
            return False
    if self.b==[2,-2,0]:
        if (self.move(dir).b==[3,-3,0] or self.move(dir).b==[3,-2,-1] ):
            return False        
    return True

  def move(self,dir):
    '''Assuming it's legal to make the move, this computes
       the new state resulting from moving a tile in the
       given direction, into the void.'''
    news = self.copy() # start with a deep copy.
    b = news.b
    if dir=='0': 
      b[0] = b[0]-1
      b[1] = b[1]+1
    if dir=='1':
      b[2] = b[2]-1
      b[1] = b[1]+1
    if dir=='2':
      b[2] = b[2]-1
      b[0] = b[0]+1
    if dir=='3':
      b[1] = b[1]-1
      b[0] = b[0]+1
    if dir=='4':
      b[1] = b[1]-1
      b[2] = b[2]+1
    if dir=='5':
      b[0] = b[0]-1
      b[2] = b[2]+1
    return news # return new state

  def edge_distance(self, s2):
      dis=abs(self.b[0]-s2.b[0])+2*abs(self.b[1]-s2.b[1])+4*abs(self.b[2]-s2.b[2])
      return dis 
  
def goal_test(s):
  '''If all the b values are in order, then s is a goal state.'''
  return s.b == [3,-3,0]

def goal_message(s):
  return "You've got all eight straight. Great!"

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
  init_state_list = [0,0,0]
  print("Using default initial state list: "+str(init_state_list))
  print(" (To use a specific initial state, enter it on the command line, e.g.,")
  print("python3 UCS.py EightPuzzle '[[3, 1, 2], [0, 4, 5], [6, 7, 8]]'")

CREATE_INITIAL_STATE = lambda: State(init_state_list)
#</INITIAL_STATE>

#<OPERATORS>
directions = ['0','1','2','3','4','5']
OPERATORS = [Operator("Monster move "+str(dir)+" into",
                      lambda s,dir1=dir: s.can_move(dir1),
                      lambda s,dir1=dir: s.move(dir1) )
             for dir in directions]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

