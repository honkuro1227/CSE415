'''Farmer_Fox.py
by Hung Lo
UWNetID: honkuro
Student number: 1926128

Assignment 2, in CSE 415, Autumn 2019.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''
#</METADATA>
SOLUZION_VERSION = "2.0"
PROBLEM_NAME = "Farmer_Fox"
PROBLEM_VERSION = "2.0"
PROBLEM_AUTHORS = ['S. Tanimoto']
PROBLEM_CREATION_DATE = "07-JAN-2018"
#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
FF=0  # array index to access Farmer counts
F= 1  # same idea for Fox
G= 2# same idea for Grain
C= 3# same idea for Chiken
LEFT=0 # same idea for left side of river
RIGHT=1 # etc.

class State():

  def __init__(self, d=None):
    if d==None: 
      d = {'people':[[0,0],[0,0],[0,0],[0,0]],
           'boat':LEFT}
    self.d = d

  def __eq__(self,s2):
    for prop in ['people', 'boat']:
      if self.d[prop] != s2.d[prop]: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    p = self.d['people']
    txt = "\n Farmer on left:"+str(p[FF][LEFT])+"\n"
    txt += " Fox on left:"+str(p[F][LEFT])+"\n"
    txt += " Grain on left:"+str(p[G][LEFT])+"\n"
    txt += " Chicken on left:"+str(p[C][LEFT])+"\n"
    txt += " Farmer on right:"+str(p[FF][RIGHT])+"\n"
    txt += " Fox on right:"+str(p[F][RIGHT])+"\n"
    txt += " Grain on right:"+str(p[G][RIGHT])+"\n"
    txt += " Chicken on right:"+str(p[C][RIGHT])+"\n"
    
    side='left'
    if self.d['boat']==1: side='right'
    txt += " boat is on the "+side+".\n"
    return txt

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    news.d['people']=[self.d['people'][FF_or_F_or_C_G][:] for FF_or_F_or_C_G in [FF, F ,G,C]]
    news.d['boat'] = self.d['boat']
    return news 
#policy
  def can_move(self,ff,f,g,c):
    '''Tests whether it's legal to move the boat and take
     m missionaries and c cannibals.'''
    side = self.d['boat'] # Where the boat is.
    p = self.d['people']

    
    ff_now=p[FF][side]
    f_now=p[F][side]
    g_now=p[G][side]
    c_now=p[C][side]
    if(ff_now-ff<0):return False
    if(f_now-f<0):return False
    if(g_now-g<0):return False
    if(c_now-c<0):return False
    ff_arrive=p[FF][1-side]+ff
    f_arrive=p[F][1-side]+f
    g_arrive=p[G][1-side]+g
    c_arrive=p[C][1-side]+c
    if(ff_arrive>1): return False
    if(f_arrive>1):return False
    if(g_arrive>1):return False
    if(c_arrive>1):return False
    if(ff_arrive==1 and c_now-c==1 and f_now-f==1): return False
    if(ff_arrive==1 and c_now-c==1 and g_now-g==1): return False
    return True
#legal move
  def move(self,ff,f,g,c):
    '''Assuming it's legal to make the move, this computes
     the new state resulting from moving the boat carrying
     m missionaries and c cannibals.'''
    news = self.copy()            # start with a deep copy.
    side = self.d['boat']         # where is the boat?
    p = news.d['people']          # get the array of arrays of people.
    p[FF][side] = p[FF][side]-ff  # Remove people from the current side.
    p[F][side] = p[F][side]-f
    p[G][side] = p[G][side]-g
    p[C][side] = p[C][side]-c    
    p[FF][1-side] = p[FF][1-side]+ff   # Add them at the other side..
    p[F][1-side] = p[F][1-side]+f
    p[G][1-side] = p[G][1-side]+g
    p[C][1-side] = p[C][1-side]+c
    news.d['boat'] = 1-side       # Move the boat itself.
    return news
#test fir giak
def goal_test(s):
  '''If chiken ,fox ,farmer and grain are on the right, then s is a goal state.'''
  p = s.d['people']
  return (p[FF][RIGHT]==1 and p[F][RIGHT]==1 and p[G][RIGHT]==1 and p[C][RIGHT]==1 )

def goal_message(s):
  return "Congratulations on successfully transport goods and farmer across the river!"

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
CREATE_INITIAL_STATE = lambda : State(d={'people':[[1, 0], [1, 0],[1,0],[1,0]], 'boat':LEFT })

#</INITIAL_STATE>

#<OPERATORS>
Farmerandgoods = [(1,0,0,0),(1,1,0,0),(1,0,1,0),(1,0,0,1)]

OPERATORS = [Operator(
  (str(ff)+"Farmer cross the river with "+str(f)+"Fox  and "+str(g)+" Grain "+str(c)+" Chicken"),
  lambda s, ff1=ff, f1=f, g1=g,c1=c: s.can_move(ff1,f1,g1,c1),
  lambda s, ff1=ff, f1=f, g1=g,c1=c: s.move(ff1,f1,g1,c1)  
  ) 
  for (ff,f,g,c) in Farmerandgoods]
  
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>
