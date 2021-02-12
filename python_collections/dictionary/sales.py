expens={"jan":28000,"feb":30000,"march":40000,"april":38000,"may":35000}

#to know the expense of feb
print(expens["feb"])
print("")

#updation (updating value of april by reducing 2000 from it)
expens["april"]-=2000
print(expens)
print("")

#adding new key-value pair
expens["june"]=45000
print(expens)
print("")

#searching for a key

#chck for july entry if not add july=52000
if "july" in expens:
    print("entry exist")
else:
    expens["july"]=52000
print(expens)
print("")

#to know all the keys and values
for k,v in expens.items():
    print(k,"",v)
