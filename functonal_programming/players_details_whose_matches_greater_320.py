players=[{"name":"sachin","matches":500,"rank":1},
{"name":"dravid","matches":450,"rank":12},
{"name":"sehwag","matches":250,"rank":52},
{"name":"msd","matches":360,"rank":7}]

mat=list(filter(lambda dict:dict["matches"]>320,players))
print(mat)

#print names whose matches are greater than 320
nm=list(map(lambda dict:dict["name"],mat))
print(nm)


#print emp names whose desgntn=dveloper
#print emp details whose exp greater than 2
#print count of empls whose desgn=quality analyst
#qacccnt=len(list(filter(lambda emp:emp.design=="quality analyst",employees)))