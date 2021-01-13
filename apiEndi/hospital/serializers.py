from rest_framework import serializers
from hospital.models import Record

class RecordSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(source="getTime")
    class Meta:
        model = Record
        fields = "__all__"

