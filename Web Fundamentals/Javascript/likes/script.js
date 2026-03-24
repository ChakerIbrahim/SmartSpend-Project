function addLike(button) {
  var likeText = button.parentElement.querySelector(".like");
  var currentLikes = parseInt(likeText.innerText);
  currentLikes++;
  likeText.innerText = currentLikes + " like(s)";
}