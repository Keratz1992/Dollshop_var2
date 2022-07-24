
from django.urls import path

from dollshop1.views import homepage, category_list, product_detail, wishlist


app_name = 'dollshop'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('product_detail/<int:get_pk>/', product_detail, name='product_detail'),
    path('wishlist/', wishlist, name='wishlist'),
    path('category/<int:cate_pk>/', category_list, name='category_list')

    ]