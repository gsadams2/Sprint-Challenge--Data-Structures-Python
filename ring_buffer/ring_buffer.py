class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:
      self.storage[self.current] = item
      self.current += 1 
     
    if self.current == self.capacity:
      self.current = 0

  def get(self):
    arr_yo = []

    for i in self.storage:
      if i:
        arr_yo.append(i)
    return arr_yo
