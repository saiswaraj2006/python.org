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
#output: 10->20->30->None

#insert at beginning 
#means aat head node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None   # start of the list

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head   # link new node to current head
        self.head = new_node        # update head to new node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
ll = LinkedList()
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)
ll.display()
'''
10 -> 20 -> 30 -> None
'''
#deleting the beginning (Head Removal)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        self.head = self.head.next   # move head to next node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
ll = LinkedList()
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)

ll.display()          # 10 -> 20 -> 30 -> None
ll.delete_at_beginning()
ll.display()          # 20 -> 30 -> None

