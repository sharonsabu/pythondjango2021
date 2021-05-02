//total sum of arr
var array = [1, 2, 3, 4] 
var total = 0;
for (var i = 0; i < array.length; i++) 
{
total += array[i] 
}
console.log(total);

console.log(" ")

//even array
var arr = [1, 2, 3, 4, 5, 6];
for (num of arr)
{	
    if (num % 2 === 0) 
    {       
       console.log(num)         
    }
}

console.log(" ")
    
//odd array
var ar = [1, 2, 3, 4, 5, 6];
for (numb of ar)
{	
    if (numb % 2 !== 0) 
    {       
       console.log(numb)         
    }
}

console.log(" ")

//create two arrays [10,20,30,40] & [20,30,40,50,60,70] print common elemnts


//sorting
var arr=[10,20,111,30,40]
arr.sort((n1,n2)=>n1-n2)    //ascending order  or arr.sort((n1,n2)=>n1>n2?1:-1) 
console.log(arr);           // n1>n2?-1:1 (this means that if n1>n2 then 1 else -1)

var arr=[10,20,111,30,40]
arr.sort((n1,n2)=>n2-n1)    //descending order or arr.sort((n1,n2)=>n1>n2?-1:1) 
console.log(arr);           
console.log(" ");


//min element
var ar=[1,2,3,8,6,4]
ar.sort((n1,n2)=>n1>n2?1:-1)
console.log(ar[0])

//max element
var ar=[1,2,3,8,6,4]
ar.sort((n1,n2)=>n1>n2?-1:1)
console.log(ar[0])







