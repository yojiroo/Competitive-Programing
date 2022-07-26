class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)