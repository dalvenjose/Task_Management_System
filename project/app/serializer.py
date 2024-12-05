from rest_framework import serializers
from .models import *

class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = taskstatus
        fields = ('status')

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'