dict={
"semih":"15",
"ali":"14",
"veli":"16",
"kerem":"14",
"hasan":"14"
}
print(dict,end="\n\n")

wanting=input("which age do you want to find the frequancy of ")
count=0
for value in dict.values():
    if value==wanting:
        count+=1
print(count)
