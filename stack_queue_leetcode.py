class Stack:
    def __init__(self):
        self.stk=[]

    def push(self,value):
        self.stk.append(value)

    def pop(self):
        if len(self.stk)==0:
            return None
        return self.stk.pop()
    

def paranthesis_balanced(s: str):
    open_list=['(','{','[']
    close_list=[')','}',']']
    stk=[]
    for string in s:
        if string in open_list:
            stk.append(string)
        elif len(stk)==0 and string in close_list:
            return False
        else:
            pos=close_list.index(string)
            
            if open_list[pos]==stk[-1]:
                stk.pop()
            else:
                return False
    return len(stk)==0



def reverse_string(string):
    stk=[]
    res=""
    for i in string:
        stk.append(i)
    while len(stk)>0:
        res+=stk.pop()
    return res

print(reverse_string('naveen'))

# Implementing queue using two stacks

class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self,x):
        self.s1.append(x)

    def pop(self):
        n=len(self.s1)-1
        for _ in range(n):
            self.s2.append(self.s1.pop())
        temp=self.s1.pop()
        for _ in range(n):
            self.s1.append(self.s2.pop())
        return temp
    
    def peek(self):
        return self.s1[0]
    
    def is_empty(self):
        return len(self.s1)==0
    
q=Queue()
q.push(1)
q.push(2)
q.push(3)
q.pop()


