stack = [None]*10
top=-1
def add(x):
    global top
    global stack
    top+=1
    stack[top]=x
def delete():
    global top
    global stack
    a=stack[top]
    top-=1
    return a
def infixToP(exp):
    global stack
    global top
    output=''
    s = {'+', '-', '*', '/','(',')'}
    pr = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for i in exp:
        if i not in s:
            output+=i
        elif i=='(':
            add(i)

        elif i==')':
            while stack and stack[top]!='(':
                output+=delete()
            delete()
        else:
            while stack[0]!=None and stack[top]!='(' and pr[stack[top]]>=pr[i]:
                output+=delete()
            add(i)
    while stack[top]!=None:
        output+=delete()
    print(output)
infixToP(input("enter the prefix expression:"))


