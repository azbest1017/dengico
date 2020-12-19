
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
      $("#rubles").toggleClass("add_gold_border");  //Toggle the active class to the area is hovered
  });


  $("#myRangeDay").hover(function(){
        $("#weeks").toggleClass("add_gold_border");
    });
// Add gold border to Input while hover on Range End --->
