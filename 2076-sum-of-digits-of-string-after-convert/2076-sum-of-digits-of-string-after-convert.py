class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        for letter in s:
            res += str(ord(letter) - 96)
        for i in range(k):
            ans = 0
            for num in res:
                ans += int(num)
            res = str(ans)
        return ans
