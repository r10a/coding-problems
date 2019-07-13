# Find build order for related projects
class queue:

  def __init__(self):
    self.arr = []
  
  def enq(self, val):
    self.arr.append(val)
  
  def deq(self):
    return self.arr.pop(0)
  
  def printq(self):
    for i in self.arr:
      print(i, end=" ")
    print()
  
  def is_empty(self):
    return len(self.arr) == 0

class graph:

  def __init__(self, vertices):
    self.adj_list = {}
    self.incoming = {}
    for v in vertices:
      self.adj_list[v] = []
      self.incoming[v] = 0
    

  def add_edge(self, a, b):
    self.incoming[b] += 1
    self.adj_list[a].append(b)

def build_order(vertices, arr):
  g = graph(vertices)
  for s, e in arr:
    g.add_edge(s, e)
  print(g.adj_list)
  print(g.incoming)

  built = set() # init built
  q = queue()
  for k, v in g.incoming.items():
    if k in built:
      continue
    if v == 0:
      built.add(k)
      print(k, end=" ")
      for k in g.adj_list[k]:
        q.enq(k)
  
  while not q.is_empty():
    v = q.deq()
    if v in built:
      continue
    for j in g.adj_list[v]:
      q.enq(j)
    built.add(v)
    print(v, end=" ")
  print()

vertices = ['a', 'b', 'c', 'd', 'e', 'f']
arr = [('a','d'), ('f','b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
build_order(vertices, arr)
