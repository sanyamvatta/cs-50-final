document.querySelector('.close-icon').style.display= 'none';
function menu(){
   element= document.querySelector(".data-links");
   element.style.transform='translateY(0%)';
   element.style.filter= 'blur(0px)';
   document.querySelector('.menu-icon').style.display= 'none';
   document.querySelector('.close-icon').style.display= 'block';
}
function Mclose(){
    element.style.transform='translateY(-200%)';
    element.style.filter= 'blur(20px)';
    document.querySelector('.close-icon').style.display= 'none';
    document.querySelector('.menu-icon').style.display= 'block';
}
//you can even add animate.css animations