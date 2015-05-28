from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'home.views.index', name='index'),
]