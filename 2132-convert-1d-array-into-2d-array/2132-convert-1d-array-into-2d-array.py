class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original) != m*n:
            return []

        ans = [[] for i in range(m)]
        j = 0
        for i in range(m):    
            ans[i] = original[j:j+n]
            j += n 
        return ans

