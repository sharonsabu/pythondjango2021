#create a dict that contains keys id, name, desig, salary
#print empl name
#emply salary
#chck if gender key is there if not add gender key value pair
#iterate all key value pairs

employee={"id":1000,"name":"sha","desig":"tester","salary":58000}

print(employee["name"])

print(employee["salary"])

if "gender" in employee:
    print("gender exist")
else:
    employee["gender"]="female"
print(employee)
print("")

for k,v in employee.items():
    print(k,"",v)

