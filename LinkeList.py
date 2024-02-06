class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
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
            self.tail=new_node
        self.length+=1
        return True
    
    def pop(self):
        if self.length==0:
            return False
        temp=self.head
        prev=None
        while temp.next is not None:
            prev=temp
            temp=temp.next
        self.tail=prev
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp
    
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.length==0:
            return False
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr
    
    def set(self,index,value):
        if index<0 or index>=self.length:
            return None
        curr=self.head
        for _ in range(index):
            curr=curr.next
        if curr:
            curr.value=value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or index>self.length:  # not >= because the index == self.length means that the append operation will run
            return False
        if index==0:
            new_node=Node(value)
            if self.length==0:
                self.head=new_node
                self.tail=new_node
            else:
                new_node.next=self.head
                self.head=new_node
            self.length+=1
            return True
        if index==self.length:
            new_node=Node(value)
            if self.length==0:
                self.head =new_node
                self.tail=new_node
            else:
                self.tail.next=new_node
                self.tail=new_node
            self.length+=1
            return True
        new_node=Node(value)
        curr=self.head
        for _ in range(index-1):
            curr=curr.next
        new_node.next=curr.next
        curr.next=new_node
        self.length+=1
        return True
        
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            if self.length==0:
                return None
            curr=self.head
            self.head=self.head.next
            curr.next=None
            self.length-=1
            if self.length==0:
                self.tail=None
            return curr
        if index==self.length-1:
            if self.length==0:
                return None
            curr=self.head
            prev=None
            while curr.next is not None:
                prev=curr
                curr=curr.next
            prev.next=None
            self.tail=prev
            self.length-=1
            if self.length==0:
                self.head=None
                self.tail=None
            return curr
        curr=self.head
        prev=self.head
        for _ in range(index):
            prev=curr
            curr=curr.next
        prev.next=curr.next
        curr.next=None
        self.length-=1
        return curr

    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.head
        curr=self.head
        prev=None
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.tail=self.head
        self.head=prev
        return self.head
    
    # Leetcode problems based on the singly linked list for practice

    def find_middle(self): #without using length
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.value
    
    def has_loop(self):
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    
    def partition_list(self,x):
        if self.head is None:
            return None
        dummy1=Node(0)
        dummy2=Node(0)
        prev1,prev2=dummy1,dummy2
        curr=self.head
        while curr is not None:
            if curr.value<x:
                prev1.next=curr
                prev1=curr
            else:
                prev2.next=curr
                prev2=curr
            curr=curr.next
        prev1.next=None
        prev2.next=None
        prev1.next=dummy2.next
        return dummy1.next
    
    def remove_duplicates(self):  # using set to remove duplicates from the linked list
        values=set()
        prev=None
        curr=self.head
        while curr is not None:
            if curr.value in values:
                prev.next=curr.next
                self.length-=1
            else:
                values.add(curr.value)
                prev=curr
            curr=curr.next
    
    def remove_duplicates2(self):
        curr=self.head
        while curr:
            runner=curr
            while runner.next:
                if runner.next.value==curr.value:
                    runner.next=runner.next.next
                    self.length-=1
                else:
                    runner=runner.next
            curr=curr.next

    def binary_to_decimal(self):
        if self.head is None:
            return 0
        res=''
        curr=self.head
        while curr is not None:
            res+=str(curr.value)
            curr=curr.next
        return int(res,2)
    
    def binary_to_decimal2(self):
        num=0
        curr=self.head
        while curr:
            num=num*2+curr.value # num=num*2+curr.value is a logic to add the binary from left to right
            curr=curr.next
        return num
    
    def reverse_between(self,start_index,end_index):
        if self.head is None:
            return None
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy

        for _ in range(start_index):
            prev=prev.next
        curr=prev.next

        for _ in range(end_index-start_index):
            next_node=curr.next
            curr.next=next_node.next
            next_node.next=prev.next
            prev.next=next_node
        self.head=dummy.next

    
def find_kth_node_from_end(ll,k):
    slow=fast=ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast=fast.next
    while fast:
        slow=slow.next
        fast=fast.next
    return slow

    


    

my_list=LinkedList(4)
my_list.append(3)
my_list.append(2)
my_list.prepend(5)
my_list.prepend(6)
my_list.pop_first()
my_list.pop()
my_list.insert(2,11)
print(my_list.set(1,10))
print(my_list.get(7))
print(my_list.find_middle())
print(my_list.has_loop())
print(my_list.partition_list(5))
my_list.PrintList()
my_list.PrintList()
