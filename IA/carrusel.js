const carousel = document.getElementById('carouselLista');
const anterior = document.getElementById('carouselAnterior');
const siguiente = document.getElementById('carouselSiguiente');
const anchoItem = carousel.firstElementChild.offsetWidth;
let posicion = 0;

siguiente.addEventListener('click', () => {
  posicion -= anchoItem;
  carousel.style.transform = `translateX(${posicion}px)`;
});

anterior.addEventListener('click', () => {
  posicion += anchoItem;
  carousel.style.transform = `translateX(${posicion}px)`;
});
