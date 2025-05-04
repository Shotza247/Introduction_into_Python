first_name = input("Enter your first name: ")
last_name = input("Enter your last name:  ")

full_name = first_name + " " + last_name

print("Hello Python World, I'm " + full_name)

try:
    user_age = int(input("Please enter your age: "))
    #teenage years start at thirteen
    if user_age >= 13 and user_age < 18:
        print("You are a teen.")
    elif user_age >= 18 and user_age <= 25:
        print("Your at an adolescent age. ")
    elif user_age > 25 and user_age <= 31:
        print("Peak young adult")
    elif user_age > 31 and user_age <= 50:
        print("Middle aged adult")
    elif user_age > 50: #For individuals older than 50
        print("Your old.")
    else:
        print("Invalid age " + str(user_age) + " entered.")
except ValueError:
    print("The input wasn't a valid  number.")