from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from drf.models import Women


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = '__all__'
