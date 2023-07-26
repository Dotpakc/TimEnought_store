from rest_framework import serializers

from apps.order.models import Favorite


class FavoriteSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = (
            'id',
            'user',
            'product',
        )

    