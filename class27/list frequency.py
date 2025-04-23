lst=["semih","semih","semih","ali","ali","veli"]


dict={}


for i in lst:
    if i not in dict:
        dict.update({i:1})
    else:
        dict[i]= dict.get(i) + 1
        
print(dict)



    