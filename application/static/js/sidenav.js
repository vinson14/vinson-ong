function toggleSidebar() {
  var sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("sidebar-active");
  var icon = document.getElementById("sidebar-expand-icon");
  icon.classList.toggle("fa-bars");
  icon.classList.toggle("fa-times");
}

window.addEventListener("load", function() {
    body = document.querySelector('body');
    body.classList.add("fadeIn");
})
