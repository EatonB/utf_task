from django.urls import include, path
from rest_framework import routers
from .views import FoodCategoryViewSet


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/foods/', FoodCategoryViewSet.as_view({'get': 'list',})),
]