#Link ->  https://leetcode.com/problems/distinct-subsequences/


class Solution(object):
    def numDistinct(self, s, t):
        m = len(s)  # Length of the source string s
        n = len(t)  # Length of the target string t

        # Step 1: Create a 2D dp table of size (m+1) x (n+1) filled with 0
        dp = []
        for i in range(m + 1):
            l = []
            for j in range(n + 1):
                l.append(0)
            dp.append(l)

        # Step 2: Initialize the first column (dp[i][0] = 1 for all i)
        # Reason: An empty string t ("") can be matched with any prefix of s in exactly one way (by deleting all characters)
        for i in range(m + 1):
            dp[i][0] = 1

        # Step 3: Fill the dp table
        for i in range(1, m + 1):  # Loop over each character in s
            for j in range(1, n + 1):  # Loop over each character in t
                if s[i - 1] == t[j - 1]:
                    # If characters match:
                    # 1. Use this character (dp[i-1][j-1])
                    # 2. Or skip this character in s (dp[i-1][j])
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # If characters don't match:
                    # Only option is to skip this character in s
                    dp[i][j] = dp[i - 1][j]

        # Step 4: The answer is in dp[m][n] (all of s, all of t)
        return dp[m][n]

        
