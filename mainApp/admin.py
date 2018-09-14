from django.contrib import admin
from mainApp.models import UserStats

class UserStatsAdmin(admin.ModelAdmin):
	class Meta:
		model = UserStats

	list_display = ('id', 'user_id')

admin.site.register(UserStats, UserStatsAdmin)