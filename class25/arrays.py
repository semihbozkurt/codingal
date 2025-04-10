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