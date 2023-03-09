from django.contrib import admin
from django.urls import path
from Products.views import MainCBV, ProductCBV, ProductDetailCBV, HashtagsCBV, CreateProductCBV
from django.conf.urls.static import static
from Store.settings import MEDIA_ROOT, MEDIA_URL
from users.views import RegisterCBV, LoginCBV, LogoutCBV


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainCBV.as_view()),
    path('products/', ProductCBV.as_view()),
    path('products/<int:id>/', ProductDetailCBV.as_view()),

    path('hashtags/', HashtagsCBV.as_view()),

    path('products/create/', CreateProductCBV.as_view()),

    path('users/register/', RegisterCBV.as_view()),
    path('users/login/', LoginCBV.as_view()),
    path('users/logout/', LogoutCBV.as_view())

]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
