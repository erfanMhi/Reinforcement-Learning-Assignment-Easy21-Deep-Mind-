import  numpy  as  np
from copy import deepcopy

class State:
    def __init__(self, dealer_card,  pl_sum, is_terminal=False):
        self.dealer_card = dealer_card
        self.pl_sum = pl_sum
        self.is_terminal = is_terminal
    
    def pl_dealer_reward(self):
        if self.dealer_card == self.pl_sum:
            return  0
        elif self.dealer_card < self.pl_sum:
            return  1
        else:
            return  -1
    def __repr__(self):
        return "dealer score: {}, player_score: {}, is_terminal: {}".format(self.dealer_card, self.pl_sum, self.is_terminal)
    def __str__(self):
        return "dealer score: {}, player_score: {}, is_terminal: {}".format(self.dealer_card, self.pl_sum, self.is_terminal)

class Environment(object):
  
    def __init__(self):
        self.state = State(np.random.randint(1,11),  np.random.randint(1,11))
    
    def  reinitialize(self):
        """[Easy21  game  start]
        Returns:
            cards  {[(int,  int)]}  --  [Randomly  generated  first  cards  for  player  and  dealer]
        """
        self.state  =  State(np.random.randint(1,11),  np.random.randint(1,11))
        return self.state

    def  _take_card(self,  s):
        if np.random.rand()  >  1/3:
            return np.random.randint(1,11)
        else:
            return -np.random.randint(1,11)
    
    def  _step(self,  a,  s):
        """[Easy21  game  step]
        
        Arguments:
            a  {[string]}  --  ['hit'  or  'stick']
            s  {[State]}  --  [player's  first  card,  and  player  sums]    

        Returns:
            s_p  {[State]}  --  [next  state]
        """
        r  =  0

        assert  a  in  ['hit',  'stick']
        assert  type(s)  is  State
        
        if  a  ==  'hit':
            card_score  =  self._take_card(s)
            s_p  =  State(s.dealer_card,  s.pl_sum  +  card_score)
            if  not  (1  <  s_p.pl_sum  <  22):
                r  =  -1
                s_p.is_terminal = True
        else:
            s_p = deepcopy(s)
            s.is_terminal = True
            while  s_p.dealer_card  <  17:
                s_p.dealer_card  +=  np.random.randint(1,11)
            if  (not  (1  <  s_p.dealer_card  <  22)) :
                r  =  1
            else:
                r = s_p.pl_dealer_reward()
                
                
        return  s_p,  r

    def next(self, a):
        self.state,  r  =  self._step(a,  self.state)
        return  self.state,  r