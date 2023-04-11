# def append(self, value):
#     new_node = Node(value)
#     if self.head is None:
#         self.head = new_node
#         self.tail = new_node
#     else:
#         self.tail.next = new_node
#         self.tail = new_node
#     self.length += 1
#     return True

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        # note while comparing for head, use head itself rather than head.value or head.next
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # note here to tail.next we are assigning the new node itself i.e. both attributes value and next of new node
            self.tail.next = new_node
            self.tail = new_node

my_linked_list = LinkedList(4)

my_linked_list.append(3)

my_linked_list.append(5)

my_linked_list.print_list()