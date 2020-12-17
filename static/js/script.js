
function numberWithCommas(x) {
    return x.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, " ");
}









function updateWeeksInput(val) {
          document.getElementById('weeks').value=val;
        }

$(document).on('input', '#myRange', function() {
            $('#rubles').val( $(this).val() );
      });

$(document).on('input', '#myRangeDay', function() {
            $('#weeks').val( $(this).val() );
      });
