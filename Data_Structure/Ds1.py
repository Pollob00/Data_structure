class Node:
    def __init__(self,value):
        self.next = None
        self.prev = None
        self.val = value


class DoublelinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

        def add(self,val):
            node = Node(val)
            if self.tail is None:
                self.head = node
                self.tail = node
                self.size +=1
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                self.size +=1

     def __str__(self):
         vals =[]
         node = self.head
         while node is not None:
             vals.append(node.val)
             node=node.next
         return f"[{', '.join(str(val) for val in vals)}]"

my_list=DoublelinkedList
my_list.add(1)
my_list.add(4)
my_list.add(5)
my_list.add(6)
print(my_list)
