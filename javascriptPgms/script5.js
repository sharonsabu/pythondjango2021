var employee={eid:1000,name:"amal",designation:"developer",exp:5}
console.log(employee["name"])

console.log(employee["exp"])

//checking if gender is present
console.log("gender" in employee)
console.log(" ")

//adding gender
employee["gender"]="male"
console.log(employee);
console.log(" ");


//iteration
for(let k in employee)
{
    console.log(k+"->"+employee[k]);
}
console.log(" ");


//adding extra experience
employee["exp"]+=1
console.log(employee["exp"]);