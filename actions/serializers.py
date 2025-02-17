from rest_framework import serializers
from actions.models import Action

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'
