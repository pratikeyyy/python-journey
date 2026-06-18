#break used to terminate the loop when encounered
i=1
while i <= 5:
    print(i)
    if(i==3):
        break
    i +=1

print("end of loop")

#continue terminate current iteration and continue execution of loop

i=0
while i <= 5:
   
    if(i==3):
        i+=1
        continue
    print(i)
    i +=1

#by using for and range 

#print 1 to 100
for i  in range(1,101):
       print(i)

# print 100 to 1
for i in range(100,0,-1):
       print(i)


#multiplication

n=int(input("enter ur numbe:"))
for i in range(1,11):
     print(n*i)