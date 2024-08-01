from rest_framework import viewsets
from .serializers import FoodListSerializer
from .models import FoodCategory, Food


class FoodCategoryViewSet(viewsets.ModelViewSet):

    food_queryset = Food.objects.filter(is_publish=True).distinct().order_by('id')

    queryset = FoodCategory.objects.filter(food__in=food_queryset).distinct().order_by('id')

    serializer_class = FoodListSerializer
