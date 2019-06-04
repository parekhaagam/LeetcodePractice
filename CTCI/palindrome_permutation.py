# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:49:46 2019

@author: Agam
"""

class palindrome_permutation:
    def solve(self, string):
        string = string.lower()
        
        if len(string) == 0:
            return True
        
        countList = [0 for i in range(26)]
        
        for st in string:
            if st != ' ':
                index = ord(st) - ord('a')
                #print(index)
                countList[index] += 1
        
        odd_count = 0
        print(countList)
        for eachCount in countList:
            if eachCount %2 == 1:
                if odd_count == 0 :
                    
                    odd_count += 1
                    print('incrementing', eachCount)
                elif odd_count == 1:
                    return False
        return True

pal = palindrome_permutation()
print(pal.solve("Tact Coa"))
            
