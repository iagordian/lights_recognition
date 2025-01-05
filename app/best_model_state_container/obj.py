
from typing import Optional

class BestModelStateContainer:

  def __init__(self, start_score: Optional[float] = 0.0):
    self.score = start_score
    self.best_model_state = None
    self.new_best_state = False

  def __setitem__(self, score: float, model_state: dict):

    if score > self.score:
      self.score = score
      self.new_best_state = True
      self.best_model_state = model_state

    else:
      self.new_best_state = False

    if self.new_best_state:
      print('Найдено новое лучшее состояние!')