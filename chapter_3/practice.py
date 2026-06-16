#to store name of mocies in list
favmovie1=input("enter your favourite movie name 1 :")
favmovie2=input("enter your favourite movie name 2:")
favmovie3=input("enter your favourite movie name 3: ")
movies=[favmovie1,favmovie2,favmovie3]
print(movies)

#list contain palindrome

list1=[1,2,3]
list2=[1,2,1]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("list1 is palindrome")
else:  
     print("list1 is not palindrome")
