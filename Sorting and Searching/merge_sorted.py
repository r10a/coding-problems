def merge(arr1, arr2):
  len1 = 0
  while arr1[len1 + 1] is not None:
    len1 += 1
  i, j, k = len1, (len(arr2) - 1), (len(arr1) - 1)
  print(i, j, k)
  while i >= 0 and j >= 0:
    num = 0
    if arr2[j] > arr1[i]:
      num = arr2[j]
      j -= 1
    else:
      num = arr1[i]
      i -= 1
    arr1[k] = num
    k -= 1
  return arr1

arr1 = [1, 3, 5, 7, 9, 11, None, None, None, None, None]
arr2 = [0, 2, 4, 6, 8, 10]
print(merge(arr1, arr2))
