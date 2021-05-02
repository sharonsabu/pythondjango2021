//method overriding

class parent
{
    phone()
    {
        console.log("inside phone method");
    }
}
class child extends parent
{
    phone()
    {
        console.log("inside child phone method");
    }
}

var ch= new child()
ch.phone()