## Sorting and Searching

1. sorted_matrix_search.py : Given an M x N matrix in which each row and each column is sorted in ascending order, write a method to find an element.

2. magic_index.py : A magic index in an array `A[0...n-1]` is defined to be an index such that `A[i]= i`. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

3. rank_from_stream.py : Imagine you are reading in a stream of integers. Periodically, you wish to be able to lookup the rank of a numberx (the number of values less than or equal to x). lmplementthe data structures and algorithms to support these operations. That is, implement the method track ( int x), which is called when each number is generated, and the method getRankOfNumber(int x), which returns the number of values less than or equal to x (not including x itself). 
```
      EXAMPLE
      Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
      getRankOfNumber(l) 0
      getRankOfNumber(3) = 1
      getRankOfNumber(4) 3
```

4. merge_sorted.py : Merge two sorted arrays in place. The 1st array has extra space for accomodating the 2nd array.

5. rotated_binsearch.py : An element in a sorted array can be found in O(log n) time via binary search. But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array in O(log n) time.
