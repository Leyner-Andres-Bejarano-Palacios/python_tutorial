#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accumt = 0
        runningSum = []
        for numIndex in range(len(nums)):
            accumt  = accumt + nums[numIndex]
            runningSum.append(accumt)
        return runningSum
        
        
            
solution = Solution()
print(solution.runningSum([1,2,3,4]))