#print elements

nums=[1,4,9,16,25,36,64,81]

for el in nums:
    print(el)

#search for a number

nums=[1,23,4,45,45,54,3,332,554,646,546]
x=3

idx=0
for el in nums:
    if(el==x):
        print("number found",idx)
    idx=+1  

    #sum of first n numbers

n = 5

sum =  0
for i in range(1,n+1):
    sum += i
print("total",sum)


#factorial

n = 5
fact=1

for i in range(1,n+1):
    fact*= i
print("factorial",fact)
