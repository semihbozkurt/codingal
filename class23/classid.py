clas={

"id1":{
"name":"Semih",
"class":"8A",
"lesson":"math,science"
},

"id2":{
    "name":"Ali",
    "class":"4B",
    "lesson":"social studies"
},
"id3":{
    "name":"Ahmet",
    "class":"2C",
    "lesson":"english"
}


}

id=input("write the id of the student: id1,id2 ...\n")
student=clas[id]
want=input("do you want name or class or lesson\n")


remove=[]
for key in student:
    if key!=want:
        remove.append(key)



for i in remove:
    student.pop(i)

print(student)