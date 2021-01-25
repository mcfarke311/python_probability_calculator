import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargumentsDict):
    self.contents = []
    for key, value in kwargumentsDict.items():
      self.contents += [f"{key}"] * value

  def draw(self, numBalls):
    if numBalls > len(self.contents):
      balls = copy.copy(self.contents)
      self.contents = []
      return balls
    balls = random.sample(self.contents, k = numBalls)
    for ball in balls:
      self.contents.remove(ball)
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_counter = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)
    for ballcolor, ballcount in expected_balls.items():
      if drawn.count(ballcolor) < ballcount:
        break
    else:
      success_counter += 1
  return success_counter / num_experiments