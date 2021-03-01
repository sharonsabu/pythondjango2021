employee=[{"name":"varun","desig":"devop","salary":40000,"join":2000,"resign":2008},
{"name":"ram","desig":"devop","salary":30000,"join":1989,"resign":1995},
{"name":"raju","desig":"qa","salary":28000,"join":2004,"resign":2010},
{"name":"ravi","desig":"qa","salary":32000,"join":2005,"resign":2015},
{"name":"sravan","desig":"mrkt","salary":35000,"join":2010,"resign":2020}
          ]

highest_sal=max(list(map(lambda emp:emp["salary"],employee)))
print(highest_sal_sal)

name_of_max_salary=list(filter(lambda emp:emp["salary"]==mx_sal,employee))
print(name_of_max_salary)

exp_above_8_yrs=list(filter(lambda emp:emp["resign"]-emp["join"]>8,employee))
print(exp_above_8_yrs)
