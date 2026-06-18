function playSong(title, artist, src,elem) {
  const player = document.getElementById("audio-player");

  document.getElementById("track-title").innerText = title;
  document.getElementById("track-artist").innerText = artist;

  player.src = src; //change the song//
  player.load(); //load the new song//
  player.play(); //play the new song//

      document.querySelectorAll(".track").forEach(track => {
      track.classList.remove("active");
    });
    elem.classList.add('active');
}