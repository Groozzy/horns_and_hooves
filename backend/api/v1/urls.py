from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1 import views

router = DefaultRouter()
router.register('cart', views.CartViewSet)

urlpatterns = (
    path('', include(router.urls)),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('order/', views.OrderCreateView.as_view()),
    path('products/', views.ProductFilterAPIView.as_view()),
    path('auth/', include('djoser.urls.authtoken'))
)
