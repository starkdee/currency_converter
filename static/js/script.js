$(document).ready(function (){

	getCurrencyNames();

	$('#data-submit').click(function (){
		getCalculationResult();
	});
    
});

var getCurrencyNames = function (){
	$.ajax({
		type: 'GET',
		url: '/getcurrencynames',
		success: fillAutocomplete,
		dataType: 'json'
	});
};

var getCalculationResult = function (){
	var amount = $('#amount').val();

	if (!isNaN(amount) && amount.indexOf('.') == -1){
		amount += '.00';
	}

	var cur_from = $('#cur-from').val();
	var cur_to = $('#cur-to').val();

	var requestUrl = '/' + amount + '/' + cur_from + '/to/' + cur_to + '/in/' + 'html';
	console.log(requestUrl);

	$.ajax({
		type: 'GET',
		url: requestUrl,
		success: showResult,
		dataType: 'html'
	});
};


var fillAutocomplete = function (data, textStatus, jqXHR){
	$('#cur-from, #cur-to').autocomplete({
       source: data
    });
    $('#cur-from').val('USD');
    $('#cur-to').val('EUR');
};

var showResult = function (data, textStatus, jqXHR){
	console.log(data);
};
