<<<<<<< HEAD
# Set in Python is used to store multiple items in a single variable. It is a collection which is unordered, unindexed and does not allow duplicate values. Sets are written with curly brackets.
collection={1,2,3,4,5,2,345,3,8,"hello","world","hello"}
print(collection) #it will remove duplicate values and print unique values only
print(type(collection)) #to check the type of collection
print(len(collection)) #to check the length of collection
#empty set
empty_set=set()
print(empty_set)
print(type(empty_set))

#set methods
my_set={1,2,3}
print(my_set)
my_set.add(4) #to add an element to set
print(my_set)
my_set.update([5,6,7]) #to add multiple elements to set
print(my_set)
my_set.remove(3) #to remove an element from set
print(my_set)
my_set.discard(10) #to remove an element from set if it exists, if it does not exist it will not raise an error
print(my_set)
my_set.clear() #to remove all elements from set
print(my_set)
#union of sets
set1={1,2,3}
set2={3,4,5}
union_set=set1.union(set2) #to get the union of two sets
print(union_set)
=======
# Set in Python is used to store multiple items in a single variable. It is a collection which is unordered, unindexed and does not allow duplicate values. Sets are written with curly brackets.
collection={1,2,3,4,5,2,345,3,8,"hello","world","hello"}
print(collection) #it will remove duplicate values and print unique values only
print(type(collection)) #to check the type of collection
print(len(collection)) #to check the length of collection
#empty set
empty_set=set()
print(empty_set)
print(type(empty_set))

#set methods
my_set={1,2,3}
print(my_set)
my_set.add(4) #to add an element to set
print(my_set)
my_set.update([5,6,7]) #to add multiple elements to set
print(my_set)
my_set.remove(3) #to remove an element from set
print(my_set)
my_set.discard(10) #to remove an element from set if it exists, if it does not exist it will not raise an error
print(my_set)
my_set.clear() #to remove all elements from set
print(my_set)
#union of sets
set1={1,2,3}
set2={3,4,5}
union_set=set1.union(set2) #to get the union of two sets
print(union_set)
>>>>>>> d67ac7aee57f1d35588c2033e52be7ce6d9e4a72
