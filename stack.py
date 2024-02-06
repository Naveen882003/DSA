class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.bottom=new_node  # bottom is not used in the stack
        self.height=1

    def push(self,value):
        new_node=Node(value)
        if self.top is None:
            self.top=new_node
            self.bottom=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1

    def pop(self):
        if self.top is None:
            return None
        temp=self.top
        self.top=self.top.next
        temp.next=None
        return temp
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.value
    
    def is_empty(self):
        if self.top is None:
            return True
        return False
    

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value,end=" ")
            temp=temp.next


stack=Stack(1)
stack.push(2)
stack.push(3)
print(stack.is_empty())
stack.print_stack()


