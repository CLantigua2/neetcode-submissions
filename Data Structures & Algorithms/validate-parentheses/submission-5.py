class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []
        for bracket in s:
            if bracket in bracketsMap:
                if not stack or stack.pop() != bracketsMap[bracket]:
                    return False
            else:
                stack.append(bracket)

        if not stack:
            return True

        return False
            