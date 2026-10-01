
list=[1, 2, 3, 4, 5, 6, 7, 8, 9,10]
left =0
right=len(list)-1
while left<right:
    list[left],list[right]=list[right],list[left]
    left+=1
    right-=1    
print(list)

str="saurabh"
list=list(str)  
left=0
right=len(str)-1
while left<right:
    list[left],list[right]=list[right],list[left]
    left+=1
    right-=1
    # list[left],list[right]=list[right],list[left]

print(list)
