even=[]
odd=[]
lst=[1,2,3,4,5,6,7,8,9]
for i in lst:
    if i%2==1:
        odd.append(i)
    elif i%2==0:
        even.append(i)
print("even:",even,"\n odd:",odd)

#shorter way:
evenlst=[x for x in lst if x%2==0]
oddlst=[a for a in lst if a%2==1]

print("---------------------")
print("even list:",evenlst)
print("odd list:",oddlst)


#squer dictionary:

sqrdict={x :x**2 for x in [1,2,3,4,5,6,7,8,9]}
print(sqrdict)

#map

lst1=[1,2,3,4,5]
def mycalc(a):
    return a*2-3

#   using  mycalc on lst1
res=list(map(mycalc,lst1))
print(res)


#zip

lst2=["alice","bob","james","ingrid"]
lst3=[1,2,3,4]

zipedlst=list(zip(lst2,lst3))
print(zipedlst)

#exit

print(1)
exit()
print(1)
print(2)