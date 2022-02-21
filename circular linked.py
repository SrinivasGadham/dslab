class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def atBegin(self):
        if self.head==None:
            x=int(input("enter the value item:"))
            newnode=Node(x)
            self.head=newnode
            self.tail=newnode
            newnode.next=self.head
            newnode.prev=self.tail
        else:
            x = int(input("enter the value item:"))
            newnode = Node(x)
            newnode.next=self.head
            newnode.prev=self.tail
            self.head.prev=newnode
            self.head=newnode
            self.tail.next=newnode
    def atEnd(self):
        if self.head==None:
            x=int(input("enter the value item:"))
            newnode=Node(x)
            self.head=newnode
            self.tail=newnode
            newnode.next=self.head
            newnode.prev=self.tail
        else:
            x = int(input("enter the value item:"))
            newnode = Node(x)
            newnode.prev=self.tail
            newnode.next=self.head
            self.tail.next=newnode
            self.tail=newnode
            self.head.prev=newnode
    def atMiddle(self):
        if self.head==None:
            x=int(input("enter the value item:"))
            newnode=Node(x)
            self.head=newnode
            self.tail=newnode
            newnode.next=self.head
            newnode.prev=self.tail
        else:
            x = int(input("enter the value item:"))
            newnode = Node(x)
            loc=int(input("enter the location:"))
            n=self.head
            for i in range(loc-2):
                n=n.next
            newnode.next=n.next
            newnode.prev=n
            n.next.prev=newnode
            n.next=newnode
    def deletionAtFirst(self):
        if self.head==None:
            print("Linked List is empty")
        else:
            self.head=self.head.next
            self.head.prev=self.tail
            self.tail.next=self.head
    def deletionAtLast(self):
        if self.head==None:
            print("Linked List is empty")
        else:
            self.tail=self.tail.prev
            self.tail.next=self.head
            self.head.prev=self.tail
    def display(self):
        n=self.head
        while(n!=self.tail):
            print(n.data,end=" ")
            n=n.next
        print(n.data)
obj=LinkedList()
while(1):
    print("1.Insertion")
    print("2.Display")
    print("3.Deletion")
    print("4.exit")
    n=int(input("Select your option:"))

    if n==1:
        print("1.AtBegin")
        print("2.AtEnd")
        print("3.AtMiddle")
        a = int(input("Select your option:"))
        if a==1:
            obj.atBegin()
        elif a==2:
            obj.atEnd()
        elif a==3:
            obj.atMiddle()

    elif n==2:
        obj.display()
    elif n==3:
        print("1.AtBegin")
        print("2.AtEnd")
        print("3.AtMiddle")
        a = int(input("Select your option:"))
        if a == 1:
            obj.deletionAtFirst()
        elif a==2:
            obj.deletionAtLast()
    elif n==4:
        exit()





