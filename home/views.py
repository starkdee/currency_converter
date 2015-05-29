from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

import json
from home.calculate import calculate_amount

from home.models import Currency, Rate
from home.forms import CurrencyForm



def index(request):
    c_form = CurrencyForm()

    return render(request, 'index.html', {'c_form': c_form})

def result(request, amount, from_code, to_code, content_type):
    print amount, from_code, to_code, content_type

    result, error = calculate_amount(amount, from_code, to_code)

    if content_type.lower() == 'html':
        return render(request, 'result.html', {'result': result, 'error': error})

    elif content_type.lower() == 'json':
        raw_data = {'success': True}
        
        if error:
            raw_data['success'] = False
            raw_data['error'] = error
        else:
            raw_data['result'] = result

        json_data = json.dumps(raw_data)

        return HttpResponse(json_data, content_type='application/json')

    elif content_type.lower() == 'text':
        if error:
            return HttpResponse(error)
        else:
            return HttpResponse(result)

def get_currency_names(request):
    currencies = Currency.objects.all()

    raw_data = []
    for cur in currencies:
        raw_data.append({'label': cur.full_name, 'value': cur.code})

    json_data = json.dumps(raw_data)

    return HttpResponse(json_data, content_type='application/json')