from django.contrib import admin

# Register your models here.
from .models import Event, Banner, Servant

admin.site.register(Event)
admin.site.register(Banner)
admin.site.register(Servant)