class Queue:
    def __init__(self):
        self.items = []

    #Return True if the Queue is empty
    def is_empty(self):
        return len(self.items) == 0
    
    #Adds a value to the end of the Queue
    def add(self, item):
        self.items.append(item)

    #Withdraw the first value from the Queue
    def pop_first(self):
        if not self.is_empty():
            return self.items.pop(0)

    #Return the first value from the Queue
    def peek(self):
        if not self.is_empty():
            return self.items[0]
    
    #Return the size of the Queue
    def size(self):
        return len(self.items)
    
    #Return the Queue
    def get_queue(self):
        return self.items
    
