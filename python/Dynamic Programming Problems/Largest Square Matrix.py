def maximalSquare(matrix):
    # agar matrix empty hai toh directly 0 return karo
    if not matrix or not matrix[0]:
        return 0
    # n = rows, m = columns
    n,m=len(matrix),len(matrix[0])
    # dp matrix banao jisme har cell initially 0 ho
    dp = [[0] * m for _ in range(n)]
    # max_side store karega largest square ka side length
    max_side = 0
    # --- Step 1: First column initialize karo ---
    for i in range(n):
        dp[i][0]=matrix[i][0]  # same as matrix ka first column
        max_side=max(max_side,dp[i][0])  # check max side
    # --- Step 2: First row initialize karo ---
    for j in range(m):
        dp[0][j]=matrix[0][j]  # same as matrix ka first row
        max_side=max(max_side,dp[0][j])
    # --- Step 3: Baaki cells ke liye formula apply karo ---
    for i in range(1,n):         # 1 se start kyunki 0th row/col already done
        for j in range(1,m):
            if matrix[i][j]==1:
                # agar current cell 1 hai toh
                # check karo left, top aur top-left cell me se minimum
                dp[i][j]=1+min(
                    dp[i-1][j],     # top cell
                    dp[i][j-1],     # left cell
                    dp[i-1][j-1]    # top-left cell
                )
                # update max_side agar bada square mil gaya ho
                max_side = max(max_side, dp[i][j])
            else:
                # agar cell 0 hai toh wahan koi square end nahi ho sakta
                dp[i][j] = 0

    # --- Step 4: area return karo (side^2) ---
    return max_side ** 2
matrix = [
  [0,1,1,0,1],
  [1,1,1,1,0],
  [0,1,1,1,0],
  [1,1,1,1,1],
  [1,1,1,1,0]
]
print(maximalSquare(matrix))  # Output: 9
