from django.core.cache import cache
from home.models import Rate


def calculate_amount(amount, from_code, to_code):
    CACHE_TIME = 1800

    error = []
    result = 0
    to_currency = ''
    
    try:
        amount = float(amount)
        try:

            from_rate = cache.get(from_code.upper())
            to_rate = cache.get(to_code.upper())

            if not from_rate:
                from_rate = Rate.objects.get(currency__code=from_code)
                cache.set(from_code.upper(), from_rate, CACHE_TIME)

            if not to_rate:
                to_rate = Rate.objects.get(currency__code=to_code)
                cache.set(to_code.upper(), to_rate, CACHE_TIME)
                
            to_currency = to_rate.currency.full_name

        except Exception, e:
            error = 'Please, enter correct currencies'

        print amount, to_rate, from_rate 

        if from_code.lower() == 'usd':
            result = amount * to_rate.rate
        elif to_code.lower() == 'usd':
            result = amount / from_rate.rate
        else:
            cross_rate = to_rate.rate / from_rate.rate
            result = amount * cross_rate

    except ValueError:
        error = 'Amount isn\'t a number'
    finally:
        return (round(result, 2), to_currency, error)