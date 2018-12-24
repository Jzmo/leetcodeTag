class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = [1,1,]
        if n >= 2:
            for i in range(2,n+1):
                output.append(0)
                for j in range(i):
                    output[i] += output[j]*output[i-j-1]
        return output[n]
        