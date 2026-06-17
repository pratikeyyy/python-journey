<<<<<<< HEAD
# Dictionary in Python it is used to store data in key-value pairs. It is a collection which is ordered, changeable and does not allow duplicates. Dictionaries are written with curly brackets, and they have keys and values.
info={"name":"John","age":30,"city":"New York",
      "hobbies": ["pratik","kumar"],
      #nested dictionary
      "subjects": {"math": 90, "science": 85},
      12: 123
      }
print(info)
print(info["name"])
print(info["hobbies"]) 
print(info["subjects"]["math"]) #accessing nested dictionary
info["age"]=12
info["number"]=1234567890
print(info)

#ductionary methods

student={
    "name":"pratik",
    "age": 20, 
    "subjects": ["math", "science", "english"],
}
print(student)
print(list(student.keys())) #to get all keys
print(list(student.values())) #to get all values
print(list(student.get("name"))) #to get value of a specific key
print(student.items()) #to get all key-value pairs
student.pop("age") #to remove a key-value pair  
print(student)
=======
# Dictionary in Python it is used to store data in key-value pairs. It is a collection which is ordered, changeable and does not allow duplicates. Dictionaries are written with curly brackets, and they have keys and values.
info={"name":"John","age":30,"city":"New York",
      "hobbies": ["pratik","kumar"],
      #nested dictionary
      "subjects": {"math": 90, "science": 85},
      12: 123
      }
print(info)
print(info["name"])
print(info["hobbies"]) 
print(info["subjects"]["math"]) #accessing nested dictionary
info["age"]=12
info["number"]=1234567890
print(info)

#ductionary methods

student={
    "name":"pratik",
    "age": 20, 
    "subjects": ["math", "science", "english"],
}
print(student)
print(list(student.keys())) #to get all keys
print(list(student.values())) #to get all values
print(list(student.get("name"))) #to get value of a specific key
print(student.items()) #to get all key-value pairs
student.pop("age") #to remove a key-value pair  
print(student)
>>>>>>> d67ac7aee57f1d35588c2033e52be7ce6d9e4a72
