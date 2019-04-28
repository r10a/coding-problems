def triple_step(n):
  dp = {}
  def _triple_step(n):
    if n < 0:
      return 0
    elif n == 0:
      return 1
    elif n in dp:
      return dp[n]
    else:
      dp[n] = _triple_step(n - 1) + _triple_step(n - 2) + _triple_step(n - 3)
      return dp[n]
  
  return _triple_step(n)

print(triple_step(25))
