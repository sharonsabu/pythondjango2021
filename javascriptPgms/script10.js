class Student
{
    setStudent(sno,name,course)
    {
        this.sno=sno;
        this.name=name;
        this.course=course;
    }
    
    printStudent()
    {
        console.log(this.sno);
        console.log(this.name);
        console.log(this.course);
    }
}

var obj=new Student()
obj.setStudent(100,"amal","bcom")
obj.printStudent()