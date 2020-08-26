import collections

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        h = collections.OrderedDict({3: 'Fizz', 5: 'Buzz'})
        res = []
        for i in range(1,n+1):
            ans = ""
            for key in h.keys():
                if i%key == 0:
                    ans += h[key]
            if ans == "":
                ans = str(i)
            res.append(ans)
        
        return res
