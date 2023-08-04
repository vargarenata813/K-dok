
age = int(input("Enter your age: "))

def age_check(age):
    if age >= 18: 
        print("You are 18 or older than 18. You can read this article.")
    else:
        print("You are younger than 18. You can't read this article. ")

age_check(age)
