#strings

name="Shreya"
city="Talwara"
message="hello world"
print(name)
print(city)
print(message)



text="Python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])

print(text[-1])
print(text[-2])


#string slicing

#string[start:end:step]

text="Python"

print(text[1:2])
print(text[1:3:5])
print(text[::-1])


#string concatenation and reptition

first="hello"
second="shreya"
result=first +" "+second
print(result)


text="shreya "
print(text * 3)

#string comparison

str1="apple"
str2="mango"
str3="apple"
print(str1==str3)
print(str1!=str2)
print(str2<str3)
print(str2>str3)

#string methods


#case conversion
text="hello python"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

#removing spaces

text="    Python  "
print(text.strip())
print(text.lstrip())
print(text.rstrip())


#searching methods
text="I love python"
print(text.find("python"))
print(text.find("o"))
print(text.find("C++"))

#replacing text

text="I love Java"
print(text.replace("Java","Python"))

#checking methods
text="Python123"
print(text.isalnum())
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.islower())
print(text.isspace())

#string formatting

#using f string
name="Shreya"
age=20
print(f"My name is {name} and i am {age} years old")

#using format method
name="Shreya"
age=20
print("My name is {} and i am {} years old".format(name , age))

#using % formatting
name="Shreya"
age=20
print("My nme is %s and i am %d years old" %(name,age))

#test
text="Python"
print(text[1:4]) #yth
print(text[-1]) #n

#program to count how many times the letter a appears in "banana"
text="banana"
count=text.count("a")
print(count)

#program to reverse a string

text="python"
reverse=text[::-1]
print(reverse)