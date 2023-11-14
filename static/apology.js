document.addEventListener("DOMContentLoaded",function(){
  
  var body=document.body;
   setInterval(createStar,100);
   function createStar(){
     var right=Math.random()*500;
     var top=Math.random()*screen.height;
     var star=document.createElement("div");
  star.classList.add("star")
   body.appendChild(star);
   setInterval(runStar,10);
     star.style.top=top+"px";
   function runStar(){
     if(right>=screen.width){
       star.remove();
     }
     right+=3;
     star.style.right=right+"px";
   }
   } 
 })

 document.addEventListener("DOMContentLoaded", function() {
  // Capture the current URL before redirection
  var previousUrl = document.referrer;

  // Store the previous URL in sessionStorage
  sessionStorage.setItem("previousUrl", previousUrl);

  // Add a click event listener to the "Go Back" button
  var backButton = document.getElementById("backButton");
  backButton.addEventListener("click", function() {
      // Retrieve the previous URL from sessionStorage and navigate to it
      var storedUrl = sessionStorage.getItem("previousUrl");
      if (storedUrl) {
          window.location.href = storedUrl;
      } else {
          // Handle the case when there is no stored URL
          alert("No previous URL available");
      }
  });
});