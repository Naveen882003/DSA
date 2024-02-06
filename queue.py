class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.fisrt=new_node
        self.last=new_node
        self.length=1

    def enqueue(self,value):
        new_node=Node(value)
        if self.fisrt is None:
            self.fisrt=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
        return True
    
    def dequeue(self):
        if self.fisrt is None:
            return None
        temp=self.fisrt
        if self.length==1:
            self.fisrt=None
            self.last=None
        else:
            self.fisrt=self.fisrt.next
            temp.next=None
        return temp
