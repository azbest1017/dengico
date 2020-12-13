
function numberWithCommas(x) {
    return x.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, " ");
}


var slider = document.getElementById("myRange");
var output = document.getElementById("rubles");
output.innerHTML = numberWithCommas(slider.value);



slider.oninput = function() {
  output.innerHTML = numberWithCommas(this.value);
}

var days = document.getElementById("myRangeDay");
var output_days = document.getElementById("weeks");
output_days.innerHTML = numberWithCommas(days.value);

days.oninput = function() {
  output_days.innerHTML = numberWithCommas(this.value);
}


// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("mfo_main");

// Get the offset position of the navbar
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}
