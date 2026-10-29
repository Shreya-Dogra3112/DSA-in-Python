#syntax = list_name = [item1 , item2 , item3]


fruits=["Apple","Banana","Mango","Orange"]

print(fruits)
print(type(fruits))

#list of integers
numbers = [10,20,30,40]

#list of strings
fruits=["Apple","Banana","Mango","Orange"]


#mixed datatypes
data=[10,"Python",3.5,True]

print(numbers)
print(fruits)
print(data)

#Accessing list elements

fruits=["Apple","Banana","Mango","Orange"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])

#len()
fruits=["Apple","Banana","Mango","Orange"]
print(len(fruits))


#list slicing

#syntax
#list_name[start:end:step]


numbers=[10,20,30,40,50,60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])


#updating list elements

fruits=["Apple","Banana","Mango"]
fruits[1]="Orange"
print(fruits)

#deleting elements
numbers=[10,20,30,40]
del numbers[1]
print(numbers)

#removing elements

fruits=["Apple","Banana","Mango"]
fruits.remove("Banana")
print(fruits)


#append()
numbers=[10,20,30]
numbers.append(40)
print(numbers)

#extend()
numbers=[10,20]
numbers.extend([30,40])
print(numbers)

#insert()
fruits=["apple","mango"]
fruits.insert(1,"Banana")
print(fruits)

#remove
numbers=[10,20,30,20]
numbers.remove(20)
print(numbers)

#pop()
numbers=[10,20,30]
x=numbers.pop()
print(x)

#clear
numbers=[10,20,30]
numbers.clear()
print(numbers)

#index()
fruits=["Apple","Banana","Mango"]
print(fruits.index("Banana"))

#count()
numbers=[10,20,10,30,10]
print(numbers.count(10))

#sort()
numbers=[40,10,30,20]
numbers.sort()
print(numbers)

#reverse
numbers=[10,20,30,40]
numbers.reverse()
print(numbers)

#nested list
students=[
    ["Aman",20],
    ["Shreya",21],
    ["Riya",22]
]
print(students)

#assessing elements
students=[
    ["Aman",20],
    ["Shreya",21],
    ["Riya",22]
]
print(students[0])
print(students[1][0])
print(students[2][1])


#nested loops
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for item in row:
        print(item,end=" ")
    print()


#len()
numbers=[10,20,30,40]
print(len(numbers))

#max()
numbers=[10,20,30,50]
print(max(numbers))

#min()
numbers=[10,20,30,50]
print(min(numbers))

#sum()
numbers=[10,20,30,50]
print(sum(numbers))

#sorted()
numbers=[10,1,6,9]
print(sorted(numbers))
prin(numbers)

#list()
text="Python"
characters=list(text)
print(characters)



