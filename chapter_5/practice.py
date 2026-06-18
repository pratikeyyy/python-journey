#print numbers from 1 to 100

i=1
while i <=100 :
    print(i)
    i+=1

#print numbers from 100 to 1 

i=100
while i >= 1  :
    print(i)
    i-=1

#multiplication of n

n= int(input("enter number :"))
i=1
while i<=10:
    print(i*n)
    i+=1

#print the list
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(nums) :
    print(nums[idx])
    idx +=1

#search for a number

nums=(1,4,9,16,25,36,49,64,81,100)

x=36

i=0
while i < len(nums):
    if(nums[i]==x):
        print("founded",i)
    else:
        print("not found")
    i+=1



#sum of first n numbers

n = 5
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("total",sum)
