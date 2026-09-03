"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.


Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(t):
         return False

        set1 = set(s)
        set2 = set(t)

        if set1 == set2:
            for l in set1:
                if s.count(l) != t.count(l):
                    return False
        elif set1 != set2:
            return False
            
        return True