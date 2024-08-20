from django.urls import path
from .views import ProductListView, get_all_reviews

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product-list'),
    path('reviews/<int:product_id>/', get_all_reviews, name='reviews'),
]