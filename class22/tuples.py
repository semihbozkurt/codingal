tpl=(1,2,3,4,"Semih",True,"Semih",3,"ali",3,False)
tplint=(1,2,22,99,53)

newtpl=tplint + (9,)
print(tplint,"---",newtpl)

#tpl.append(1)         there is no such code

lst=[1,2,3,4,"Semih",False]

lst.append("semih")
print(lst)

#you can change the lists but
#you can't change tuples
print(len(tpl))

print(tpl[::-1])

count=0
element=True     #element we are searching for
for i in range(len(tpl)):
    if type(element) is bool:                   #if type is boolean
        if str(element)==str(tpl[i]):          #check with all elements in tuple
            count+=1                               #if they matches increase count by 1
        continue                                #don't look to down if element is boolean

    if tpl[i]==element:               #look hear if element is not a boolean
        count+=1
    
print("number of elements:",count)

