#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
    def evalRPN(self, tokens):
        
        stack=[]
        for i in tokens:
            if i=="+" or i=="-" or i=="*" or i=="/":
                a=stack.pop()
                b=stack.pop()
                
                if i=='+':
                    stack.append(int(b)+int(a))
                elif i=='-':
                    stack.append(int(b)-int(a))
                elif i=='*':
                    stack.append(int(b)*int(a))
                elif i=='/':
                    stack.append(int(float(b) / float(a)))
            else:
                stack.append(i)
            print(stack)
        return int(stack.pop())
