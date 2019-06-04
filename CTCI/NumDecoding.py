# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:02:41 2019

@author: Agam
"""

class Solution:

    
    def numDecodings(self, s: str) -> int:
        cache = [0 for i in range(len(s) + 1) ]
        cache[len(s)] = 1
        
        for index in range(len(s) - 1, -1, -1):
            if s[index] == '0':
                cache[index] = 0
            elif index == len(s) - 1:
                cache[index] = 1
            else:
                cache[index] += cache[index + 1]
                if int(s[index:index + 2]) < 26:
                    cache[index] += cache[index + 2]
        print(cache)
        return cache[0]
s = Solution()
print(s.numDecodings('89'))