//method overloading

class calculation
{
    add()
    {
        console.log("inside single arg method");
    }
    add(num1,num2)
    {
        console.log("inside two arg method");
    }
}

var obj=new calculation()
obj.add()     
obj.add(10,20)
//here always the newest method will be invoked if u call any method either 1st or 2nd