from rest_framework import serializers
from sprint.models import sprint


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = sprint
        fields = ('id','estado','horashombre',)