## Graphs

1. swapLexOrder.py : Given a string str and array of pairs that indicates which indices in the string can be swapped, return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times. 
```
	Example
	For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
	swapLexOrder(str, pairs) = "dbca".
```

2. build_order.py : Given a list of modules with dependencies eg. `('a','b'), ('b','c'), etc` which represents a depends on b and b depends on c, construct an order in which all modules can be built without dependency conflicts.
