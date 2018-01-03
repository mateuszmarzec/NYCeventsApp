$( document ).ready(function() {
    if ( $('#map').length){
        $("#reg-form").css("margin-top","20px");
    }
    else if ($('#container').length){
        $("#reg-form").css("margin-top","20px");
    }
    else{
        $("#reg-form").css("margin-top","20vh");
    }
});


