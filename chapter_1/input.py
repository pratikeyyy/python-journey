
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + "! You are " + age + " years old.")

val=input("Enter a number: ")
print(type(val))
#gives string as output because input function takes input as string by default.
val=int(input("Enter a number: "))
print(type(val))
#gives integer as output because we have typecasted the input to integer using int() function.