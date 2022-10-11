from RPSLS_player import RPSLS_player
import random

class P18457(RPSLS_player):
  def __init__(self):
    pass
    #mylist = ["rock", "paper", "scissors", "lizard", "spock"]

  def shoot(self):
    mylist = ["rock", "paper", "scissors", "lizard", "spock"]
    a = random.randint(0,4)
    return mylist[a]
  
  def update(self, result: str, competitor_shot: str):
    pass