let userName = document.querySelector("#name");
let requestBadge = document.querySelector(".badge1");
let connectionBadge = document.querySelector(".badge2");


function editName(){
    let newName = prompt("Enter a new name:");
        userName.innerText = newName;
};

function accept(element) {
   element.closest("li").remove() ;
    
    requestBadge.innerText--;
    connectionBadge.innerText++;
}

function unaccept(element) {
    element.closest("li").remove()
    requestBadge.innerText--;
}




