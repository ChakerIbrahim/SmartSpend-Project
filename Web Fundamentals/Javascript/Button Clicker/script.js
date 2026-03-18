function removeBtn(element){
    element.remove()
}

function loginOut(element){
    if (element.innerText === "login"){
        element.innerText = "logout";
    }
    else(element.innerText = "login")
}
