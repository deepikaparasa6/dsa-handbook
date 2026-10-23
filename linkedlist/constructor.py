class Node: #capital letter says that we are creating a class
    def __init__(self,value): #constructor method, creates a new node and initializes the value and next properties
        self.value = value #assigns the value to the node
        self.next = None #assigns the next property to None, since this is a new node and it doesn't point to anything yet

class LinkedList: #capital letter says that we are creating a class
    def __init__(self,value): #constructor method, creates a new node and initializes the linkedlist
        new_node = Node(value) #creates a new node using the Node class and assigns it to new_node
        self.head = new_node #assigns the head property to the new_node
        self.tail = new_node #assigns the tail property to the new_node
        self.length = 1 #assigns the length property to 1, since we have one node in the linkedlist

    def append(self,value): #creates a new node and appends it to the end of the linkedlist
    def prepend(self,value): #creates a new node and prepends it to the beginning of the linkedlist
    def insert(self,index,value): #creates a new node and inserts it at the specified index in the linkedlist
       
my_linked_list = LinkedList(4) #creates a new linkedlist with a value of 4


''' 
So the constructor it is going to create a node.
It's also going to initialize the new linked list.
But it's going to create a node.
The append method is going to create a node.
And then add that node to the end.
Prepend is going to create a node and add that node to the beginning insert.
It's going to create a node, and then insert that node at whatever index where you want that.
So you can see these all create a new node.
So we don't want to write the code for creating a new node for different times.
So what we're going to do is we're going to create a class that does nothing but create nodes.
And we're going to call that class.
node.
So when any one of these four methods needs to create a node, it will call on.
The node class to create it.
And the only thing this is going to contain is a constructor, that we're going to pass a value so we
can assign it to the node.

'''