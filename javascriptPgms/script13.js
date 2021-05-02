//multiple inhertance not supported

//multi-level inheritance

class Parent
{
    object()
    {
        console.log("c1");
    }
}

class Child extends Parent
{
    object1()
    {
        console.log("c2");
    }
}

class Subchild extends Child
{
    object2()
    {
        console.log("c3");
    }
}

var sub=new Subchild()
sub.object()
sub.object1()
sub.object2()