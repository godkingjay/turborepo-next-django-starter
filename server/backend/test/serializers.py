from rest_framework.serializers import ModelSerializer
from .models import Test


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"
