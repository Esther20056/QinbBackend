from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ItemSerializer
from .models import Items
from rest_framework import status
from django.db.models import Q

@api_view(['GET'])
def ItemsView(request, productCategoryIdentifier):
    try:
        allItems = Items.objects.filter(productCategoryIdentifier=productCategoryIdentifier)
        serializer = ItemSerializer(allItems, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Items.DoesNotExist:
        return Response({'error': 'No items found for the given category.'}, status=status.HTTP_404_NOT_FOUND)

#    Retrieve products by their category e.g jewelries, watches etc. 
@api_view(['GET'])
def Products(request, category, subcategory=None):
    try:
        if subcategory:
            # Filter by both category and subcategory
            allItems = Items.objects.filter(category=category, subcategory=subcategory)
        else:
            # Filter by category only
            allItems = Items.objects.filter(category=category)

        serializer = ItemSerializer(allItems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Items.DoesNotExist:
        return Response({'error': 'No items found for the given category.'}, status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def ProductDataDisplay(request, name):
     description = Items.objects.filter(name = name).first()
     serializer = ItemSerializer(description)
     return Response(serializer.data, status=status.HTTP_200_OK)

#    For search filter
@api_view(['GET'])
def product_search(request):
    query = request.GET.get('query', '').strip()
    if query:
        products = Items.objects.filter(
            Q(name__icontains=query) |
            Q(category__icontains=query) |
            Q(description__icontains=query) |
            Q(subcategory__icontains=query)
        )
    else:
        products = Items.objects.all()

    serializer = ItemSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
 
 