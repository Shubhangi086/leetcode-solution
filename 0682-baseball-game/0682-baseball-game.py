class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack=[]
        for i in range(len(operations)):
            try:
                stack.append(int(operations[i]))
            except ValueError:
                if operations[i]=='+':
                    stack.append(stack[-1]+stack[-2])
                elif operations[i]=="D":
                    stack.append(stack[-1]*2)
                elif operations[i]=="C":
                    stack.pop()
            total=sum(stack)
        return total