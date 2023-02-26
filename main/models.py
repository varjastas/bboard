from django.db import models
from django.contrib.auth.models import AbstractUser

class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях?')
    class Meta(AbstractUser.Meta):
        pass

class Secret(models.Model):
    text = models.CharField(max_length=4900)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text
    