from django.contrib import admin
from .models import BookRequest,Day,Field
# Register your models here.

admin.site.register(Field)

class BookRequestAdmin(admin.ModelAdmin):
	list_display = ('user', 'field', 'time', 'date_time')

admin.site.register(BookRequest, BookRequestAdmin)

class DayAdmin(admin.ModelAdmin):
	list_display = ('field', 'date', 'day_of_week')

admin.site.register(Day, DayAdmin)