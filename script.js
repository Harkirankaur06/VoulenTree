let currentIndex = 0;
function moveSlide(direction) {
    const slider = document.querySelector(".slider-wrapper");
    const slides = document.querySelectorAll(".slider-content");
    const totalSlides = slides.length;
    const visibleSlides = 4; 
    const slideWidth = slides[0].offsetWidth + 100; 
    
    currentIndex += direction;
    if (currentIndex < 0) {
        currentIndex = totalSlides - visibleSlides;
    } else if (currentIndex > totalSlides - visibleSlides) {
        currentIndex = 0;
    }
    slider.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
}