class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []
        for b in s:
            if b == "]" and stack:
                curr = stack.pop()
                if curr != brackets[b]:
                    return False
            elif b == "}" and stack:
                curr = stack.pop()
                if curr != brackets[b]:
                    return False            
            elif b == ")" and stack:
                curr = stack.pop()
                if curr != brackets[b]:
                    return False
            else:
                stack.append(b)

        if not stack:
            return True

        return False
            