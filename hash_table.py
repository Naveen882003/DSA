class HashTable:
    def __init__(self,size):
        self.data_map=[None]*size

    def __hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash+ord(letter)*23%len(self.data_map))
        return my_hash
    
    def set_item(self,key,value):
        index=self.__hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index=self.__hash(key)
        if self.data_map[index]is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    


# Common Interview problems

def item_in_common(li1,li2):
    my_dict={}
    for i in li1:
        my_dict[i]=True
    for j in li2:
        if j in my_dict:  # my_dict[j]==True gets the key error if the key is not found
            return True
    return False



def count_duplicates0(arr):
    res={}
    for num in arr:
        val=res.get(num,0)
        res[num]=val+1
    return res

def count_duplicates1(arr):
    res={}
    for num in arr:
        if num in res:
            res[num]+=1
        else:
            res[num]=1
    return res

from collections import Counter
def count_duplicates2(arr):
    res=Counter(arr)
    return res

def first_non_repeating_char(string):
    my_dict={}
    for s in string:
        my_dict[s]=my_dict.get(s,0)+1
    for char in my_dict:
        if my_dict[char]==1:
            return char
    return None

def group_anagrams(string):
    anagram_group={}
    for s in string:
        canonical=''.join(sorted(s))
        if canonical in anagram_group:       # separate chaining idea is executed in this problem
            anagram_group[canonical].append(s)    # other canonical formats are calculate the total ord of string
        else:
            anagram_group[canonical]=[string]
    return list(anagram_group.values())

def two_sum(nums,target):
    res={}
    for i,num in enumerate(nums):
        val=target-num
        if val in res:     
            return(res[val],i)
        res[num]=i
    return []

def subarray_sum(nums,target):
    sum_index={0:-1}
    curr_sum=0
    for i,num in enumerate(nums):
        curr_sum+=num
        if (curr_sum-target) in sum_index:
            return [sum_index[curr_sum-target]+1,i]
        sum_index[curr_sum]=i
    return []







