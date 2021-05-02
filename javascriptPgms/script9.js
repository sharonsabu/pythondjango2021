//class-->blueprint, design pattern, plan, template
//object-->real world entity
//instance variable-->variable created as a object

class Person{
    setPerson(name,age)
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

var obj=new Person()
obj.setPerson("amal",25)
obj.printPerson()