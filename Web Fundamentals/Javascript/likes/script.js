function addLike(element) {
  var likeText = element.parentElement.querySelector(".like");
  var currentLikes = parseInt(likeText.innerText);
  currentLikes++;
  likeText.innerText = currentLikes + " like(s)";
}