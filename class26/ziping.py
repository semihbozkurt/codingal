lst1=[1,2,3,4]
lst2=[6,7,8,9]
#zip
print(list(zip(lst1,lst2)))
#2. list reversed
print(list(zip(lst1,lst2[::-1])))
#dictionary
print(dict(zip(lst1,lst2)))
