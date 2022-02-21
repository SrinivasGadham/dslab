class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
class Stack:
    def __init__(self):
        self.top=None
    def add(self):
        item=int(input("Enter the item to be inserted:"))
        new=Node(item)
        if self.top==None:
            self.top=new
        else:
            new.link=self.top
            self.top=new
    def remove(self):
        if self.top==None:
            print("empty")
        else:
            self.top=self.top.link
    def Display(self):
        ptr=self.top
        while(ptr!=None):
            print(ptr.data)
            ptr=ptr.link

s=Stack()
n=1
while(1):
    print("****MENU******")
    print("1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT")
    n=int(input("Enter your option:"))
    if(n==1):
        s.add()
    elif(n==2):
        s.remove()
    elif(n==3):
        s.Display()
    else:
        exit()
