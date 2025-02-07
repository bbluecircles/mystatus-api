from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import permission_classes, api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from actions.models import Action
from actions.serializers import ActionSerializer

from dal import get_actions_by_username

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def get_user_actions(request):
    username = request.GET.get('username')
    if not username:
        return Response({'error', "'username' is a required parameter"}, status=400)

    actions = get_actions_by_username(username)
    return Response({'fuckyou': actions}, status=200)