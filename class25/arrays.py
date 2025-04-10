import array

#arrays stores onley 1 data type that you give it
#                 i means integer
arr1=array.array("i",[1,2,3,4,40,785])
print(arr1)

#adds the number to the last:
arr1.append(11)
# insert adds second number to first numbers index:
# add 16 to first index:
arr1.insert(1,16)

print(arr1)

arr2=array.array("i",[1,3,2,3,4,3,5,3,6,3])
count=0
for i in range(len(arr2)):
    if arr2[i]==3:
        count+=1
print("number of 3 es in arr2 is: ",count)
