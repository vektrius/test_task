from collections import defaultdict

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['color', 'category', 'price']
    search_fields = ['title', 'description']


@api_view(['GET'])
def get_all_reviews(request: Request, product_id: int) -> list:
    queryset: Review = Review.objects.filter(product_id=product_id)
    serializer: ReviewSerializer = ReviewSerializer(queryset, many=True)
    rate_groups: defaultdict = defaultdict(list)
    for review in serializer.data:
        rate_groups[review['rate']].append(review)

    return Response({'rate': rate, 'items': rate_groups[rate]} for rate in rate_groups)
