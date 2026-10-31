student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
print(student)


#creating a dictionaries

student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
print(student)

#accessing values using keys
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
print(student["name"])
print(student["roll no"])

#using get()

student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
print(student.get("name"))
print(student.get("course"))

#finding the number of items

student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
print(len(student))

#adding a new element

student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
student["city"]="Talwara"
print(student)

#updating an existing element
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
student["roll no"]=20
print(student)

#using update() method
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
student.update({"roll no": 20})
print(student)

#using pop()
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
student.pop("roll no")
print(student)

#using popitem()
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
student.popitem()
print(student)

#using del()
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
del student["roll no"]
print(student)

#using clear()
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
student.clear()
print(student)

#keys()
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
print(student.keys())

#values
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
print(student.values())

#items()
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
print(student.items())

#copy
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
new_student=student.copy()
print(new_student)

#setdefault()
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
student.setdefault("city","Talwara")
print(student)

#fromkeys()
subjects=("Python","java","linux")
result=dict.fromkeys(subjects,0)
print(result)

#looping through keys
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
for key in student:
    print(key)

#looping through values
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
for value in student:
    print(value)

#looping through key value pairs
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
for key,value in student.items():
    print(key,value)

#nested dictionaries

students={
    "student1":{
        "name":"Aman",
        "age":20
    },
    "student2":{
        "name":"Riya",
        "age":21
    }
}
print(students)

#accesing nested dictionary values
students={
    "student1":{
        "name":"Aman",
        "age":20
    },
    "student2":{
        "name":"Riya",
        "age":21
    }
}
print(students["student1"]["name"])
print(students["student2"]["age"])

#updating nested dictionary values
students={
    "student1":{
        "name":"Aman",
        "age":20
    },
    "student2":{
        "name":"Riya",
        "age":21
    }
}
students["student1"]["age"]=22
print(students["student1"])

#looping through a nested dictionary 
students={
    "student1":{
        "name":"Aman",
        "age":20
    },
    "student2":{
        "name":"Riya",
        "age":21
    }
}
for key , value in students.items():
    print(key)
    print(value)

#built in function of dictionary 
student={
    "name":"Shreya",
    "roll no":19,
    "course":"BCA"
}
print(len(student))
print(str(student))
print(type(student))
print(max(student))
print(min(student))
