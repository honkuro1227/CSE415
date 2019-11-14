'''honkuro_TTS_agent.py
A bare-bones agent that plays Toro-Tile Straight,
but rather poorly.

To create your own agent, make a copy of this file, using
the naming convention YourUWNetID_TTS_agent.py.

If you need to import additional custom modules, use
a similar naming convention... e.g.,
'''

import time
from random import choice
from TTS_State import TTS_State
K=0
USE_BASIC_STATIC_EVAL =False
currentstate=None
maxply=1
ALPHABETA=True
TIMED=False
H=0 #= len(board) # height of board = num. of rows
W=0 #= len(board[0]) # width of board = num. of cols.
DATA = {}
DATA['CURRENT_STATE_STATIC_VAL'] = -1000.0
DATA['N_STATES_EXPANDED'] = 0
DATA['N_STATIC_EVALS'] = 0
DATA['N_CUTOFFS'] = 0

QUOTES = ["I am ready","I will kill u","Now is time to show my truely power","Good trying ","Interested"]


plusDirections  = [(0,1),(1,1),(1,0),(-1,1)] # E, NE, N, NW
minusDirections = [(0,-1),(-1,-1),(-1,0),(1,-1)] # W, SW, S, SE

#use_custom_static_eval_function=False

class MY_TTS_State(TTS_State):
  def static_eval(self):
    if USE_BASIC_STATIC_EVAL:
      return self.basic_static_eval()
    else:
      return self.custom_static_eval()

  def basic_static_eval(self):
      TBF=0
      TWF=0
      board= self.board
      H = len(board) # height of board = num. of rows
      W = len(board[0]) # width of board = num. of cols.
      plusDirections  = [(0,1),(1,1),(1,0),(-1,1),(0,-1),(-1,-1),(-1,0),(1,-1)] # E, NE, N, NW
      #minusDirections = [] # W, SW, S, SE
      for j in range(W):
          for i in range(H):
              if board[i][j]=='W':
                  count=8
                  for di in range(8):              
                      dp = plusDirections[di]                    
                      wa=i
                      wb=j
                      wa += dp[0]
                      if wa < 0 or wa >= H: wa = ((wa + H) % H) # toroidal wrap
                      wb += dp[1]
                      if wb < 0 or wb >= W: wb = ((wb + W) % W) 
                      if board[wa][wb] != ' ':
                          count-=1
                  TWF+=count
              if board[i][j]=='B':
                  count=8
                  for di in range(8):              
                      dp = plusDirections[di]                    
                      wa=i
                      wb=j
                      wa += dp[0]
                      if wa < 0 or wa >= H: wa = ((wa + H) % H) # toroidal wrap
                      wb += dp[1]
                      if wb < 0 or wb >= W: wb = ((wb + W) % W) 
                      if board[wa][wb] != ' ':
                          count-=1
                  TBF+=count
      value=TWF - TBF
      return  value

  def custom_static_eval(self):
      return isGoal(self)
    #return 2
  def getNumAgents(self):
      return 2
#def parameterized_minimax(
#       current_state=None,
#       max_ply=2,
#       alpha_beta=False, 
#       use_custom_static_eval_function=False):
    
    
def get_ready(initial_state, k, who_i_play, player2Nickname):
    # do any prep, like eval pre-calculation, here.
    global USE_BASIC_STATIC_EVAL, K,currentstate, H, W
    USE_BASIC_STATIC_EVAL==False
    currentstate=initial_state
    K=k
    H = len(currentstate.board) # height of board = num. of rows
    W = len(currentstate.board[0]) # width of board = num. of cols.
    return "I am ready"


      
# The following is a skeleton for the function called parameterized_minimax,
# which should be a top-level function in each agent file.
# A tester or an autograder may do something like
# import ABC_TTS_agent as player, call get_ready(),
# and then it will be able to call tryout using something like this:
# results = player.parameterized_minimax(**kwargs)

