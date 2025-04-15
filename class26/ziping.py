lst1=[1,2,3,4]
lst2=[6,7,8,9]
print(list(zip(lst1,lst2)))

print(list(zip(lst1,lst2[::-1])))

print(dict(zip(lst1,lst2)))