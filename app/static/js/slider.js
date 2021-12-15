const slider = document.getElementById("slider");
let containerSliderImage = document.getElementsByClassName("container-slider-image");
let containerSliderImageLast = containerSliderImage[containerSliderImage.length - 1];
slider.insertAdjacentElement('afterbegin', containerSliderImageLast);

const buttonLeft = document.getElementById("button-left");
const buttonRigth = document.getElementById("button-right");

let points = document.getElementsByClassName("slider-point");
let currenPoint = 0;

function nextPoint() {
    points[currenPoint].style.color = "rgba(255, 255, 255, 70%)";
    points[currenPoint].style.transform = "scale(1)";
    if (currenPoint === (points.length - 1)) {
        currenPoint = 0;
    }
    else {
        currenPoint++;
    }
    points[currenPoint].style.color = "white";
    points[currenPoint].style.transform = "scale(1.2)";
}

function previousPoint() {
    points[currenPoint].style.color = "rgba(255, 255, 255, 70%)";
    points[currenPoint].style.transform = "scale(1)";
    if (currenPoint === 0) {
        currenPoint = points.length - 1;
    }
    else {
        currenPoint--;
    }
    points[currenPoint].style.color = "white";
    points[currenPoint].style.transform = "scale(1.2)";
}

function nextLeft() {
    let containerSliderImage = document.getElementsByClassName("container-slider-image");
    let containerSliderImageLast = containerSliderImage[containerSliderImage.length - 1];
    slider.style.marginLeft = "0";
    slider.style.transition = "all 0.5s";
    previousPoint();
    setTimeout(function(){
        slider.style.transition = "none";
        slider.insertAdjacentElement('afterbegin', containerSliderImageLast);
        slider.style.marginLeft = "-100%";
    }, 500);
}

function nextRight() {
    let containerSliderImageFirst = document.getElementsByClassName("container-slider-image")[0];
    slider.style.marginLeft = "-200%";
    slider.style.transition = "all 0.5s";
    nextPoint();
    setTimeout(function(){
        slider.style.transition = "none";
        slider.insertAdjacentElement('beforeend', containerSliderImageFirst);
        slider.style.marginLeft = "-100%";
    }, 500);
}

buttonLeft.addEventListener('click', function(){
    nextLeft();
});

buttonRigth.addEventListener('click', function(){
    nextRight();
    
});

setInterval(function(){
    nextRight();
}, 5000);