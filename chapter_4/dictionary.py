# Dictionary in Python it is used to store data in key-value pairs. It is a collection which is ordered, changeable and does not allow duplicates. Dictionaries are written with curly brackets, and they have keys and values.
info={"name":"John","age":30,"city":"New York",
      "hobbies": ["pratik","kumar"],
      "subjects": {"math": 90, "science": 85},
      12: 123
      }
print(info)
print(info["name"])
print(info["hobbies"]) 
 
info["age"]=12
print(info)