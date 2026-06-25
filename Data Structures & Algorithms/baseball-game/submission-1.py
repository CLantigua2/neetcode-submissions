class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for s in operations:
            if s == "+":
                # add previous 2 items
                stack.append(stack[-1] + stack[-2])
            elif s == "C":
                # invalidate previous
                stack.pop()
            elif s == "D":
                # record new score * 2
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(s))
        return sum(stack)

