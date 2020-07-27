"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def insert_next(self, node):
        #check if has previous node and make sure it doesnt refer to this any longer
        if node.prev:
            node.prev.next = None  #cleans up the previous node
        # node.prev can be set to this node, and can set next node
        node.prev = self
        self.next = node
    
    """Inserts a node to this node's prev property and updates pointers"""

    def insert_previous(self, node):
        if node.next:
            node.next.prev = None #cleans up next nodes prev pointer
        node.next = self
        self.prev = node

    """Rearranges the pointers to effectively delete the listnode"""
    
    def self_destruct(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev



"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def set_head_and_tail_to(self, node):
        self.head = node
        self.tail = node
        self.length = 1
    
    def reset(self):
        self.head = None
        self.tail = None
        self.length = 0

    def tail_is_heads(self):
        return self.tail is self.head
    
    def node_is_tails_or_head(self, node):
        return node is self.tail or node is self.head
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #if linked list has no nodes
        node = ListNode(value)
        if self.head is None and self.tail is None:
            self.set_head_and_tail_to(node)
        #if linked list has > 1 node
        else:
            self.head.insert_previous(node)
            self.head = node
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        head = self.head
        self.delete(self.head)
        return head.value if head else None
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #if linked list is empty
        node = ListNode(value)
        if self.head is None and self.tail is None:
            self.set_head_and_tail_to(node)
        #if linked list > 1
        else:
            self.tail.insert_next(node)
            self.tail = node
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        tail = self.tail
        self.delete(self.tail)
        return tail.value if tail else None
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #if list is empty or just self.head do nothing
        if node is None or node is self.head:
            return
        #if node is self.tail
        elif node is self.tail:
            self.remove_from_tail()
        #if any node that isnt tails
        else:
            self.delete(node)
        value = node.value
        self.add_to_head(value)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        #if list is empty or self.tail do nothing
        if node is None or node is self.tail:
            return
        #if node is self.head
        elif node is self.head:
            self.remove_from_head()
        #any node that isnt tails
        else:
            self.delete(node)
        value = node.value
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #if no tiems
        if not self.length:
            return
        #if only 1 item exists
        if self.tail_is_heads():
            self.reset()
            return
        
        #if 2 items exist
        if self.node_is_tails_or_head(node):
            #connected_node will be the node thats connected to the node being deleted
            #node.delete helper will cut all connections to node, then set tail and hea to connected_node
            connected_node = None
            #check head or tails
            if node.prev:
                connected_node = node.prev
            elif node.next:
                connected_node = node.next
            
            if self.length == 2:
                self.set_head_and_tail_to(connected_node)
                return
            
            if node is self.tail:
                self.tail = connected_node
            else:
                self.head = connected_node
        
        self.length -= 1
        node.self_destruct()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        high = self.head.value
        node = self.head

        while node:
            high = node.value if node.value > high else high
            node = node.next
        return high

node = ListNode(44444444)
testin = DoublyLinkedList(node)


testin.add_to_tail(9090090900)
print(testin.head.__dict__)
testin.delete(node)
print(testin.head.__dict__)