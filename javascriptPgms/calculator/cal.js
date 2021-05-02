
function dis(val)
{
document.getElementById("edu").value+=val
 }
//function for evaluation
function solve()
{
let x = document.getElementById("edu").value
let y = eval(x)
document.getElementById("edu").value = y
}
//function for clearing the display
function clr()
{
document.getElementById("edu").value = ""
}

function cancelElement()
{
    let data = document.querySelector("#edu").value
    data=data.slice(0,-1)
    document.querySelector("#edu").value=data
}