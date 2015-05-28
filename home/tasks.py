from django.conf import settings
from celery import task
import requests

from home.models import Currency, Rate

@task()
def update_currency_data():
    c_names = get_currency_names()
    c_rates = get_currency_rates()['rates']

    if c_names and c_rates:
        
        print c_names
        for code in c_names:
            currency, c_created = get_currency(code, c_names[code])
            print '%s - %s' % (code, c_names[code])
            
            if c_created:
                currency.save()

            rate, r_created = get_rate(currency, c_rates[currency.code])
            print '%s - %s' % (currency, c_rates[currency.code])

            if r_created:
                    rate.save()
            else:
                rate.rate = c_rates[currency.code]
                rate.save()

#makes http request and gets actual names of currencies
def get_currency_names():
    try:
        r = requests.get('http://openexchangerates.org/api/currencies.json')

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            return None
    except Exception, e:
        return None

#makes http request and gets actual rates of currencies
def get_currency_rates():
    try:
        payload = {'app_id': settings.APP_ID}
        r = requests.get('http://openexchangerates.org/api/latest.json', params=payload)

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            return None
    except Exception, e:
        return None

def get_currency(code, full_name):
    currency = Currency.objects.get_or_create(code=code, full_name=full_name)
    return currency

def get_rate(currency, rate):
    rate = Rate.objects.get_or_create(currency=currency, rate=rate)
    return rate