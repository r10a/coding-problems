def magic_index(arr):
  def _magic_index(l, r):
    mid = (l + r) // 2
    if mid == arr[mid]:
      return mid
    elif l > r:
      return -1
    elif mid > arr[mid]:
      return _magic_index(mid + 1, r)
    else:
      return _magic_index(l, mid - 1)
  
  return _magic_index(0, len(arr) - 1)

def magic_index_repeats(arr):
  def _magic_index(l, r):
    mid = (l + r) // 2
    if mid == arr[mid]:
      return mid
    elif l > r:
      return -1
    right = _magic_index(mid + 1, r)
    if right == -1:
      return _magic_index(l, mid - 1)
    else:
      return right
  
  return _magic_index(0, len(arr) - 1)

arr = [-1, 0, 1, 2, 4, 6, 8, 10]
print(magic_index(arr))

arr = [-1, 0, 1, 4, 4, 4, 8, 10]
print(magic_index_repeats(arr))
