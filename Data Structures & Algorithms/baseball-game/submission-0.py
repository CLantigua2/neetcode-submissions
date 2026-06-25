class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for s in operations:
            if s == "+":
                # add previous 2 items
                first = stack[-1]
                second = stack[-2]
                stack.append(int(first) + int(second))
            elif s == "C":
                # invalidate previous
                stack.pop()
            elif s == "D":
                # record new score * 2
                stack.append(str(int(stack[-1]) * 2))
            else:
                stack.append(s)

        sum = 0

        while len(stack) > 0:
            sum = sum + int(stack.pop())

        return sum

