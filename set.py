def remove_duplicates(my_list):
    return list(set(my_list))

    #new_list=list(set(my_list))
    #return new_list


def has_unique_chars0(strings):
    return len(strings)==len(set(strings))

def has_unique_chars1(strings):
    char_set=set()
    for char in strings:
        if char in char_set:
            return False
        char_set.add(char)
    return True

print(has_unique_chars1('naveen'))

def find_pairs(arr1,arr2,target):
    set1=set(arr1)
    pairs=[]
    for num in arr2:
        complement=target-num
        if complement in set1:
            pairs.append([complement,num])
    return pairs

print(find_pairs([1,2,3,4,5,6],[3,4,5,6],9))

def longest_consecutive_sequence(nums):
    num_set=set(nums)
    longest_sequence=0
    for num in nums:
        curr_sum=num
        current_seqence=1
        while curr_sum+1 in num_set:
            curr_sum+=1
            current_seqence+=1
        longest_sequence=max(longest_sequence,current_seqence)
    return longest_sequence

print(longest_consecutive_sequence([1,2,3,4,5,7,11,12,13,14,15,16,17]))



