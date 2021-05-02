// to change Click to Clicked on double tap 
var clck=document.getElementById("clkid")
function clickChange()
{
    clck.textContent="Clicked"
}
clck.addEventListener("click",clickChange)



//to change DoubleClick to Double Clicked and content color to red on double tap
var dbc=document.querySelector("#dbclkid")
dbc.addEventListener("dblclick",()=>{
    dbc.textContent="Double Clicked"
    dbc.style.color="red"
})



 var m=document.querySelector("#mo")
 m.addEventListener("dblclick",()=>{
     m.textContent="Mouse Overed"
     m.style.color="blue"
 })

// var m=document.getElementById("mo")
// function mouseChange()
// {
//     m.textContent="Mouse Overed"
// }
// m.addEventListener("click",mouseChange)