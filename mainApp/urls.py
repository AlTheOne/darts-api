from django.urls import path
from mainApp.views import UsersList, UpdateStats, UpdateALLStats, CreatePlayer, DeletePlayer
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	path('users_list/', UsersList.as_view(), name='userslist'),
	path('update_stats/', UpdateStats.as_view(), name='updatestats'),
	path('update_all_stats/', UpdateALLStats.as_view(), name='updatestats'),
	path('auth/', obtain_jwt_token, name='AuthUser'),
	path('registry_player/', CreatePlayer.as_view(), name='registryPlayer'),
	path('delete_player/', DeletePlayer.as_view(), name='deletePlayer'),
]