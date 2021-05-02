function displayBook(book)
{
    let html_data=""
    html_data=`<tr><td>${book.bname}</td><td>${book.author}</td><td>${book.price}</td><td>${book.category}</td></tr>`
    document.querySelector(".dataarea").innerHTML=html_data
}
function createBook()
{
    let bname=document.querySelector("#bname").value
    let author=document.querySelector("#author").value
    let price=document.querySelector("#price").value
    let category=document.querySelector("#category").value

    let book={
        bname:bname,
        author:author,
        price:price
        category:category
    }
    displayBook(book)
}
    

