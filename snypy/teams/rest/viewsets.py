from django.db.models import Count, Case, When, F, CharField

from core.rest.viewsets import BaseModelViewSet

from ..models import Team, UserTeam
from .filters import UserTeamFilter
from .serializers import TeamSerializer, UserTeamSerializer


class TeamViewSet(BaseModelViewSet):
    """
    Test Docs 1
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    title = "Test 1"
    description = "Desc 1"


    def list(self, request, *args, **kwargs):
        """
        Test Docs 2
        """
        return super().list(request, *args, **kwargs)

    def options(self, request, *args, **kwargs):
        """
        Don't include the view description in OPTIONS responses.
        """
        return super().options(request, *args, **kwargs)

class UserTeamViewSet(BaseModelViewSet):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer
    filter_class = UserTeamFilter

    def get_queryset(self):
        return self.queryset.viewable().annotate(
            snippet_count=Count(
                Case(
                    When(team__snippets__user=F('user'), then=1),
                    output_field=CharField(),
                )
            )
        )
