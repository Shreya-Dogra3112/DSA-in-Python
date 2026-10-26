#if
age=3
if(age<5):
    print("Toddler")

#if-else
age = 16
if(age>=18):
    print("Eligible to vote")
else:
    print("Not eligible")

#if-elif-else

marks=85
if(marks>90):
    print("Grade:A")
elif(marks>80):
    print("Grade:B")
else:
    print("Fail")


#nested if
age=20
has_id=True
if(age>=18):
    if has_id:
        print("Allowed")
    else:
        print("Not allowed")
else:
    print("Not allowed")

