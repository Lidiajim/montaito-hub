document.addEventListener("DOMContentLoaded", function () {
    const ratingContainers = document.querySelectorAll(".rating-container");
    ratingContainers.forEach(container => {
        const rating = parseFloat(container.getAttribute("data-rating"));
        const fullStars = Math.floor(rating);
        const halfStar = rating % 1 >= 0.5 ? 1 : 0;
        const emptyStars = 5 - fullStars - halfStar;

        const starFontSize = "31px"; 

        for (let i = 0; i < fullStars; i++) {
            const star = document.createElement("span");
            star.classList.add("star", "filled");
            star.innerHTML = "&#9733;"; 
            star.style.color = "gold"; 
            star.style.fontSize = starFontSize; 
            container.appendChild(star);
        }

        if (halfStar) {
            const star = document.createElement("span");
            star.classList.add("star", "half");
            star.innerHTML = "&#9733;"; 
            star.style.color = "gold"; 
            star.style.clipPath = "inset(0 50% 0 0)";
            star.style.fontSize = starFontSize; 
            container.appendChild(star);
        }

        for (let i = 0; i < emptyStars; i++) {
            const star = document.createElement("span");
            star.classList.add("star", "empty");
            star.innerHTML = "&#9734;"; 
            star.style.color = "lightgray"; 
            star.style.fontSize = starFontSize; 
            container.appendChild(star);
        }
    });
});
