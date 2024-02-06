class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    
class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def PrintList(self):
        curr=self.head
        while curr is not None:
            print(curr.value,end=' ')
            curr=curr.next

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True

    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.tail
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp.value
    
    def pop2(self):
        if self.length==0:
            return None
        temp=self.tail
        self.tail=self.tail.prev
        self.tail.next=None
        temp.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp
    
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.head is None:
            return None
        temp=self.head
        self.head=self.head.next
        self.head.prev=None
        temp.next=None
        self.length-=1
        if self.length==0:
            self.head= None
            self.tail=None
        return temp.value
    
    def pop_first2(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return temp.value
    
    def get(self,index):  # Original way to get the value from the doubly linked list
        if index<0 or index>=self.length:  # Similar method like singly linked list
            return None
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr
    
    def get2(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        if index<self.length//2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    
    def set(self,index,value):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        if value<self.length//2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        if temp:
            temp.value=value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            return None
        if self.length==0:
            new_node=Node(value)
            if self.length==0:
                self.head=new_node
                self.tail=new_node
            else:
                new_node.next=self.head
                self.head.prev=new_node
                self.head=new_node
            self.length+=1
            return True
        if self.length==index:
            new_node=Node(value)
            if self.length==0:
                self.head=new_node
                self.tail=new_node
            else:
                self.tail.next=new_node
                new_node.prev=self.tail
                self.tail=new_node
            self.length+=1
            return True
        new_node=Node(value)
        temp=self.head
        if index<self.length//2:
            for _ in range(index-1):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index-1,-1):
                temp=temp.prev
        after=temp.next
        new_node.prev=temp
        new_node.next=after
        temp.next=new_node
        after.prev=new_node
        self.length+=1
        return True
    
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            if self.length==0:
                return None
            temp=self.head
            if self.length==1:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
                self.head.prev=None
                temp.next=None
            self.length-=1
            return temp
        if index==self.length-1:
            if self.length==0:
                return None
            temp=self.tail
            if self.length==1:
                self.head=None
                self.tail=None
            else:
                self.tail=self.tail.prev
                self.tail.next=None
                temp.prev=None
            self.length-=1
            return temp
        temp=self.head
        if index<self.length//2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        before=temp.prev
        after=temp.next
        before.next=after
        after.prev=before
        temp.next=None
        temp.prev=None
        self.length-=1
        return temp
    
    # Leetcode problems based on doubly linked list

    def swap_first_last(self):
        if self.head is None or self.head==self.tail:
            return None
        self.head.value,self.tail.value=self.tail.value,self.head.value

    def reverse(self):
        temp=self.head
        while temp is not None:
            temp.next,temp.prev=temp.prev,temp.next
            temp=temp.prev
        self.head,self.tail=self.tail,self.head

    def is_palindrome(self):
        if self.length<=0:
            return True
        front=self.head
        back=self.tail
        for _ in range(self.length//2):
            if front.value!=back.value:
                return False
            front,back=front.next,back.prev
        return True
    
    def swap_pairs(self):
        pass
        


        





my_list=DoublyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.prepend(0)
my_list.pop()


my_list.reverse()
my_list.PrintList()


        