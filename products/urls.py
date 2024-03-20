from django.urls.conf import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductMixinView.as_view(),
         name='product_detail_update_delete'),
    path('<int:pk>/update', views.ProductUpdateAPIViews.as_view(), name='update_view'),
    path('<int:pk>/destroy', views.ProductDestroyAPIViews.as_view(),
         name='destroy_view'),
    path('', views.ProductMixinView.as_view(), name='product_list_create'),
    path('search', views.SearchListView.as_view(), name='search'),
]
