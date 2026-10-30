#syntax
#tuple_name = (item1,item2,item3)

fruits=("Apple","Mango","Banana")
print(fruits)
print(type(fruits))

single=(10,)
print(type(single))

#tuple of integers

numbers=(10,20,30,40)

#tuple of strings

fruits=("Apple","Mango","Banana")

#Mixed datatypes

data=(10,"Python",3.5,True)
print(numbers)
print(fruits)
print(data)


#Accessing tuple elements
fruits=("Apple","Mango","Banana")
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])

#finding length of a tuple
numbers=(10,20,30,40)
print(len(numbers))

#slicing
#tuple_name[start:end:step]
numbers=(10,20,30,40)
print(numbers[0:3:1])
print(numbers[0:3:])
print(numbers[::-1])
print(numbers[-1:-2])

#tuple operations

#concatenation
t1=(10,20,30)
t2=(20,50,60)
result=t1+t2
print(result)

#repitition
numbers=(10,20)
print(numbers *3)

#membersip operators
fruits=("Apple","Mango","Banana")
print("Apple" in fruits)
print("Litchi" not in fruits)

#comparison
t1=(10,20,30)
t2=(10,20,40)
print(t1==t2)
print(t1<t2)

#tuple methods
#count()
numbers=(10,20,10,20,10,10)
print(numbers.count(10))

#index
fruits=("Apple","Mango","Banana")
print(fruits.index("Banana"))

#built in functions with tuple
numbers=(10,20,30,40,50)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

#looping through tuples

fruits=("Apple","Mango","Banana")
for i in fruits:
    print(i)
#while loop
numbers=(1,2,3,4)
i=0
while(i<len(numbers)):
    print(i)
    i+=1

#tuple packing
student="Shreya",20,"BCA"
print(student)

#tuple unpacking
student=("Shreya","BCA",20)
name,course,age=student
print(name)
print(course)
print(age)


#practice
t1=(10,20,30,40,50)
print(t1[2])

