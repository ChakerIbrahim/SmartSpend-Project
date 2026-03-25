
let editLink = document.querySelector("#editProfile");
let userName = document.querySelector("#name");
let requestBadge = document.querySelector(".col-1 .card:first-child .badge");
let connectionBadge = document.querySelector(".col-1 .card:nth-child(2) .badge");
//change Name
editLink.addEventListener("click", function (e) {
    let newName = prompt("Enter a new name:");
    if (newName !== "" ) {
        userName.innerText = newName;
    }
});

// accept request
function accept(element) {
    console.log("hello")
    let listItem = element.parentElement.parentElement;
    listItem.remove();

    requestBadge.innerText = Number(requestBadge.innerText) - 1;
    connectionBadge.innerText = Number(connectionBadge.innerText) + 1;
    
}

// remove request
function unaccept(element) {
    let listItem = element.parentElement.parentElement;
    listItem.remove();

    requestBadge.innerText = Number(requestBadge.innerText) - 1;
    
}
