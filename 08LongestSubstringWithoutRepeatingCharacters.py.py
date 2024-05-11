class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
      # sliding window 
      indexMap= {}
      windowPonterLeft = 0
      maxLen = 0

      for index in range(len(s)):
        if s[index] in indexMap:
            windowPonterLeft = max(indexMap[s[index]] + 1, windowPonterLeft)
        indexMap[s[index]] = index
        maxLen = max(maxLen,index - windowPonterLeft + 1)
      return maxLen
