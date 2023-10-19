

class player:
  def play(self):
    print("The player is playing cricket\n")

class batsman(player):
  def play(self):
    print("Ther batsman is batting\n")

class bowler(player):
  def play(self):
    print("Ther batsman is bowling\n")

p = player()
b1 = batsman()
b2  = bowler()

p.play()
b1.play()
b2.play()

print("\nSayonera")
