def rotated_binsearch(arr, key, left, right):
  mid = (left + right) // 2
  print(left,mid, right)
  print(arr[left], arr[mid], arr[right])
  print()
  
  if arr[mid] == key:
    return mid
  
  if left > right:
    return -1
  
  if arr[left] < arr[mid]: # left ordered
    if key < arr[mid] and key >= arr[left]:
      return rotated_binsearch(arr, key, left, mid - 1)
    else:
      return rotated_binsearch(arr, key, mid + 1, right)
  else: # right ordered
    if key > arr[mid] and key <= arr[right]:
      return rotated_binsearch(arr, key, mid + 1, right)
    else:
      return rotated_binsearch(arr, key, left, mid - 1)

# arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
# arr = [17, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14, 15, 16]
arr = [10, 14, 15, 16, 17, 19, 20, 25, 1, 3, 4, 5, 7]
print(rotated_binsearch(arr, key=25, left=0, right=len(arr)-1))
