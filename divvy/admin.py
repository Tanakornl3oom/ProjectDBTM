from django.contrib import admin

from divvy.models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Customer._meta.fields]



admin.site.register(Customer,CustomerAdmin)