def parameterized_minimax(current_state=None,max_ply=2,use_alpha_beta=False, use_basic_static_eval=False):
    global DATA, USE_BASIC_STATIC_EVAL , maxply, ALPHABETA

    DATA['CURRENT_STATE_STATIC_VAL'] = -1000.0
    DATA['N_STATES_EXPANDED'] = 0
    DATA['N_STATIC_EVALS'] = 0
    DATA['N_CUTOFFS'] = 0
    state = MY_TTS_State(current_state.board)
    USE_BASIC_STATIC_EVAL = use_basic_static_eval
    maxply=max_ply
    ALPHABETA=use_alpha_beta
    #state=current_state

    if(ALPHABETA):
        alphabeta(state, state.whose_turn ,max_ply)
    else:
        minimax(state, state.whose_turn ,max_ply)

    return DATA
    

  # All students, add code to replace these default
  # values with correct values from your agent (either here or below).

  
  #if alpha_beta:
  #if use_custom_static_eval_function:
  # STUDENTS: You may create the rest of the body of this function here.

  # Actually return all results...
#  return(DATA)
  

  

   
    

def take_turn(current_state, last_utterance, time_limit):
    global DATA, TIMED, maxply, H, W, QUOTES

    # Compute the new state for a move.
    # Start by copying the current state.

    new_state = MY_TTS_State(current_state.board)

    H = len(new_state.board) # height of board = num. of rows
    W = len(new_state.board[0])
#    DATA['CURRENT_STATE_STATIC_VAL'] = new_state.static_eval()
#    return
    who = current_state.whose_turn
    if(time_limit!=0):

        TIMED=True
        start_time = time.time()
    new_who = 'B'  
    if who=='B': new_who = 'W'  
    legalActions = getLegalActions(new_state)
    bestaction = []
    if who=='W':
        score = -(float("inf"))
        for action in legalActions:
            nextState = generateSuccessor(current_state ,who , action)
            prevscore = score
            if (ALPHABETA):
                if(TIMED):
                    score = max(score, alphabeta(nextState, who, maxply, start_time,time_limit))
                else:
                    score = max(score, alphabeta(nextState, who, maxply))
                if score > prevscore:
                    bestaction = action
            else:
                if(TIMED):
                    score = max(score, minimax(nextState, who, maxply,start_time,time_limit))
                else:
                    score = max(score, minimax(nextState, who, maxply))
                if score > prevscore:
                    bestaction = action
    else:
        score = float("inf")
        for action in legalActions:
            nextState = generateSuccessor(current_state ,who , action)
            prevscore = score
            if (ALPHABETA):
                if(TIMED):
                    score = min(score, alphabeta(nextState, who, maxply, start_time,time_limit))
                else:
                    score = min(score, alphabeta(nextState, who, maxply))
                if score < prevscore:
                    bestaction = action
            else:
                if(TIMED):
                    score = min(score, minimax(nextState, who, maxply,start_time,time_limit))
                else:
                    score = min(score, minimax(nextState, who, maxply))
                if score < prevscore:
                    bestaction = action

    new_state.whose_turn = new_who
    # Place a new tile
    location = bestaction

    if location==False: return [[False, current_state], "I don't have any moves!"]
    new_state.board[location[0]][location[1]] = who

    # Construct a representation of the move that goes from the
    # currentState to the newState.
    move = location

    # Make up a new remark
    new_utterance = choice(QUOTES)
  
    return [[move, new_state], new_utterance]

def _find_next_vacancy(b):
    for i in range(len(b)):
      for j in range(len(b[0])):
        if b[i][j]==' ': return (i,j)
    return False

def moniker():
    return "Honkuro" # Return your agent's short nickname here.

def who_am_i():
    return """My name is honkuro, created by HungLo. version Terminator"""
    
def minimax(state, whoseMove, plyLeft, start_time=None, time_limit=None): #return the best-choice move, 
    global DATA, TIMED
    legalmoves=getLegalActions(state)
    if plyLeft==0 or len(legalmoves)==0:#bottom or get_win(state, 5)!='No win'
        DATA['CURRENT_STATE_STATIC_VAL'] = state.static_eval()
        return state.static_eval()
    if TIMED:
        if (start_time!=None):
            if (time.time() - start_time) >= time_limit * 0.7:
                DATA['CURRENT_STATE_STATIC_VAL'] = state.static_eval()
                return state.static_eval()
    if whoseMove=='W':
        provisional = float("-inf")
    else:
        provisional = float("inf")
    DATA['N_STATES_EXPANDED']+=1
    for action in legalmoves:
        new_state=generateSuccessor(state, whoseMove, action)
        new_val=minimax(new_state,new_state.whose_turn,plyLeft-1)
        if whoseMove=='W' and new_val>provisional:
            provisional=new_val
        if whoseMove=='B' and new_val<provisional:
            provisional=new_val
    return provisional

    


