
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data=data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def show(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def reverse_linked_list(self):
        # Initialize three pointers
        prev = None
        curr = self.head
        # next = self.head.next

        while curr:
            next = curr.next
            # reverse direction
            curr.next = prev
            # shift nodes
            prev = curr
            curr = next
        # set new head
        self.head = prev


llist = LinkedList()
print(llist)

llist.insert('a')
llist.insert('b')
llist.insert('c')
llist.insert('d')

llist.show()

llist.reverse_linked_list()

llist.show()







