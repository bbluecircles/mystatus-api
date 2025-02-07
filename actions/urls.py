from django.urls import path, include
from rest_framework.routers import DefaultRouter

from actions.views import ActionViewSet, get_user_actions

router = DefaultRouter()
router.register(r'fuckyou', ActionViewSet)

urlpatterns = [
    path('user_actions/', get_user_actions, name='get_user_actions'),
]