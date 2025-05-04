course = "Python for beginners"

upper_case = course.upper()
print("Object to Uppercase: " + upper_case)

lower_case = course.lower()
print("Object to lowercase: " + lower_case)

find_for = course.find("n")
print("First n is found at this index: " + str(find_for))

replace_for = course.replace("for","by")
print("Replaced for with by: " + replace_for)

lookup_word = input("Enter a letter/word to search: ")

if lookup_word in course:
    print("The word/letter: " + lookup_word + " exists in our course object")
else:
    print("No such word/letter exists in course object")