import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
     
        if len(self.items)==0
           
    def is_full(self):
        # Write code here
        if len(self.item) == self.size
           

    def push(self, data):
        if not self.is_full():
            # Write code here
            self.items.apend(data)

    def pop(self):
        if not self.is_empty():
            # Write code here
            self.items.pop(-1)

    def status(self):
        # Write code here
        for element in self.items:
            print(element)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
