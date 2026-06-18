function showCityAlert(city) {
  alert("Loading weather report for " + city);
}

function acceptCookies() {
  document.querySelector(".cookie-box").remove();
}

function convertTemps(elem) {
  var temps = document.querySelectorAll(".temp")
  for(let i = 0;i < temps.length;i++){
    if(elem === "c"){
       c = parseInt(temps[i].innerText);
      c = c -32 * 5/9;
      temps[i].innerText=Math.floor(c) + "°c";
    }
    else{
      f = parseInt(temps[i].innerText)
      f = f * 9/5 + 32
      temps[i].innerText=Math.floor(f) + "°f"
    }
  }
}


