from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'home.views.index', name='index'),
    url(r'^getcurrencynames/$', 'home.views.get_currency_names', name='get_names'),
    url(r'^(?P<amount>[0-9a-zA-Z_.]+)/(?P<from_code>\w+)/to/(?P<to_code>\w+)/in/(?P<content_type>\w+)$', 'home.views.result', name='result')
]