
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

// SAVE VALUE OF CHECKBOX AFTER SUBMINT FORM START--->
$(function(){
    var test = localStorage.input === 'true'? true: false;
    $('input').prop('checked', test);
});

$('input').on('change', function() {
    localStorage.input = $(this).is(':checked');
    console.log($(this).is(':checked'));
});
// SAVE VALUE OF CHECKBOX AFTER SUBMINT FORM END--->
