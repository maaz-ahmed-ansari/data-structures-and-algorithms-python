def print_list(self):
    # Get the head variable
    temp = self.head
    # Iterate over the LL by self.head.next at each iteration
    # and print the value except when it's None
    while temp is not None:
        print(temp.value)
        temp = temp.next
