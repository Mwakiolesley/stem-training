#if statement
x=0
if x >=1:
    print("Hey , im still here")
    x-=1
    print(x)
print ("done")
#else statement 
x=10
if x==10:
    print(x)
else :
    print("not 10")
#elif to create grading system
grad= int(input("write student score: "))
if grade >80 and grade <=100 :
    print("student got an A")
elif grade >=70 and grade < 80 :
    print(" student got a B") 
