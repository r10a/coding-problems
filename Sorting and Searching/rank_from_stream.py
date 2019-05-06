class treenode:

  def __init__(self, val, rank):
    self.value = val
    self.left = None
    self.right = None
    self.rank = rank

class bst_tracker:

  def __init__(self):
    self.root = treenode(None, 0)
  
  def inorder(self):
    def _inorder(root):
      if root:
        _inorder(root.left)
        print(root.value, root.rank)
        _inorder(root.right)
    
    _inorder(self.root)
  
  def get_rank_of_number(self, val):
    
    def _get_rank_of_number(root, val):
      if root:
        if val == root.value:
          if root.right and root.right.value == val:
              return _get_rank_of_number(root.right, val)
          return root.rank
        elif val >= root.value:
          return _get_rank_of_number(root.right, val)
        else:
          return _get_rank_of_number(root.left, val)
      return "Number not in stream"
    
    return _get_rank_of_number(self.root, val)

  def track(self, val):
    if not self.root.value:
      self.root.value = val
      return
    
    def _update_rank(root):
      if root:
        root.rank += 1
        _update_rank(root.left)
        _update_rank(root.right)

    def _track(root, val):
      if val == root.value:
        root.rank += 1
        _update_rank(root.right)
      elif val > root.value:
        if root.right:
          _track(root.right, val)
        else:
          root.right = treenode(val, root.rank + 1)
      else:
        root.rank += 1
        _update_rank(root.right)
        if root.left:
          _track(root.left, val)
        else:
          root.left = treenode(val, root.rank - 1)
    
    _track(self.root, val)

bst = bst_tracker()

def stream():
  for i in [5, 1, 4, 4, 5, 9, 7, 13, 3]:
    yield i

for i in stream():
  bst.track(i)

# bst.inorder()
print(bst.get_rank_of_number(4))
