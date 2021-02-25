players=[{"name":"sachin","matches":500,"rank":1},
         {"name":"dravid","matches":450,"rank":12},
         {"name":"sehwag","matches":250,"rank":52},
         {"name":"msd","matches":360,"rank":7}]

names=list(map(lambda dict:dict["name"],players))
print(names)
rk=list(map(lambda dict:dict["rank"],players))
print(rk)