#Defined a system that shows the capabilities of the methods of the list

#Define the list of names
lstname = ["John","Sammy","Sarah","Linda"]

#Python is case sensitive, print the list of names
print(lstname)

#Different ways of adding a new user into the list at a specific position
#place Sammie at index 1 this replaces the individual at index 1
lstname[1] = "Sammie"
print(lstname)
#Place sharon at index 1 this doesn't replace the individual at index 1
lstname.insert(1,"Sharon")
print(lstname)

#print all the names in the list
icount = 0
while  icount < len(lstname):
    print(lstname[icount])
    icount += 1

#Add in a new name to the end of the list 
lstname.append("Miller")
#Print the list of names to show that the new name is added
print(lstname)

#Remove the name Sharon in the list
lstname.remove("Sharon")
print(lstname)

#Lets check if any name is in our list
searchname = input("Search for: ")
if searchname in lstname:
    print(str(lstname.find(searchname)))
else:
    print(searchname + ", does not")

print("length of list Items:" + str(len(lstname)))

