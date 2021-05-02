var student={sid:100,name:"amal",course:"Bcom",total:96}

console.log(student["name"])
console.log(student["total"]);

console.log("gender" in student)
console.log(" ")

student["gender"]="male"
console.log(student);
console.log(" ");


//iteration
for(let k in student)
{
    console.log(k+"->"+student[k]);
}

