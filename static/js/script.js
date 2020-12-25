
function numberWithCommas(x) {
    return x.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, " ");
}

// Value from Range to Input Start --->
$(document).on('input', '#myRange', function() {
            $('#rubles').val( $(this).val() );
      });
$(document).on('input', '#myRangeDay', function() {
            $('#weeks').val( $(this).val() );
      });
$(document).on('input', '#rubles', function() {
            $('#myRange').val( $(this).val() );
      });
$(document).on('input', '#weeks', function() {
            $('#myRangeDay').val( $(this).val() );
      });
// Value from Range to Input End --->

// Add gold border to Input while hover on Range Start --->
$("#myRange").hover(function(){
      $("#rubles").toggleClass("add_gold_border");
  });

  $("#myRangeDay").hover(function(){
        $("#weeks").toggleClass("add_gold_border");
    });
// Add gold border to Input while hover on Range End --->

// SAVE VALUE AFTER SUBMINT FORM START --->
document.getElementById('button_go').addEventListener('click', function() {
  var data = [];
  data.push(document.getElementById('myRange').value);
  data.push(document.getElementById('rubles').value);
  data.push(document.getElementById('myRangeDay').value);
  data.push(document.getElementById('weeks').value);
  localStorage.setItem('k', JSON.stringify(data));
});
window.addEventListener('load', function() {
  var data = JSON.parse(localStorage.getItem('k'));
  document.getElementById('myRange').value = data[0];
  document.getElementById('rubles').value = data[1];
  document.getElementById('myRangeDay').value = data[2];
  document.getElementById('weeks').value = data[3];
});
// SAVE VALUE AFTER SUBMINT FORM END--->

// SAVE VALUE OF CHECKBOXes AFTER SUBMINT FORM START--->
document.addEventListener("DOMContentLoaded", function(){

   var checkbox = document.querySelectorAll("input[type='checkbox']");

   for(var item of checkbox){
      item.addEventListener("click", function(){
         localStorage.s_item ? // verifico se existe localStorage
            localStorage.s_item = localStorage.s_item.indexOf(this.id+",") == -1 // verifico de localStorage contém o id
            ? localStorage.s_item+this.id+"," // não existe. Adiciono a id no loaclStorage
            : localStorage.s_item.replace(this.id+",","") : // já existe, apago do localStorage
         localStorage.s_item = this.id+",";  // não existe. Crio com o id do checkbox
      });
   }

   if(localStorage.s_item){ // verifico se existe localStorage
      for(var item of checkbox){ // existe, percorro as checkbox
         item.checked = localStorage.s_item.indexOf(item.id+",") != -1 ? true : false; // marco true nas ids que existem no localStorage
      }
   }
});

// SAVE VALUE OF CHECKBOX AFTER SUBMINT FORM END--->

// MultiCheckBoxes list select START--->

var show = true;

function showCheckboxes() {
    var checkboxes = document.getElementById("checkBoxes");

    if (show) {
        checkboxes.style.display = "block";
        show = false;
    } else {
        checkboxes.style.display = "none";
        show = true;
    }

}


// MultiCheckBoxes list select END--->
