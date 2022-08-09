#balancig parenthesis
def isBalanced(s):
    st=[]
    for char in s:
        if(char in "({["):
            st.append(char)
        elif char == ')':
            if(not st or st[-1]!='('):
                return False
            st.pop()
        elif char == '}':
            if(not st or st[-1]!='{'):
                return False
            st.pop()
        elif char == ']':
            if(not st or st[-1]!='['):
                return False
            st.pop()
    if(not st):
        return("Expression is balanced")
    return("Not Balanced")
s=input("Enter the expression: ")
ans=isBalanced(s)
print(ans)
