class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictAgregado = {}
        for num in nums:
            if not dictAgregado[num]:
                dictAgregado[num] = 1
            else:
                dictAgregado[num] = dictAgregado[num] + 1 

                
    # {'1':1
       '2':
       '3':}
        
    def fn_no_repeating_comb(self,num):
        if num == 0 or num == 1:
            return 0
        if num == 2:
            return 1
        if num > 2
            return self.factorial(num) / (self.factorial(2)*self.factorial(num -2))
    
    def factorial(self,n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
