#store words in a python dictionary
word={"table":"a piece of furniture","list of facts "
      "cat":"a small animal"}
print(word)

#no. of classrooms
subjects={
    "python","java","c",
"python","java","c"
}
print(len(subjects))

#marks
marks={}

x=int(input("enter phy : "))
marks.update({"phy" : x})
x=int(input("enter chem : "))
marks.update({"chem" : x})
print(marks)