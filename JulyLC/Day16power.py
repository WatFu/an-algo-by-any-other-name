class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
            if n == 1:
                return x
            if n%2 == 1:
                return x * self.myPow(x, n - 1)
            return self.myPow(x * x, n/2)
            #return self.myPow(x, n/2) * self.myPow(x,n/2) fails TLE... extra invocation of the function
        elif n < 0:
            return 1/self.myPow(x,-1*n)
        return 1
        
        # doesn't work with large numbers
        # res = 1
        # if n > 0:
        #     while n > 0:
        #         res *= x
        #         n -= 1
        # else:
        #     while n < 0:
        #         res /= x
        #         n += 1
        # return res
    
        # doesn't work with python because of recursion depth
        # if n == 0:
        #     return 1
        # if n > 0:
        #     return x * self.myPow(x,n-1)
        # if n < 0:
        #     return self.myPow(x,n+1)/x
