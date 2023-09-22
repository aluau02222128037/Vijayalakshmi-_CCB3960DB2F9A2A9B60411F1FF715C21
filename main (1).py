#Define the base class player
class Player:
  def play(self):
    print ("The player is playing cricket.")
    #Define the derived classs Batsman
class Batsman (Player):
  def play(self):
    print("The batsman is batting. ")
    #define the derived class  bowler
class Bowler(Player):
  def play(self):
    print("the bowler is bowling.")
    
batsman=Batsman()
bowler=Bowler()
player=Player()

batsman.play()
bowler.play()
player.play()





