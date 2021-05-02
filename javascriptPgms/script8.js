var cube=no1=>no1**3
console.log(cube(3))


var arr=[10,11,12,13,14]
var sum=arr.reduce((n1,n2)=>n1+n2)
console.log(sum);


var mini=arr.reduce((n1,n2)=>n1<n2?n1:n2)
console.log(mini);

var max=arr.reduce((n1,n2)=>n2<n1?n1:n2)
console.log(max)