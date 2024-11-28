# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import CountrySelection
# from .Serializers import CountrySelectionSerializer


# @api_view(['GET', 'POST'])
# def saveCountry(request):
#     if request.method == 'GET':
#         countries = [choice[0] for choice in CountrySelection.COUNTRY_CHOICES]
#         return Response(countries, status=status.HTTP_200_OK)

#     elif request.method == 'POST':
#         selected_country = request.data.get('country')
#         valid_countries = [choice[0] for choice in CountrySelection.COUNTRY_CHOICES]
#         if selected_country in valid_countries:
#             country_data = {'country': selected_country}
#             serializer = CountrySelectionSerializer(data=country_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"message": f"Country {selected_country} selected successfully!"}, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({"error": "Invalid country selected."}, status=status.HTTP_400_BAD_REQUEST)

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CountrySelection
from .Serializers import CountrySelectionSerializer
from .utils import generate_guest_id  # Import the helper function

@api_view(['GET', 'POST'])
def saveCountry(request):
    if request.method == 'GET':
        # Respond with the list of country choices
        countries = [choice[0] for choice in CountrySelection.COUNTRY_CHOICES]
        return Response(countries, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        selected_country = request.data.get('country')

        valid_countries = [choice[0] for choice in CountrySelection.COUNTRY_CHOICES]
        if selected_country in valid_countries:
            # Use the helper function to get the guest ID from session or generate a new one
            guest_id = generate_guest_id(request)

            # Use the serializer to validate and save the selected country
            country_data = {'country': selected_country, 'guest_id': guest_id}
            serializer = CountrySelectionSerializer(data=country_data)

            if serializer.is_valid():
                serializer.save()  # Save the country selection
                return Response({"message": f"Country {selected_country} selected successfully!"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Invalid country selected."}, status=status.HTTP_400_BAD_REQUEST)
