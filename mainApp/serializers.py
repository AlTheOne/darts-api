from django.contrib.auth.models import User
from rest_framework import serializers
from mainApp.models import UserStats


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name')


class UsersListSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserStats
		fields = (
			'user_id',
			'avatar',
			'shoots',
			'points',
			'zero',
			'misshot',
			'oneshot',
			'twoshot',
			'threeshot',
			'another',
			'single',
			'double',
			'triple',
			'outer',
			'inner',
			'accuracy',
			'sibling',
			'maxScores',
			'minScores',
			'games',
			'small',
			'big',
			'middleMiss'
		)

	user_id = UsersSerializer()


class UsersStatsUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserStats
		fields = (
			'shoots',
			'points',
			'zero',
			'misshot',
			'oneshot',
			'twoshot',
			'threeshot',
			'another',
			'single',
			'double',
			'triple',
			'outer',
			'inner',
			'accuracy',
			'sibling',
			'maxScores',
			'minScores',
			'games',
			'small',
			'big',
			'middleMiss'
		)