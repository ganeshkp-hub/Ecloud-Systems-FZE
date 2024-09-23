from .models import UsersDetails
from rest_framework.serializers import ModelSerializer

class UsersSerializer(ModelSerializer):

    class Meta:
        model = UsersDetails
        fields = '__all__'

