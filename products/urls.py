from django.urls.conf import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductMixinView.as_view(), name='detail_view'),
    path('<int:pk>/update', views.ProductUpdateAPIViews.as_view(), name='update_view'),
    path('<int:pk>/destroy', views.ProductDestroyAPIViews.as_view(), name='destroy_view'),
    path('', views.ProductMixinView.as_view(), name='create_view'),
]
