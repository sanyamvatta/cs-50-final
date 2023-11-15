document.addEventListener("DOMContentLoaded", function() {
  const ctaButton = document.getElementById("ctaButton");

  ctaButton.addEventListener("mousedown", function() {
      ctaButton.style.transform = "scale(0.95)"; /* Slightly decrease size on click */
  });

  ctaButton.addEventListener("mouseup", function() {
      ctaButton.style.transform = "scale(1)"; /* Reset size after click */
  });
});

