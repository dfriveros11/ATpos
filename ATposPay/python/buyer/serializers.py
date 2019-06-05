from rest_framework import serializers
from . import models


class BuyerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'email',)
        model = models.Buyer