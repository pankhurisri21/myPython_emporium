
mylist = [25,39,40,57,63,88,43,54,23,21,46]
num = int(input("Enter the element to be searched"))
len = len(mylist)
mylist.sort()
print(f"Sorted list : {mylist}")


#function definition
def binary_search(mylist,lower,upper):
    
    mid_pos = (lower+upper)//2
    mid = mylist[mid_pos]
    
    if upper >= lower :
        if num == mid:
            return mid
        elif num < mid:
            return binary_search(mylist,lower,mid_pos-1)  

        elif num > mid:
            return binary_search(mylist,mid_pos+1,upper) 

    else:
        return -1

#function call
result = binary_search(mylist,0,len-1)

if result == -1:
    print("Element is not in the list")
else:
    mid_pos = mylist.index(result)
    print(f"Element {num} is found at position : {mid_pos}")    
