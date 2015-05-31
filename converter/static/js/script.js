$(document).ready(function (){

	getCurrencyNames();

	$('#data-submit').click(function (){
		getCalculationResult();
	});
    
    $(document).keypress(function (event){
    	if (event.which == 13){
    		$('#data-submit').click();
    	}
    })

    $('.currency').click(function (){
    	$(this).val('');
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

	var cur_from = $('#cur-from').val();
	if (cur_from == ''){
		var cur_from = 'CUR1';
	}

	var cur_to = $('#cur-to').val();
	if (cur_to == ''){
		var cur_to = 'CUR2';
	}

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
	$('#result-block').html(data);
};
