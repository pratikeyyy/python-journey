#length of list

cities=["delhi,","mumbai","gurugram","chennai"]
heroes=["thor","iron man","spider man"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

def print_list(list):
    for item in list:
        print(item,end="")


print_list(heroes)
print()

#factorial

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)

cal_fact(5)
cal_fact(32)

#usd to inr

def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"usd=",inr_val,"inr")

converter(23)

#num=int(input("enter ur number:"))

def num(n):
   if n%2==0:
         print(n,"even")
   else:
       print(n,"odd")     

num(15)
num(18)