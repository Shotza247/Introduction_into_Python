#using a list with dictionaries
# dict = [] this is a list
# dict = {} this is a dictionary
#dict.append({}) dictionary inside a list
dict = []
icount = 0
dict.append({"empid":100, "name": 'john', 'paycode':6734, 'dept': 'sales', "salary":16250, "monthly tax":3650})
dict.append({"empid":101, "name": 'Ben', 'paycode':4332, 'dept': 'marketing', "salary":10000, "monthly tax":1230})
while icount < len(dict):
    print(dict[0].keys())
    print(dict[icount].values())
    icount+= 1
