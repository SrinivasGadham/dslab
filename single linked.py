class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertatBegin(self):
        if self.head==None:
            x=int(input("enter the value:"))
            newnode=Node(x)
            self.head=newnode
        else:
            x = int(input("enter the value:"))
            newnode=Node(x)
            newnode.next=self.head
            self.head=newnode
    def insertAtMiddle(self):
        x = int(input("enter the location:"))
        n=self.head
        for i in range(x-2):
            n=n.next
        x = int(input("enter the value:"))
        newnode = Node(x)
        newnode.next=n.next
        n.next=newnode


    def insertatEnd(self):
        if self.head==None:
            x=int(input("enter the value:"))
            newnode=Node(x)
            self.head=newnode
        else:
            x = int(input("enter the value:"))
            newnode=Node(x)
            n=self.head
            while(n.next):
                n=n.next
            n.next=newnode
    def deletionAtBegin(self):
        self.head=self.head.next
    def deletionAtEnd(self):
        n=self.head
        while(n.next.next!=None):
            n=n.next
        n.next=None
    def deletionatMiddle(self):
        x = int(input("enter the location:"))
        if x==1:
            self.deletionAtBegin()
        else:
            n=self.head
            for i in range(x-2):
                n=n.next
            n.next=n.next.next




    def display(self):
        n=self.head
        while n:
            print(n.data,end=" ")
            n=n.next
        print("")
s=LinkedList()
while 1:
    print("1.insertion")
    print("2.display")
    print("3.Deletion")
    print("4.Exit")
    a=int(input("Select your choice:"))
    if a==1:
        print("1.Insertatbegin")
        print("2.InsertatEnd")
        print("3.InsertatMiddle")
        a = int(input("Select your choice:"))
        if a==1:
            s.insertatBegin()
        elif a==2:
            s.insertatEnd()
        elif a==3:
            s.insertAtMiddle()
    elif a==2:
        s.display()
    elif a==3:
        print("1.Deletion at begin")
        print("2.Deletion at end")
        print("3.Deletion at Middle")
        a = int(input("Select your choice:"))
        if a==1:
            s.deletionAtBegin()
        elif a==2:
            s.deletionAtEnd()
        elif a==3:
            s.deletionatMiddle()

    elif a==4:
        exit()






