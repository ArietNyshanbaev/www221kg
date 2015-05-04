from django.contrib import admin
from .models import Team, League, News
# Register your models here.
admin.site.register(Team)
admin.site.register(League)

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