def alphabeta(state, whoseMove ,plyLeft ,alpha=float("-inf"),beta=float("inf"),start_time=None,time_limit=None):
    global DATA, K ,TIMED
    legalmoves=getLegalActions(state)
    if plyLeft==0 or len(legalmoves)==0 :
        DATA['N_STATIC_EVALS'] += 1
        DATA['CURRENT_STATE_STATIC_VAL']=state.basic_static_eval()
        return state.static_eval()
    if TIMED:
        if (start_time!=None):
            if (time.time() - start_time) >= time_limit * 0.7:
                DATA['CURRENT_STATE_STATIC_VAL'] = state.static_eval()
                return state.static_eval()
    if  whoseMove == 'W':
        bestScore=float("-inf")
        DATA['N_STATES_EXPANDED']+=1
        for action in legalmoves: 

            new_state =generateSuccessor(state,whoseMove, action)
            bestScore =max(bestScore, alphabeta(new_state,new_state.whose_turn,plyLeft-1,alpha,beta))
            alpha= max(alpha, bestScore)
            if(alpha>=beta):
                DATA['N_CUTOFFS']+=1
                break
        return bestScore
    else :
        bestScore=float("inf")
        DATA['N_STATES_EXPANDED']+=1
        for action in legalmoves:

            new_state =generateSuccessor(state,whoseMove, action)
            bestScore =min(bestScore, alphabeta(new_state,new_state.whose_turn,plyLeft-1,alpha,beta))
            beta= min(beta, bestScore)
            if(alpha>=beta):
                DATA['N_CUTOFFS']+=1
                break
        return bestScore    
        

def isGoal(state): 
    global K, plusDirections, minusDirections 
    board = state.board
    #moveI, moveJ = move
    H = len(board) # height of board = num. of rows
    W = len(board[0]) # width of board = num. of cols.

    total_val=0
    for ic in range(H):
        for jc in range(W):
            tmp=[]
            whoWent = board[ic][jc]

            for di in range(4):
                dp = plusDirections[di]
                dm = minusDirections[di]
                # count number of Ws (or Bs) in plusDirection:
                count = 1
                i = ic
                j = jc
                #boundary check:

                for step in range(K-1):
                    i += dp[0]
                    if i < 0 or i >= H: i = ((i + H) % H) # toroidal wrap
                    j += dp[1]
                    if j < 0 or j >= W: j = ((j + W) % W) # toroidal wrap
                    if board[i][j] != whoWent:

                        break # the run ends.
                    count += 1

                i = ic
                j = jc
                for step in range(K-1):
                    i += dm[0]
                    if i < 0 or i >= H: i = ((i + H) % H) # toroidal wrap
                    j += dm[1]
                    if j < 0 or j >= W: j = ((j + W) % W) # toroidal wrap
                    tmp.append(board[i][j])
                    if board[i][j] != whoWent:

                        break # the run ends.
                    count += 1
                    if count==K: break


                for kval in range(count):
                    if whoWent=='W':
                        total_val+=pow(10,kval)#*(2-counter)
                    if whoWent=='B':
                        total_val-=pow(10,kval)#*(2-counter)   
                if count>=K:
                    if whoWent=='W':
                        total_val+=100000
                    if whoWent=='B':
                        total_val-=100000
    return total_val



def getLegalActions(state):
    re=[]
    b=state.board
    for i in range(len(b)):
      for j in range(len(b[0])):
          if b[i][j]!=' ':
              continue;
          else:
              re.append((i,j))
    return re

def generateSuccessor(current_state,who,move):
    new_state = MY_TTS_State(current_state.board)
    new_who = 'B'  
    if who=='B': new_who = 'W'  
    new_state.board[move[0]][move[1]] = who
    new_state.whose_turn = new_who
    return new_state