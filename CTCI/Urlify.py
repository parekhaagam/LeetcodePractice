# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:22:13 2019

@author: Agam
"""

class urlify:
    def solve(self,strList, trueLength):
        
        
        newPointer = len(strList) - 1
        oldPointer = trueLength - 1
        
        while newPointer >= 0:
            if strList[oldPointer] == ' ':
                print('updated string', strList)
                strList[newPointer] = '0'
                strList[newPointer - 1] = '2'
                strList[newPointer - 2 ] = '%'
                newPointer -= 3
                
            else:
                strList[newPointer] = strList[oldPointer]
                newPointer -= 1 
            oldPointer -= 1
            
        return strList
    
Urlify = urlify()
strList = [s for s in "Mr John Smith    "]

print(Urlify.solve(strList, 13))

                
                
        