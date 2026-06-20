#sep=" " to give space between the word written in print
 
print("pratik",'KUMAR')

#end="\n" to move in other lines if use in print then at same line

print("pratikkk")
print("kumar")


print("pratikkk", end="@@@")
print("kumar")

#len(
#range()
#type()
#some moere inbuilt fn

#user defined

#default paarmeter
def cal_prod(a=45,b=54):
   
    print(a*b)
    return a*b

cal_prod()

def cal_prod(a,b=54):
   
    print(a*b)
    return a*b

cal_prod(12)