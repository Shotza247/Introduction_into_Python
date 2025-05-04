# StartingIntoPython
Here is a collection of my first python programs I developed using a mobile application to understant th theory behind python and the common key functions,methods, and keyowrds, to kickstart my python journey.

##The mobile app used for learning is Python Coding, and the IDE/Compiler i used to run and test these code is Python 3. 
##Bare in mind that I started on my mobile phone after I was blessed with a new machine, I couldn't wait to dive deeper into Python.

So I'll first start with my developed python codes:
--This was created a few hours after understanding the fundementals of python and what Pc or mobile installations were required.
--After these few hours of learning I was already testing out ideas because I have an understanding of C# coding

#####
One of the most interesting things about learning a new language/system is getting to understand the basics such as syntax,.
####

**1.PrintInput.py**
----------------------
#Here is an analysis of my first Python code, highlighting the most important aspects of my foundations in python:

### 1. **User Input**
   - The code uses the `input()` function to collect user input for the first name, last name, and age.
   - python code:
     first_name = input("Enter your first name: ")
     ```

### 2. **String Concatenation**
   - The `+` operator is used to concatenate strings to form the full name and display a greeting.
   - python code:
     full_name = first_name + " " + last_name
     print("Hello Python World, I'm " + full_name)
     ```

### 3. **Type Conversion**
   - The `int()` function is used to convert the user's age input (a string) into an integer for comparison.

### 4. **Conditional Statements**
   - The code uses `if`, `elif`, and `else` statements to categorize the user's age into different life stages.

### 5. **Error Handling**
   - A `try-except` block is used to handle invalid input (e.g., non-numeric values for age). If the input cannot be converted to an integer, a `ValueError` is caught, and an error message is displayed.
   - python code:
     try:
         user_age = int(input("Please enter your age: "))
     except ValueError:
         print("The input wasn't a valid  number.")
    

### 6. **Logical Operators**
   - Logical operators like `and` are used to define ranges for age categories.
   - python code:
     if user_age >= 13 and user_age < 18:

This code gave me a good basic of Python programming concepts like input handling, conditionals, and error handling.

**2.stringMethods.py**
--------------------------
   - python code:
     course = "Python for beginners"
-String Methods: Uses upper(), lower(), find(), and replace() to manipulate the course string.
-User Input: Accepts a letter/word to search in the string.
-Substring Check: Uses the in operator to verify if the input exists in the string.
-Conditional Logic: Outputs appropriate messages based on the presence of the input in the string.
-Output: Prints results of string manipulations and search outcomes.

**3.simpleMaths.py**
--------------------------
   - python code:
     x = (10 -5) + 3 * 10 / 2
This code demonstrates basic arithmetic operations in Python, including addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`). It also evaluates a compound expression using operator precedence. The results of these calculations are printed to the console.

**4.range.py**
-------------------
   - python code:
    for number in range(1,20,2):
    print(number * "*")
    # range is used to store a range of numbes 1 to 19 and stepping over a number by 2
# Output
*
***
*****
*******
*********, etc.

**5.whileloopPyramid.py**
-------------------
# creating two right angle tringles opposite each other, looking like an isosceles triangle
# Output
*
***
*****
*******
*********
*******
*****
***
*

**6.listvalues.py**
-------------------
# This code demonstrates basic list operations in Python, including updating elements, appending, inserting, removing, searching, and iterating through a list. It also checks the list's length and uses both `while` and `for` loops for iteration. It highlights foundational list manipulation techniques.

**7.Listdatatables.py**
------------------------
Here’s a detailed analysis of my code:

### **Purpose**
The code manages employee data using multiple lists (`lstnames`, `lstdept`, `lstsalary`, and `lstid`) to store names, departments, salaries, and IDs. It allows users to add new employees interactively and displays the data in a structured format.

---

### **Key Components**

#### **a. Lists for Data Storage**
- Multiple lists are used to store different attributes of employees:
  - `lstnames`: Stores employee names.
  - `lstdept`: Stores employee departments.
  - `lstsalary`: Stores employee salaries.
  - `lstid`: Stores employee IDs, which are generated dynamically.

#### **b. User Interaction**
- The program uses a `while` loop to allow users to add new employee data interactively:
  ```python
  response = input("Add new user with data(Yes/No): ")
  if response.upper() == "NO":
      isAppend = False
  ```
  - Users can input the name, department, and salary for new employees.
  - The data is appended to the respective lists.

#### **c. Dynamic ID Generation**
- Employee IDs are dynamically generated using the `icount` variable, which increments with each new entry:
  ```python
  lstid.append(icount)
  ```

#### **d. Data Display**
- A second `while` loop iterates through the lists and prints the employee data in a structured format:
  ```python
  print("At "+ str(icount) + " ," + lstnames[icount] + ", " + lstdept[icount] + " ," + str(lstsalary[icount]))
  ```

---

### Features**

1. **Data Input and Storage**:
   - The program collects employee data (name, department, salary) and stores it in separate lists.
   - It uses `input()` for user interaction.

2. **Dynamic Data Handling**:
   - New data can be appended to the lists dynamically during runtime.

3. **Data Display**:
   - The program displays all employee data in a readable format, showing the ID, name, department, and salary.

4. **List Operations**:
   - `append()`: Adds new data to the lists.
   - `insert()`: Inserts IDs into the `lstid` list at specific positions.
   
```python
# Refactored Code
employees = []
is_append = True

while is_append:
    response = input("Add new user with data (Yes/No): ")
    if response.upper() == "NO":
        is_append = False
    else:
        name = input("Enter name: ")
        dept = input("Enter department: ")
        salary = int(input("Enter salary: "))
        emp_id = len(employees)  # Generate ID based on current list length
        employees.append({"id": emp_id, "name": name, "dept": dept, "salary": salary})

# Display employee data
for emp in employees:
    print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['dept']}, Salary: {emp['salary']}")
```
### Summary
This code demonstrates foundational concepts like list manipulation, user interaction, and dynamic data handling. While it works well for basic use cases, refactoring to use a more structured data format (like dictionaries) would improve readability, scalability, and maintainability.

**7.dictionaries(kvpairs)**
--------------------------
Dictionary Creation:

A dictionary tinydict is created with key-value pairs representing employee data (e.g., empid, name, paycode, etc.).
Accessing Keys:

The keys() method is used to retrieve all the keys in the dictionary:
Accessing Values:

The values() method is used to retrieve all the values in the dictionary:
Short Description
This code demonstrates basic dictionary operations in Python, including creating a dictionary with key-value pairs and retrieving its keys and values using the keys() and values() methods.

**8.addDict2List.py**
-------------------
# A list can hold dictionaries as its elements, allowing you to store multiple key-value pairs in an organized way. This is useful for managing structured data, such as employee id,name,department,and salary, where each dictionary represents an individual entity.