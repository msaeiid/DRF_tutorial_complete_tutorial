from django.urls.conf import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='detail_view'),
    path('', views.ProductCreateAPIViews.as_view(), name='create_view')
]
