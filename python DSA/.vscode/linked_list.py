class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.head = head

    def insertAtFirst(self,data):
        if self.head == None:
            self.head = Node(data)
            return self.head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(self.head.data)

    def insertAtLast(self,data):
        if self.head == None:
            self.insertAtFirst(data)
        new_node = Node(data)
        current = self.head
        while current != None:
            current = current.next
        current = new_node



ll = LinkedList()

# print(ll.head.next.data)
