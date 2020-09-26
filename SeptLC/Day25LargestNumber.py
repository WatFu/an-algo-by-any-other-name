class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #sorted(list(map(str,nums)), reverse=True)
        if sum(nums) == 0:
            return '0'
        
        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr) // 2
            front = mergeSort(arr[:mid])
            back = mergeSort(arr[mid:])
            
            # if front[-1] <= back[0]:
            #     return front + back
            # if front[0] > back[-1]:
            #     return back + front
            
            tmp = []
            i, j, m, n = 0, 0, len(front), len(back)
            
            while i < m and j < n:
                if int(front[i] + back[j]) > int(back[j] + front[i]):
                    tmp.append(front[i])
                    i += 1
                else:
                    tmp.append(back[j])
                    j += 1
            
            if i < m:
                return tmp + front[i:]
            else:
                return tmp + back[j:]
        
        return "".join(mergeSort(list(map(str, nums))))
