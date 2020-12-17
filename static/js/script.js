
function numberWithCommas(x) {
    return x.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, " ");
}


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
