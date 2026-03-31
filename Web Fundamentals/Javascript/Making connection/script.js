
let editLink = document.querySelector("#editProfile");
let userName = document.querySelector("#name");
let requestBadge = document.querySelector(".badge1");
let connectionBadge = document.querySelector(".badge2");

editLink.addEventListener("click", function() {
    let newName = prompt("Enter a new name:");
    if (newName !== "" && newName !== null) {
        userName.innerText = newName;
    }
});


function accept(element) {
    
    let listItem = element.parentElement.parentElement;
    listItem.remove();

    requestBadge.innerText = Number(requestBadge.innerText) - 1;
    connectionBadge.innerText = Number(connectionBadge.innerText) + 1;
    
}


function unaccept(element) {
    let listItem = element.parentElement.parentElement;
    listItem.remove();

    requestBadge.innerText = Number(requestBadge.innerText) - 1;
    
}
