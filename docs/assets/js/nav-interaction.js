// nav-interaction.js
// UX: Cambia color del nav al hacer hover y scroll, mejora interacción táctil

document.addEventListener("DOMContentLoaded", function () {
  const nav = document.querySelector(".md-header");
  if (!nav) return;

  window.addEventListener("scroll", () => {
    nav.classList.toggle("scrolled", window.scrollY > 50);
  });

  const links = nav.querySelectorAll("a");
  links.forEach(link => {
    link.addEventListener("mouseover", () => {
      nav.classList.add("hover-active");
    });
    link.addEventListener("mouseout", () => {
      nav.classList.remove("hover-active");
    });
  });
});
