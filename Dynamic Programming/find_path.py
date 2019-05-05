def find_path(grid):
  path = []
  failed = set()

  def _find_path(r, c):
    if r < 0 or c < 0 or grid[r][c] == 1:
      return False
    
    elif (r, c) in failed:
      return False
    
    elif r == 0 and c == 0:
      return True
    
    elif _find_path(r, c-1) or _find_path(r-1, c):
      path.append((r, c))
      return True
    else:
      failed.add((r, c))
      return False
  
  _find_path(len(grid) - 1, len(grid[0]) - 1)
  return path

grid = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 0, 0],
  [0, 1, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0]
]

print(find_path(grid))
