$(document).ready(function() {
    $(".modal-example").click(function(e){
        e.preventDefault();
        $.ajax({
            url: $(this).attr("data-url"),
            success: function(data) {
                $("#modal-div").html(data);
                $("#modal_template").modal('show');
            }
        });
    }); 
});

$(document).ready(function() {
    $(function () { $(".rating").rateYo({ spacing   : "5px",  readOnly: true,
            multiColor: { 
                    "startColor": "#FF0000", //RED
                    "endColor"  : "#00FF00"  //GREEN
                    },
        });
    });
});

$(document).ready(function() {
    $("#myInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#myTable div").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    
});
