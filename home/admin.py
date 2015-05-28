from home.models import Currency, Rate
from django.contrib import admin
from kombu.transport.django import models as kombu_models


admin.site.register(kombu_models.Message)
admin.site.register(Currency)
admin.site.register(Rate)