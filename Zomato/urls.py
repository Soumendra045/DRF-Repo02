from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router=DefaultRouter()
router.register('product',views.ProductViewSet)
router.register('customer',views.CustomerViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('order/',views.OrderList.as_view(),name='order-list'),
    path('order/<int:pk>/',views.OrderDetails.as_view()),
    path('orderitem/',views.OrderItemList.as_view()),
    path('orderitem/<int:pk>/',views.OrderDetails.as_view()),
    # path('orderitem/<str:status>/',views.OrderItemFind.as_view()),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh')
]