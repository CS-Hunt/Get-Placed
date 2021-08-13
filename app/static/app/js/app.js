
/*  Preloader */
let preloader = document.getElementById('loading');

const onLoad = () => {
    preloader.style.display = 'none';
}

// search-box open close js code
let navbar = document.querySelector(".navbar");
let searchBox = document.querySelector(".search-box .bx-search");
// let searchBoxCancel = document.querySelector(".search-box .bx-x");

searchBox.addEventListener("click", () => {
    navbar.classList.toggle("showInput");
    if (navbar.classList.contains("showInput")) {
        searchBox.classList.replace("bx-search", "bx-x");
    } else {
        searchBox.classList.replace("bx-x", "bx-search");
    }
});

// sidebar open close js code
let navLinks = document.querySelector(".nav-links");
let menuOpenBtn = document.querySelector(".navbar .bx-menu");
let menuCloseBtn = document.querySelector(".nav-links .bx-x");
menuOpenBtn.onclick = function () {
    navLinks.style.left = "0";
}
menuCloseBtn.onclick = function () {
    navLinks.style.left = "-100%";
}
// JavaScript Document
$(document).ready(function () {
    $('#autoWidth').lightSlider({
        autoWidth: true,
        // loop: true,
        onSliderLoad: function () {
            $('#autoWidth').removeClass('cS-hidden');
        }
    });
});
$(document).ready(function () {
    $('#autoWidth1').lightSlider({
        autoWidth: true,
        // loop: true,
        onSliderLoad: function () {
            $('#autoWidth1').removeClass('cS-hidden');
        }
    });
});
$(document).ready(function () {
    $('#autoWidth2').lightSlider({
        autoWidth: true,
        // loop: true,
        onSliderLoad: function () {
            $('#autoWidth2').removeClass('cS-hidden');
        }
    });
});
console.log("hiiiiii")

// sidebar submenu open close js code
let htmlcssArrow = document.querySelector(".htmlcss-arrow");
htmlcssArrow.onclick = function () {
    navLinks.classList.toggle("show1");
}
let jsArrow = document.querySelector(".js-arrow");
jsArrow.onclick = function () {
    navLinks.classList.toggle("show3");
}
let moreArrow = document.querySelector(".more-arrow");
moreArrow.onclick = function () {
    navLinks.classList.toggle("show2");
}

document.querySelector('.js-accent-color').addEventListener('change', (e) => {
	document.documentElement.style.setProperty('--accent-color', e.target.value)
})