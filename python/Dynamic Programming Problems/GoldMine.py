def gold(mine):
    # Get dimensions of the mine
    n, m = len(mine), len(mine[0])

    # Create a DP matrix with dimensions n x m, initialized with 0
    dp = [[0] * m for i in range(n)]

    # Initialize the first row with values from the first row of the mine
    for j in range(m):
        dp[0][j] = mine[0][j]

    # Fill the DP matrix from the second row to the last row
    for i in range(1, n):
      for j in range(m):
          # Check if top-left diagonal cell is within bounds
          if (j - 1) >= 0:
              top_left = dp[i - 1][j - 1]
          else:
              top_left = 0

          # Get the value from the top cell directly above
          top = dp[i - 1][j]

          # Check if top-right diagonal cell is within bounds
          if (j + 1) < m:
              top_right = dp[i - 1][j + 1]
          else:
              top_right = 0

          # Update dp[i][j] by adding the current cell value and the maximum gold possible from the previous row
          dp[i][j] = mine[i][j] + max(top_left, top, top_right)


    # The answer will be the maximum value in the last row of dp
    return max(dp[n - 1])


mine = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]
]
print(gold(mine))

