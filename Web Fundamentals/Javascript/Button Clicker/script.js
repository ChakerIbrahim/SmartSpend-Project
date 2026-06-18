function removeBtn(element){
    element.remove()
}

function getAlert(){
    alert('Ninja was liked')
}

function loginOut(element){
    if (element.innerText === "login"){
        element.innerText = "logout";
    }
    else(element.innerText = "login")
}
