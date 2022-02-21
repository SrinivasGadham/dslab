class Stack:

    def __init__(self):
        self.stack = [None]*14
        self.top=-1
    def spush(self,x):
        self.top+=1
        #print(self.top)
        self.stack[self.top]=x
    def spop(self):
        self.top-=1
        return self.stack[self.top+1]
    def display(self):
        for i in range(self.top+1):
            print(self.stack[i])
    def isEmpty(self):
        if self.top==-1:
            #
            print("Stack is Empty")
            return True
    def topchar(self):
        return self.stack[self.top]
def infix():
    result=""
    d={"+":1,"-":1,"*":2,"/":2,"^":3}
    s=Stack()
    operator="+-*/^"
    exp=input("enter the expression:")
    for i in exp:
        if i.isalpha() or i.isnumeric():
            result+=i
        elif i in operator:
            while(1):

                top=s.topchar()
                if s.isEmpty() or top=='(':
                    s.spush(i)
                    break
                else:
                    if d[i]>d[top]:
                        s.spush(i)
                        break
                    else:
                        cpop=s.spop()
                        result+=cpop
        elif i is '(':
            s.spush(i)
        elif i is ')':
            cpop=s.spop()
            while cpop!='(':
                result+=cpop
                cpop=s.spop()
    while not s.isEmpty():
        result+=s.spop()
    return result
print(infix())





