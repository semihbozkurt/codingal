#numbers can also go from the end
#  no:    -6     -5     -4    -3    -2   -1   
lst=   ["abc","aba","123","semih","a","1221"]

length=len(lst)
num=0

for i in range (1,length):
    if lst[i][0]==lst[i][-1]  and  len(lst[i])>1:
        num+=1
    

print(num)
