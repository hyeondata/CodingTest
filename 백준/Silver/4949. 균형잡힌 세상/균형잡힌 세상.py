while True:
    s = input()
    stack = []
    balanced = True    
    if s == ".":
        break


    for i in range (len(s)):
        
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])

        if s[i] == ')':
            if not stack or stack[-1] != "(":  
                balanced = False
                break
            stack.pop()

        if s[i] == ']':
            if not stack or stack[-1] != "[":  
                balanced = False
                break
            stack.pop()
                
    print("yes" if balanced and not stack else "no")
