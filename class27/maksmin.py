lst1=[10,7,27,1,90]
if lst1[0]<lst1[1]:
    min=lst1[0]
    maks=lst1[1]

elif lst1[0]>lst1[1]:
    min=lst1[1]
    maks=lst1[0]

elif lst1[0]==lst1[1]:
    min=lst1[0]
    maks=lst1[1]

for i in range(2,len(lst1)):
    if lst1[i]>maks:
        maks=lst1[i]

for i in range(2,len(lst1)):
    if lst1[i]<min:
        min=lst1[i]

print(maks)
print(min)