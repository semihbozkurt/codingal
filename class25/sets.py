set1={1,2,3,4,5,5}
set2={4,5,6,7,8}
print(set1)
print(set2)

set1.add(986)

# union, intersection, difference, simetricdifference

#union:
print(set1|set2)
print(set1.union(set2))

#intersection:
print(set1&set2)
print(set1.intersection(set2))

#difference>
print(set1-set2)
print(set1.difference(set2))

#symmetric difference
print(set1^set2)

lst=[1,2,3,40,257]

set3=set(lst)
print (set3)

set4={"semih","ali",True,2.4,209}

set5={0,1,2,3}
#pop deletes the first caracter:
set5.pop()

print("---------")
print(f"{set1}\n{set2}\n{set3}\n{set4}\n{set5}")

