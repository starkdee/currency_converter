from home.models import Rate


def calculate_amount(amount, from_code, to_code):
    print amount, from_code, to_code
    error = []
    result = 0
    try:
        amount = float(amount)
        
        try:
            from_rate = Rate.objects.get(currency__code=from_code)
            to_rate = Rate.objects.get(currency__code=to_code)
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
        return (round(result, 2), error)