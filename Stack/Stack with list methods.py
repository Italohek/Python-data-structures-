class Stack:
    def _init_(self):
        self.items = []

    #Return True if the Stack is empty
    def is_empty(self):
        return len(self.items) == 0
    
    #Adds a value to the Stack
    def add(self, item):
        self.items.append(item)

    #Withdraw the last value from the stack
    def poptop(self):
        if not self.empty():
            return self.items.pop()

    #Check what value is at the top of the Stack
    def top(self):
        if not self.empty():
            return self.items[-1]

    #Return the len of the stack
    def size(self):
        return len(self.items)
