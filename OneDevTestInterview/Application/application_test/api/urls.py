from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from api.views_fbv_cbv import *
from api.user_view import *
from django.contrib import admin
# from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token


urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('orders/', OrderList.as_view()),
    path('orders/<int:order_id>/', order_detail),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('sign-up/', sign_up_user),
    path('profile/', Profileview.as_view()),
    path('users/', UsersView.as_view())
]