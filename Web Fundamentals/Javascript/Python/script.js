const normalText = document.getElementById("normalText");
const largeText = document.getElementById("largeText");

normalText.addEventListener("click", function (e) {
  e.preventDefault();
  document.body.classList.remove("large-text");
});

largeText.addEventListener("click", function (e) {
  e.preventDefault();
  document.body.classList.add("large-text");
});