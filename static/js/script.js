var names = {};
$(document).ready(function (){

	getCurrencyNames();
    
});

var getCurrencyNames = function (){
	$.ajax({
		type: 'GET',
		url: '/getcurrencynames',
		success: fillAutocomplete,
		dataType: 'json'
	});
};

var fillAutocomplete = function (data, textStatus, jqXHR){
	$('#cur-from, #cur-to').autocomplete({
       source: data
    });
    $('#cur-from').val('USD');
    $('#cur-to').val('EUR');
};
