
dict = {}
#lstdict = {"code":""
lstid =[]
lstnames = ["Sarah","Mike","Thabo","Palesa","Mlu","Thandiwe"]
lstdept = ["HR","Finance","Sales","Marketing","ICT","Sales"]
lstsalary = [12456,16500,9567,9863,10345,10000]

icount = 0


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
            
#print(lstid)
#print(lstnames)
#print(lstdept)
#print(lstsalary)

#lstid.insert(icount,lstnames[icount])
while icount < len(lstnames):
    #insert lstname at index 0 where icount = 0
    lstid.insert(icount,icount) 
    #insert icount at index 0 = icount
    print("At "+ str(icount) + " ," + lstnames[icount] + ", " + lstdept[icount] + " ," + str(lstsalary[icount]))
    #we print sarah at icount position = 0
    icount += 1
#print(lstnames[icount])