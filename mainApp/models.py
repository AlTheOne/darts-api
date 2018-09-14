from django.db import models
from django.contrib.auth.models import User

class UserStats(models.Model):
	class Meta:
		verbose_name = 'Статистика'
		verbose_name_plural = 'Статистики'

	user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='globalStats', verbose_name='Пользователь')
	avatar = models.IntegerField(blank=True, verbose_name='Аватар')
	shoots = models.IntegerField(default=0, verbose_name='Броски')
	points = models.IntegerField(default=0, verbose_name='Очки')
	zero = models.IntegerField(default=0, verbose_name='Зеро')
	misshot = models.IntegerField(default=0, verbose_name='Промах')
	oneshot = models.IntegerField(default=0, verbose_name='Первый бросок')
	twoshot = models.IntegerField(default=0, verbose_name='Второй бросок')
	threeshot = models.IntegerField(default=0, verbose_name='Третий бросок')
	another = models.IntegerField(default=0, verbose_name='Другой')
	single = models.IntegerField(default=0, verbose_name='Один')
	double = models.IntegerField(default=0, verbose_name='Двойной')
	triple = models.IntegerField(default=0, verbose_name='Тройной')
	outer = models.IntegerField(default=0, verbose_name='Внешний')
	inner = models.IntegerField(default=0, verbose_name='Внутренний')
	accuracy = models.IntegerField(default=0, verbose_name='Точность')
	sibling = models.IntegerField(default=0, verbose_name='Сиблинг')
	maxScores = models.IntegerField(default=0, verbose_name='Максимальный балл')
	minScores = models.IntegerField(default=9999, verbose_name='Минимальный балл')
	games = models.IntegerField(default=0, verbose_name='Игр')
	small = models.IntegerField(default=0, verbose_name='Маленький')
	big = models.IntegerField(default=0, verbose_name='Большой')
	middleMiss = models.IntegerField(default=0, verbose_name='Средний промах')

	def __str__(self):
		return "Статистика %s" % self.user_id.username