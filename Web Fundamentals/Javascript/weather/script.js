function showCityAlert(city) {
  alert("Loading weather report for " + city);
}

function acceptCookies() {
  document.querySelector(".cookie-box").remove();
}

function convertTemps() {
  let unit = document.querySelector("#unit").value;
  let temps = document.querySelectorAll(".temp");

  for (let i = 0; i < temps.length; i++) {
   let c = temps[i].getAttribute("data-c");

    if (unit === "c") {
      temps[i].innerText = c + "°C";
    } else {
      temps[i].innerText = Math.round(c * 9/5 + 32) + "°F";
    }
  }
}