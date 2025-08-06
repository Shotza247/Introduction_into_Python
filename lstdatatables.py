#Here you will find code i created for a table for a "Telecom Company" to a list all employees and their data within the list.
#The program has a function to calculate each employees tax deduction and stores it to the list data.
#Later the user is prompted if they want to add a new user/data into the list.
#If yes they'll have to add in the name, department, salary then their tax deduction automatically calculated before printing.

#Defined the dictionary
#dict = {}
#Defined the list components
#lstdict = {"code":""
lstid =[]
lstnames = ["Sarah","Mike","Thabo","Palesa","Mlu","Thandiwe"]
lstdept = ["HR","Finance","Sales","Marketing","ICT","Sales"]
lstsalary = [12456,16500,9567,9863,10345,10000]
lsttaxdeduction = []

#Defined the function to calculate the tax deduction of user_Id(num) based on their salary
def taxrates(num,usersalary):
    #Defined base tax for all users before salary considerations
    taxvalue = 0
    if usersalary <= 10000:
        taxrate = 0.085
    elif usersalary > 10000 and usersalary < 15000:
        taxrate = 0.11
    else:
        taxrate = 0.15
    taxvalue = taxrate * usersalary
    lsttaxdeduction.insert(num,taxvalue)
icount = 0

#lstid.insert(icount,lstnames[icount])
while icount < len(lstnames):
    #insert lstname at index 0 where icount = 0
    lstid.insert(icount,icount) 
    taxrates(icount,lstsalary[icount])
    #insert icount at index 0 = icount
    print("At "+ str(icount) + " ," + lstnames[icount] + ", " + lstdept[icount] + " ," + str(lstsalary[icount]) + ", " + str(lsttaxdeduction[icount]))
    #we print sarah at icount position = 0
    icount += 1
#print(lstnames[icount])
print()
isAppend = True
while isAppend == True:
    response = input("Add new user with data(Yes/No): ")

    if response.upper() == "NO":
        isAppend = False
    else:
            lstid.append(icount)
            name = input("Enter name: " )
            dept = input("Enter department: ")
            salary = int( input("Enter Salary: "))
            
            lstnames.append(name)
            lstdept.append(dept)
            lstsalary.append(salary)
            taxrates(icount,salary)
            
print(lstid)
print(lstnames)
print(lstdept)
print(lstsalary)
print(str(lsttaxdeduction))
