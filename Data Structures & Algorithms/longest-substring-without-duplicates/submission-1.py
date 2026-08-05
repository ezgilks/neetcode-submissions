class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() #seen chars
        l = 0 #left edge of window
        res = 0
        for r in range(len(s)): #right edge slides through
            while s[r] in charSet: 
                #shrink window from left when dup
                charSet.remove(s[l]) 
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1) #keep track of biggest

        return res


        