class LinkedList:
    def __init__(self):
        self.items=[]
    def add(self, value):
        self.items.append(value)
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
ll=LinkedList()
ll.add(2)
ll.add(35)
ll.add(32)
print(len(ll))#3
print(ll)#[2, 35, 32]


    