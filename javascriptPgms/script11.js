class Person
{
    constructor(name,age)
    {
        this.name=name;
        this.age=age;
    }
    printPerson()
    {
        console.log(this.name);
        console.log(this.age);
    }
}

var obj=new Person("ajay",25)
obj.printPerson()