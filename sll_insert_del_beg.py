class Node:
    def __init__(self,x):
        self.data=x
        self.nextt=None
class SLL:
    def __init__(self):
        self.head=None
    def insertAtbegin(self):
        val=int(input("enter a val to insert"))
        Newnode=Node(val)
        Newnode.nextt=self.head
        self.head=Newnode
    def delAtbegin(self):
        val=int(input("enter a val to delete"))
        Newnode=Node(val)
        temp=self.head
        self.head=self.head.nextt
        temp.next=None
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.nextt
sl1=SLL()
ch=0
while ch!=4:
    print("1.insertion at begin 2.delete at begin 3.display 4.search")
    ch=int(input())
    if ch==1:
          sl1.insertAtbegin()
          sl1.display()
    if ch==2:
          sl1.delAtbegin()
          sl1.display()      
    if ch==3:
          sl1.display()
    else:
        print("invalid choice")
