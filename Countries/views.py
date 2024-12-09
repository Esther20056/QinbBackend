from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CountrySelection
from .Serializers import CountrySelectionSerializer
from .utils import generate_guest_id  

@api_view(['GET', 'POST'])
def saveCountry(request):
    if request.method == 'GET':
        countries = [choice[0] for choice in CountrySelection.COUNTRY_CHOICES]
        return Response(countries, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        selected_country = request.data.get('country')

        valid_countries = [choice[0] for choice in CountrySelection.COUNTRY_CHOICES]
        if selected_country in valid_countries:
            guest_id = generate_guest_id(request)
            country_data = {'country': selected_country, 'guest_id': guest_id}
            serializer = CountrySelectionSerializer(data=country_data)

            if serializer.is_valid():
                serializer.save() 
                return Response({"message": f"Country {selected_country} selected successfully!"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Invalid country selected."}, status=status.HTTP_400_BAD_REQUEST)
