const inputs = document.querySelectorAll(".input-field");
const toggle_btn = document.querySelectorAll(".toggle");
const main = document.querySelector("main");
const images = document.querySelectorAll(".image");


inputs.forEach((inp) => {
  inp.addEventListener("focus", () => {
    inp.classList.add("active");
  });
  inp.addEventListener("blur", () => {
    if (inp.value != "") return;
    inp.classList.remove("active");
  });
});

toggle_btn.forEach((btn) => {
  btn.addEventListener("click", () => {
    main.classList.toggle("sign-up-mode");
  });
});

function moveSlider() {
  let index = this.dataset.value;

  let currentImage = document.querySelector(`.img-${index}`);
  images.forEach((img) => img.classList.remove("show"));
  currentImage.classList.add("show");

  const textSlider = document.querySelector(".text-group");
  textSlider.style.transform = `translateY(${-(index - 1) * 2.2}rem)`;

}

;
let currentIndex = 0;

function showNextImage() {
  // Ocultar la imagen actual
  images[currentIndex].classList.remove('show');

  // Calcular el índice de la próxima imagen
  currentIndex = (currentIndex + 1) % images.length;

  // Mostrar la siguiente imagen
  images[currentIndex].classList.add('show');
}

// Configura el intervalo para cambiar de imagen automáticamente
setInterval(showNextImage, 3000); // Cambia cada 3 segundos