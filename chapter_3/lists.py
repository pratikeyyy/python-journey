marks=[45,45,"pratik",45,65]

print(marks)
print(type(marks))
print(marks[3])
print(len(marks))
print(marks[1:3])

#in python list can store different data types
#list is mutable we can change the value of list

student=["pratik",12,34,"ghaziabad"]
print(student[0])
student[0]="pratik kumar"
print(student)

#list methods
#append method is used to add an element at the end of the list 
list=[1,2,3]
list.append(4)
print(list)

#sort method is used to sort the list in ascending order
list=[3,1,4,2]
list.sort()
print(list)
#sort in descending order
print(list.sort(reverse=True)) 
print(list) 
#reverse
list=[3,1,4,2]
list.reverse()
print(list)

#index

list=[1,2,3,4,5]
list.insert(1,4)
print(list) #returns the index of the first occurrence of the element

  #remove and pop method 
list=[1,2,3,4,5]

list.pop(3)
print(list)

list.remove(5)
print(list)