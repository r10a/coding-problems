def sorted_matrix_binsearch(arr, key):

  def get_index(arr, idx):
    col = len(arr[0])
    x = idx // col
    y = idx % col
    return arr[x][y]
  
  def binsearch(arr, left, right, key):
    mid = (left + right) // 2
    mid_val = get_index(arr, mid)

    if left > right:
      return -1
    
    if mid_val == key:
      return mid_val
    
    if key < mid_val:
      return binsearch(arr, left, mid - 1, key)
    else:
      return binsearch(arr, mid + 1, right, key)
  
  length = len(arr) * len(arr[0]) - 1
  return binsearch(arr, 0, length, key)


arr = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(sorted_matrix_binsearch(arr, 6))
