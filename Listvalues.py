icount = 0
lstname = ["John","Sammy","Sarah","Linda"]
#Python is case sensitive
print(lstname)
lstname[1] = "Sammie"

while  icount < len(lstname):
    print(lstname[icount])
    icount += 1

lstname.append("Miller")
print(lstname)

lstname.insert(1,"Sharon")
print(lstname)

lstname.remove("Miller")
print(lstname)

#Lets check if sharon is in our list
searchname = input("Search for: ")
if searchname in lstname:
    print(f"The name was found: {searchname}")

else:
    print("Not Found: " + searchname)
print("length of list Items:" + str(len(lstname)))

for item in lstname:
    print(item)
