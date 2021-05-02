function displayTodo(todo)
{
    let html_data=""
    html_data=`<tr><td>${todo.user}</td><td>${todo.task}</td><td>${todo.status}</td></tr>`
    document.querySelector(".dataarea").innerHTML=html_data
}
function createTodo()
{
    let user=document.querySelector("#uname").value
    let task=document.querySelector("#tname").value
    let status=document.querySelector("#status").value
    let todo={
        user:user,
        task:task,
        status:status
    }
    displayTodo(todo)
}
    

