def binary_search (seq, target):
    begin=0
    end=len(seq)-1
    while begin <= end:
        mid= begin + (end-begin)//2
        mid_value = seq[mid]
        if mid_value==target:
            return mid
        elif mid_value<target:
            begin=mid+1
        else:
            end=mid-1
    return None

a=[1,3,4,5,6,7,8,9,10]

print(binary_search(a,1))
