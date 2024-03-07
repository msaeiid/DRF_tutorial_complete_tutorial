from django.urls.conf import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='detail_view'),
    # path('', views.ProductListCreateAPIViews.as_view(), name='create_view'),
    path('', views.product_alt_view, name='product_alt_view'),
    path('<int:pk>/', views.product_alt_view, name='product_alt_view'),
]
