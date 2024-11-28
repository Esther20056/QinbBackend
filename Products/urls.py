from django.urls import path
from .views import ItemsView,Products, ProductDataDisplay,product_search

urlpatterns = [
    path('products/search/', product_search, name='product-search'),
    path('product/productCategoryIdentifier/<str:productCategoryIdentifier>/', ItemsView, name='items-list'),
    path('product/category/<str:category>/<str:subcategory>/', Products, name='items-list-subcategory'),
    path('productdetails/<str:name>', ProductDataDisplay), 
]
