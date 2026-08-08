#creating a node class first
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None #pointer to next node
class LinkedList:
    def __init__(self):
        self.head=None #here head is the starting node of the 
        #linked list so the data is None
    def insert_at_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next 
        temp.next=new_node # new_node is temp.next which means Node(data)
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")#it displays the data horizontally
            temp=temp.next
        print("None")
ll=LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()
