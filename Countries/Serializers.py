# from rest_framework import serializers
# from .models import CountrySelection

# class CountrySelectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CountrySelection
#         fields = ['country']

from rest_framework import serializers
from .models import CountrySelection

class CountrySelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountrySelection
        fields = ['country', 'guest_id']

    def create(self, validated_data):
        # Automatically associate the country with the guest_id
        guest_id = validated_data['guest_id']
        country = validated_data['country']
        return CountrySelection.objects.create(guest_id=guest_id, country=country)
