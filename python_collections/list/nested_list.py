employees=[
    [100,"tom","developer",25000,1989,1999],
    [101,"jack","developer",18000,1990,2005],
    [102,"jhon","ba",28000,1975,1988],
    [103,"dinu","qa",26000,1990,1999]
]

for emp in employees:
    print(emp[1])    #prints only the name of employees
print("")

for emps in employees:
    if (emps[2]=="developer"): #prints name of employees whose designation is developer
        print(emps[1])
print("")

#prints total salary
tot=0
for emply in employees:
    tot+=emply[3]
print(tot)
print("")

#highest salary

sal_list=[]
for empp in employees:
    sal_list.append(empp[3])
#print(sal_list)  #prints the list of salaries alone
print(max(sal_list))
print("")

#to find the highest experience from the list and print full details of that person
exp=[]
for num in employees:
    exp.append(num[5]-num[4])
print(exp)
print(max(exp))






