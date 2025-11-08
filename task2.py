list=[1,2,3,4,5,6,7,8,9,0]
i=0
ext_list=[]
while (i<5):
    ext_list.append(list[i])
    i=i+1
rev_list=[]
for i in range(4,-1,-1):
    rev_list.append(ext_list[i])

print("Original list :",list)
print("Extracted first five elements :",ext_list)
print("Reversed extracted elements :",rev_list)    
