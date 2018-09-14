from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import Context, loader

from mainApp.models import UserStats
from mainApp.serializers import UsersListSerializer, UsersStatsUpdateSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from random import choice
from string import ascii_uppercase
import json

class UsersList(APIView):

	# permission_classes = [permissions.IsAdminUser,]
	permission_classes = [permissions.AllowAny,]
	def get(self, request, format=None):
		users_list = UserStats.objects.all()
		serializers = UsersListSerializer(users_list, many=True)

		# serializers = NewUsersListSerializer(users_list, many=True)

		return Response(serializers.data)


class UpdateStats(APIView):
	permission_classes = [permissions.AllowAny,]
	def post(self, request):
		data = self.request.POST
		status = 'Успешно!'

		UserStats.objects.get_or_create(user_id_id = self.request.POST.get('user_id'))

		test_data = UsersStatsUpdateSerializer(data = request.POST)

		if test_data.is_valid():
			UserStats.objects.filter(
				user_id = data.get('user_id')
			).update(
				shoots = interim_user.get('shoots'),
				points = interim_user.get('points'),
				zero = interim_user.get('zero'),
				misshot = interim_user.get('misshot'),
				oneshot = interim_user.get('oneshot'),
				twoshot = interim_user.get('twoshot'),
				threeshot = interim_user.get('threeshot'),
				another = interim_user.get('another'),
				single = interim_user.get('single'),
				double = interim_user.get('double'),
				triple = interim_user.get('triple'),
				outer = interim_user.get('outer'),
				inner = interim_user.get('inner'),
				accuracy = interim_user.get('accuracy'),
				sibling = interim_user.get('sibling'),
				maxScores = interim_user.get('maxScores'),
				minScores = interim_user.get('minScores'),
				games = interim_user.get('games'),
				small = interim_user.get('small'),
				big = interim_user.get('big'),
				middleMiss = interim_user.get('middleMiss'),
			)
		else:
			status = 'Ошибка: данные невалидны...'

		return Response({status})


class UpdateALLStats(APIView):
	permission_classes = [permissions.AllowAny,]
	def post(self, request):
		data = self.request.POST
		status = 'Успешно!'

		# Shit_data --to--> json
		z = list(data.keys())[0]
		data = json.loads(z)

		for obj in data:
			interim_user = data.get(obj)
			test_data = UsersStatsUpdateSerializer(data = interim_user)
			if test_data.is_valid():
				UserStats.objects.filter(
					user_id = interim_user.get('user_id')
				).update(
					shoots = interim_user.get('shoots'),
					points = interim_user.get('points'),
					zero = interim_user.get('zero'),
					misshot = interim_user.get('misshot'),
					oneshot = interim_user.get('oneshot'),
					twoshot = interim_user.get('twoshot'),
					threeshot = interim_user.get('threeshot'),
					another = interim_user.get('another'),
					single = interim_user.get('single'),
					double = interim_user.get('double'),
					triple = interim_user.get('triple'),
					outer = interim_user.get('outer'),
					inner = interim_user.get('inner'),
					accuracy = interim_user.get('accuracy'),
					sibling = interim_user.get('sibling'),
					maxScores = interim_user.get('maxScores'),
					minScores = interim_user.get('minScores'),
					games = interim_user.get('games'),
					small = interim_user.get('small'),
					big = interim_user.get('big'),
					middleMiss = interim_user.get('middleMiss'),
				)

		return Response({status})


class CreatePlayer(APIView):
	permission_classes = [permissions.AllowAny,]
	def post(self, request):
		data = self.request.POST
		status = 'Успешно!'
		username = ''.join(choice(ascii_uppercase) for i in range(12))
		new_user = User.objects.create_user(username=username, password='user12345', first_name=data.get('firstname'))
		UserStats.objects.create(user_id=new_user, avatar=int(data.get('avatar')))

		return Response({'status': status, 'user_id': new_user.id})


class DeletePlayer(APIView):
	permission_classes = [permissions.AllowAny,]
	def post(self, request):
		data = self.request.POST
		
		secret_word = 'finish him'
		if secret_word == data.get('secret_word').lower():

			try:
				new_user = User.objects.get(id=data.get('user_id')).delete()
				return Response({'status': 'FATALITY!!! Игрок сброшен из списков...'})
			except User.DoesNotExist:
				return Response({'status': 'Не найдено игрока с таким ID'})
		else:
			return Response({'status': 'Неверное проверочное слово...'})
