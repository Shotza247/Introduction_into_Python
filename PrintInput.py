#Defined input values for the system to be able to engage with you.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name:  ")

#This line combine your first and last name
full_name = first_name + " " + last_name

print("Hello " + full_name + ", welcome to the Python world.")

#This is our try-catch block to see if the user has entered the correct input(exception handling)
#The try-catch block also has conditional statements to classify the user by age
try:
    user_age = int(input("Please enter your age: "))
    #teenage years start at thirteen
    if user_age >= 13 and user_age < 18:
        print("Your are a teen.")
    elif user_age >= 18 and user_age <= 25:
        print("Your at an adolescent age. ")
    elif user_age > 25 and user_age <= 31:
        print("Peak young adult")
    elif user_age > 31 and user_age <= 50:
        print("Middle aged adult")
    elif user_age > 50: #For individuals older than 50 retirement
        print("Your already in the retirement range.")
    else:
        print("Invalid age " + str(user_age) + " entered.")
except ValueError:
    print("The input wasn't a valid  number.")