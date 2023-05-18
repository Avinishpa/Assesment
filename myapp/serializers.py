from rest_framework.serializers import ModelSerializer
from .models import *

class SerializerMachine(ModelSerializer):
    class Meta:
        model = sinppet
        fields = '__all__'