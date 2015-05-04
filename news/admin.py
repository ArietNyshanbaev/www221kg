from django.contrib import admin
from .models import Team, League, News
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name','slogan', 'league')
admin.site.register(Team,TeamAdmin)
class LeagueAdmin(admin.ModelAdmin):
	list_display = ('name','slogan')
admin.site.register(League, LeagueAdmin)

class NewsAdmin(admin.ModelAdmin):
	list_display = ('team', 'title', 'user', 'date')
	fieldsets = [
        (None, { 'fields': [('team','title','image','description','body')] } ),
    ]

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'user', None) is None:
			obj.user = request.user
		obj.save()

admin.site.register(News,NewsAdmin)
