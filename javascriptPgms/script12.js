//single inheritance

class Parent
{
    phone()
    {
        console.log("have nokia");
    }
}
class Child extends Parent
{

}

var ch= new Child()
ch.phone()