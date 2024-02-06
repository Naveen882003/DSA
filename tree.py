# Binary search tree without recursion

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        else:
            temp=self.root
            while(True):
                if temp.value==new_node.value:
                    return False
                elif new_node.value<temp.value:
                    if temp.left is None:
                        temp.left=new_node
                        return True
                    temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        return True
                    temp=temp.right


    def in_order(self):
        results=[]
        def traverse(curr_node):
            if curr_node.left is not None:
                traverse(curr_node.left)
            results.append(curr_node.value)
            if curr_node.right is not None:
                traverse(curr_node.right)
        traverse(self.root)
        return results

    def contains(self,value):
        if self.root is None:
            return False
        temp=self.root
        while temp is not None:
            if temp.value>value:
                temp=temp.left
            elif temp.value<value:
                temp=temp.right
            else:
                return True
        return False


        
    
def print_tree(root):
    curr=root
    if curr.left is not None:
        print_tree(curr.left)
    print(curr.value,end=" ")
    if curr.right is not None:
        print_tree(curr.right)



t=BinarySearchTree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(-10)
print(t.contains(2))
                    
        
