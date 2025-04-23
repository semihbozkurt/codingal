lst=["semih","ali","veli"]

search=input("what do you want to search for?")

for i in range(len(lst)):
    if lst[i]==search:
        print(i)