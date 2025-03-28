print("welcome to the quiz show")

score=0

q1=input("what is the square root of 25")
if q1=="5":
    print("True")
    score+=10
else:
    print("false")
    print("true answer is: 5")
    score-=5


q2=input("what is the capital city of Norway")
q2=q2.upper()
if q2=="OSLO":
    print("True")
    score+=10
else:
    print("false")
    print("true answer is Oslo")
    score-=5

q3=input("what is the capital city of Canada")
q3=q3.upper()
if q3=="TORONTO":
    print("True")
    score+=10
else:
    print("false")
    print("true answer is: Toronto")
    score-=5

q4=input("what is the name of the 10. element in the periodic table")
q4=q4.upper()
if q4=="NEON":
    print("True")
    score+=10
else:
    print("false")
    print("true answer is: neon")
    score-=5

q5=input("how many caragorie of organizims are there ")
if q5=="4":
    print("True")
    score+=10
else:
    print("false")
    print("true answer is: 4")
    score-=5

if score<=0:
    print("you loose")
else:
    print("your score is:",score)