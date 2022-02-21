class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self,root):
        self.root=Node(root)
    def insert(self,root,i):
        if i<root.data:
            if root.left:
                self.insert(root.left,i)
            else:
                root.left=Node(i)
        if i>root.data:
            if root.right:
                self.insert(root.right,i)
            else:
                root.right=Node(i)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def deletion(self,root,data):
        if root:
            if root.data<data:
                root.right=self.deletion(root.right,data)
            elif root.data>data:
                root.left=self.deletion(root.left,data)
            else:
                if root.data==data:
                    print("Found")
                    if root.left and root.right:
                        temp=self.findMax(root.left)
                        root.data=temp.data
                        root.left=self.deletion(root.left,temp.data)
                    elif root.left:
                        root=root.left
                    else:
                        root=root.right
                else:
                    print("Not Found")
        else:
            print("Not Found")


        return root


    def findMax(self,root):
        if root.left==None and root.right==None:
            return root
        else:
            self.findMax(root.right)




l=[int(i) for i in input("Enter the elements you wanted to enter:").split()]
bt=BST(l[0])
for i in l[1:]:
    bt.insert(bt.root,i)
while(1):
    print("1.Insertion\n2.Deletion\n3.Display")
    d=int(input("Select your choice:"))
    if d==1:
        a = int(input("enter the element you want to insert:"))
        bt.insert(bt.root, a)
    elif d==2:
        a = int(input("enter the element you want to delete:"))
        bt.deletion(bt.root,a)
    elif d==3:
        bt.inorder(bt.root)
    else:
        exit()












