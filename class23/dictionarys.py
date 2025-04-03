dict={

"sun": "gunes",
"moon": "ay",
"man":"adam",
"earth":"dunya"

}

word=input("enter the word to see it in Turkish: ")

#print(dict[word])    #this will give error if word not found

print(len(dict))

print(dict.get(word,"cant found in turkish dictionary ")) #this will say the thing we write if it cant find the word

dict["sky"]= "gokyuzu"
print(dict.get(word,"not found"))


for key,value in dict.items():    #you can write only key or value
    print("key is: ",key,"/","value is:",value)

