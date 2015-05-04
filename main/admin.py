from django.contrib import admin
from .models import Information

class InformationAdmin(admin.ModelAdmin):
	list_display = ('user', 'phone_number', 'can_book')
admin.site.register(Information,InformationAdmin)
