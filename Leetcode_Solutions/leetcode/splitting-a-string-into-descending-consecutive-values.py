class Solution:
    def splitString(self, s: str) -> bool:
        current = []

        def backtrack(idx):
            if idx >= len(s):

                return len(current) >= 2

            for i in range(idx, len(s)):
                val = int(s[idx:i + 1])
                if not current or current[-1] - val == 1:
                    current.append(val)

                    if backtrack(i + 1):
                        return True

                    current.pop()


            return False

        return backtrack(0)