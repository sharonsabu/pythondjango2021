//adding two numbers
function add(num1,num2)
{
    return  num1+num2
}
let result=add(50,60)
console.log(result);

console.log(" ")


//factorial
 
function factorial(no)

{
    let res=1;
    for(let i=1;i<=no;i++)
        {
            res=res*i;
        }
    return res
}

let res=factorial(5)
console.log(res)

console.log(" ")

//arrays

var arr=[10,20,30,40]

console.log(arr[1]);
arr[1]=200
console.log(arr);
arr.push(50)
console.log(arr);
arr.pop()
console.log(arr);

console.log(" ")


for(let i of arr)
{
    console.log(i);
}

console.log(" ")

for(let i=0;i<arr.length;i++)
{
    console.log(arr[i]);
}


