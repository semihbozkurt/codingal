dict={



}



def createcont():
    number=input("write the new number")
    name=input("write the name for number")
    if (name and number) not in dict:
        dict[name]=number
    else: print("name and number already exists")

def searchcont():
    try:
        contact=input("write the name of the person")
        print(dict[contact])
    except:
        print("contact not found")

def update():
        name=input("write the name")
        if name in dict:
            newnum=input("write the new number")
            dict[name]=newnum
        else: print("name cant found")
    
def delete():
     name=input("write the name to delete")
     if name in dict:
          dict.pop(name)
     else: print("name dosen't exist")

def show():
     for i in (sorted(dict)):
          print(i,dict[i])


while True:
    print("write the number for operation you want\n--------------")
    operation=input('''
    1. create contact
    2. search for a contact
    3. update a contact
    4. delete a contact
    5. show all contacts
    6. exit
    ''')
    if operation=="1":
         createcont()
    elif operation=="2":
         searchcont()
    elif operation=="3":
         update()
    elif operation=="4":
         delete()
    elif operation=="5":
         show()
    elif operation=="6":
         break
    else:
         print("you need to write the number for operation")


print("Program is finished")
