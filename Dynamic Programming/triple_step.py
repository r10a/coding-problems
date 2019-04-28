def triple_step(n):
  dp = {} # memoized table
  
  def _triple_step(n): # inner recursive function
    if n < 0:
      return 0
    elif n == 0:
      return 1
    elif n in dp: # check if result is already present or not in memoized table
      return dp[n]
    else:
      dp[n] = _triple_step(n - 1) + _triple_step(n - 2) + _triple_step(n - 3) # if not present, calculate value
      return dp[n] # return calculated value after storing in table
  
  return _triple_step(n) # call recursive inner function

print(triple_step(25))
