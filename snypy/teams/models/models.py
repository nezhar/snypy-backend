from django.db import models

from django_userforeignkey.models.fields import UserForeignKey

from core.models import BaseModel, DateModelMixin
from .managers import TeamManager, UserTeamManger


class Team(BaseModel, DateModelMixin):

    objects = TeamManager()

    users = models.ManyToManyField(
        'auth.User',
        related_name='teams',
        verbose_name='Users',
        through='UserTeam',
        through_fields=('team', 'user', ),
    )

    name = models.CharField(
        verbose_name='Name',
        max_length=255,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class UserTeam(BaseModel, DateModelMixin):

    objects = UserTeamManger()

    user = UserForeignKey(
        verbose_name="User",
        related_name="user_teams",
        editable=False,
        on_delete=models.CASCADE,
    )

    team = models.ForeignKey(
        'Team',
        related_name='user_teams',
        verbose_name='Team',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
