from rest_framework import serializers
from api.models import Properity


class LeadSerializer(serializers.ModelSerializer):

    class Meta:

        model=Properity

        fields="__all__"