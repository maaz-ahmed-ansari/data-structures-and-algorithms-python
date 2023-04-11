class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def pop(self):
        # if LL is  empty
        if self.head is None:
            return None
        # if LL contains only one node
        if self.head.next is None:
            pop = self.head
            self.head = None
            self.tail = None
            self.length = 0
        else:
            # for LL containing 2 or more nodes
            temp = self.head
            # track when next to next node is None
            while temp.next.next is not None:
                temp = temp.next
            # when nex to next node found None i.e. we found node before Tail
            # make next node as None
            # and make node before tail as Tail
            pop = temp.next
            self.tail = temp
            self.tail.next = None
            self.length -= 1
        # Return poped item, since pop() removes the item 
        # and return to where it is caleed
        return pop
            


my_ll = LinkedList(1)
my_ll.make_empty()
my_ll.append(1)
my_ll.append(3)
my_ll.append(6)
print("#####Linked List")
my_ll.print_list()

print("\n#####After pop")
print("poped value: ",my_ll.pop().value)
print("-----Linked List")
my_ll.print_list()

print("\n#####After one more pop")
print("poped value: ",my_ll.pop().value)
print("-----Linked List")
my_ll.print_list()

print("\n#####After one more pop")
print("poped value: ",my_ll.pop().value)
print("-----Linked List")
my_ll.print_list()

print("\n#####After one more pop")
my_ll.pop()
print("-----Linked List")
my_ll.print_list()

"""
    #####Linked List
    1
    3
    6

    #####After pop
    poped value:  6
    -----Linked List
    1
    3

    #####After one more pop
    poped value:  3
    -----Linked List
    1

    #####After one more pop
    poped value:  1
    -----Linked List

    #####After one more pop
    -----Linked List

"""
