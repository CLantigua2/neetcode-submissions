class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []
        for b in s:
            if b in brackets:
                if not stack or stack.pop() != brackets[b]:
                    return False
            else:
                stack.append(b)

        if not stack:
            return True

        return False
            