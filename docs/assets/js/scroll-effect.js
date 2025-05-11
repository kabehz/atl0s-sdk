// scroll-effect.js
// Efecto parallax simple y optimización UX para MKDocs

document.addEventListener("DOMContentLoaded", function () {
  const header = document.querySelector(".md-header");
  const main = document.querySelector(".md-main");

  window.addEventListener("scroll", function () {
    const scrolled = window.scrollY;

    if (header) {
      header.style.backdropFilter = "blur(" + Math.min(scrolled / 20, 8) + "px)";
      header.style.boxShadow = scrolled > 10 ? "0 2px 8px rgba(0,0,0,0.2)" : "none";
    }

    if (main) {
      main.style.transform = "translateY(" + scrolled * 0.01 + "px)";
    }
  });
});
