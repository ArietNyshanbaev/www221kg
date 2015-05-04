from django.contrib import admin
from .models import Match, Bet, Tour, CurrentTour

admin.site.register(CurrentTour)

class MatchAdmin(admin.ModelAdmin):
	list_display = ('tour', 'first_team', 'second_team')

admin.site.register(Match, MatchAdmin)

class TourAdmin(admin.ModelAdmin):
	list_display = ('tour_number', 'tour_end', 'tour_prize')

admin.site.register(Tour,TourAdmin)

class BetAdmin(admin.ModelAdmin):
	list_display = ('user', 'tour_number', 'correct_num')

admin.site.register(Bet, BetAdmin)
