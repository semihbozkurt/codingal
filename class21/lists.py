#empty list:
lst=[]

# list with elements:
# numbers start from 0:
#   no:  0 1 2    3      4   5
lst=    [1,2,3,"Semih",True,1.7]
print(lst)

#if you multiplicate a list it will write the same list 
print(lst*2)


#learning the length of list:
print(len(lst))


#you can reverse it:
lst.reverse()
print("reversed list:",lst)

# re reversing :
lst.reverse()

# appending (adding) elements to the list:
newele=input("write the new element: ") #this element will be string
lst.append(newele)
print("list:",lst)

#pop removes the last element

lst.pop()
print("last element removed",lst)

#you can pop the element you vant by giving the number to pop
lst.pop(2)
print("number 2 removed",lst)

#you can remove a element by giving its name to remove:
lst.remove("Semih")
lst.remove(True)
print("Semih and True removed",lst)
