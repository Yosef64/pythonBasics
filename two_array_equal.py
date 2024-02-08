from collections import defaultdict
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        fSet , sSet = defaultdict(int),defaultdict(int)
        for ind in range(len(A)):
            fSet[A[ind]] += 1
            sSet[B[ind]] += 1
        #return: True or False
        return fSet == sSet
        #code here
