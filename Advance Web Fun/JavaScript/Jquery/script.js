$(document).ready(function () {

  // 🌙 Dark / Light Mode
  $("#mode").click(function () {
    $("body").toggleClass("dark");

    if ($("body").hasClass("dark")) {
      $(this).text("Light Mode");
    } else {
      $(this).text("Dark Mode");
    }
  });

  // ➕ Add item
  $("#add").click(function () {
    let text = $("#input").val();

    if (text === "") return;

    let item = `
      <div class="item">
        ${text}
        <button class="delete">X</button>
      </div>
    `;

    $("#list").append(item);
    $("#input").val("");
  });

  // ❌ Delete item
  $(document).on("click", ".delete", function () {
    $(this).parent().remove();
  });

});