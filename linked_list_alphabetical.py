
# coding: utf-8

# In[6]:


'''This module contains a class representing linked list structure constructed for storing string data in alphabetical order.'''


# In[7]:


class DataError(Exception):
    
    '''Class representing a wrong data error.'''
    
    def __init__(self):
        Exception.__init__(self,'Node must contain a string.')


# In[8]:


class Node:
    
    '''Class representing a node - a 'box' where the data is stored.'''

    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        '''Returns the node data.'''
        return self._data

    @property
    def next_node(self):
        '''Returns the next node in the list.'''
        return self._next_node
    
    @data.setter
    def data(self, new_data):
        '''Sets new node data.'''
        self._data = new_data
    
    @next_node.setter
    def next_node(self, new_next_node): 
        '''Makes the node point at a new node as the one following it in the list.'''
        self._next_node = new_next_node


# In[9]:


class LinkedListAlphabetical:
    
    '''Klasa reprezentujaca strukture singly linked list.'''

    def __init__(self, head=None, size=0):
        self._head = head
        self._size = size

    @property
    def size(self):
        '''Returns the size of the list.'''
        return self._size
    
    @property
    def head(self):
        '''Returns the head element of the list.'''
        return self._head
    
    @size.setter
    def size(self, new_size):
        '''Sets the size of the list.'''
        self._size = new_size
    
    def increm_size(self, inc):
        '''Increments the size of the list.'''
        self.size = self.size + inc
        
    @head.setter
    def head(self, new_head):
        '''Sets the new head element of the list.'''
        self._head = new_head
        
    def goes_first(self, word1, word2):
        '''Checks which of the 2 words goes first alphabetically.'''
        if len(word1) >= len(word2):
            n = len(word2)
            smaller = word2
            bigger = word1
        else:
            n = len(word1)
            smaller = word1
            bigger = word2
            
        if set(smaller) == set(bigger):
            first = smaller  
        else:
            first = bigger
            for i in range(n):
                if ord(smaller[i]) < ord(bigger[i]):
                    first = smaller
                    break
                elif ord(smaller[i]) > ord(bigger[i]):
                    break
        return first
    
    def insert_beg(self, data):
        '''Inserts a new element at the beginning of the list.'''
        new_node = Node(data, self.head)
        self.head = new_node
        self.increm_size(1)
    
    def insert_mid(self, data, next_node, prev_node):
        '''Inserts element inside the list.'''
        new_node = Node(data, next_node)
        prev_node.next_node = new_node
        self.increm_size(1)
        
    def insert_end(self, data, prev_node):
        '''Inserts a new element in the end of the list.'''
        new_node = Node(data, None)
        prev_node.next_node = new_node
        self.increm_size(1)
    
    def insert_node(self, data):
        '''Inserts a new element accodrding to the right alphabetical order into the list.'''
        if type(data) != str:
            raise DataError
        else:
            curr = self.head
            prev = None
            inserted = False

            if not curr:
                self.insert_beg(data)
            else:
                while curr:
                    if (self.goes_first(curr.data, data) == data):
                        if prev == None:
                            self.insert_beg(data)
                        else:
                            self.insert_mid(data, curr, prev)
                        inserted = True
                        break
                    curr, prev = curr.next_node, curr
                if not inserted:
                    self.insert_end(data, prev)
       
    def print_nodes(self):
        '''Prints out all the list nodes.'''
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next_node

