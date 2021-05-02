class employee
{
    constructor(eid,name,desig,salary)
    {
        this.eid=eid;
        this.name=name;
        this.desig=desig;
        this.salary=salary;
    }
    printemployee()
    {
        console.log(this.eid);
        console.log(this.name);
        console.log(this.desig);
        console.log(this.salary);
    }
}

var obj=new employee(100,"amal","developer",28000)
var obj1=new employee(101,"varun","developer",20000)
var obj2=new employee(102,"arun","qa",23000)
var obj3=new employee(103,"akhil","mrkt",18000)


var employees=[]
employees.push(obj)
employees.push(obj1)
employees.push(obj2)
employees.push(obj3)
//console.log(employees);   {prints full details of all employees}

//print employee names
enames=employees.map(emp=>emp.name)
console.log(enames);

//print emp designation
edesig=employees.map(emp=>emp.desig)
console.log(edesig);
console.log(" ");

//print info about emp whose desig is developer
var devel=employees.filter(emp=>emp.desig=="developer")
console.log(devel);
console.log(" ");

//find highest salary
var sal=employees.reduce((emp1,emp2)=>emp1.salary>emp2.salary?emp1:emp2)
console.log(sal);
console.log(" ");

//sort employees based on their salary
var emp=employees.sort((emp1,emp2)=>emp1.salary-emp2.salary)
console.log(emp);
console.log(" ");




















