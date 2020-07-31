# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node

    def remove_next(self):
        self.next_node = None

    def __str__(self):
        return f"{self.data}"
# A Linked List class with a single head node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, value):
        new_node = Node(value)
        if(self.head is None and self.tail is None):
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next_node = self.head
            self.head = new_node
            self.size += 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.size += 1

    def pop(self):
        if self.tail is None and self.head is None:
            return None

        if self.tail is self.head:
            val = self.head.value
            self.tail = None
            self.head = None
            self.size -= 1
            return val

        if self.head.next_node is self.tail:
            val = self.tail.value
            self.head.next_node = None
            self.tail = self.head
            self.size -= 1
            return val
        curr_val = self.head
        while curr_val:
            if curr_val.next_node.next_node is None:
                val = curr_val.next_node.value
                curr_val.next_node = None
                self.tail = curr_val
                self.size -= 1
                return val

            curr_val = curr_val.next_node

    def shift(self):
        # If list is empty, do nothing
        if not self.head:
            return None
        # if list has one element, set head and tail to none
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            self.size -= 1
            return head_value
        # with more than one element in list, Do:
        head_value = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return head_value

    def printLL(self):
        current = self.head
        while(current):

            print(current.value)
            current = current.next_node

    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None

        current_node = self.head
        list_max = 0
        while current_node is not None:
            if current_node.value > list_max:
                list_max = current_node.value
            current_node = current_node.next_node
        return list_max


# LL = LinkedList()
# LL.insert(3)
# LL.insert(4)
# LL.insert(5)
# LL.printLL()
